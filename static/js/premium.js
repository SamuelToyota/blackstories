(function () {
    function storageGet(key, fallback) {
        try {
            const value = window.localStorage.getItem(key);
            return value === null ? fallback : value;
        } catch (error) {
            return fallback;
        }
    }

    function storageSet(key, value) {
        try {
            window.localStorage.setItem(key, value);
        } catch (error) {
            return undefined;
        }
    }

    function formatTime(totalSeconds) {
        const minutes = String(Math.floor(totalSeconds / 60)).padStart(2, "0");
        const seconds = String(totalSeconds % 60).padStart(2, "0");
        return `${minutes}:${seconds}`;
    }

    function normalizeText(value) {
        return String(value || "")
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .toLowerCase();
    }

    function setupLibrary() {
        const library = document.querySelector("[data-case-library]");

        if (!library) {
            return;
        }

        const search = library.querySelector("[data-case-search]");
        const cards = Array.from(library.querySelectorAll("[data-case-card]"));
        const count = library.querySelector("[data-visible-count]");
        const empty = library.querySelector("[data-filter-empty]");
        const random = library.querySelector("[data-random-case]");
        const grid = library.querySelector("[data-case-grid]");

        function visibleCards() {
            return cards.filter(function (card) {
                return !card.hidden;
            });
        }

        function updateFilter() {
            const query = normalizeText(search ? search.value.trim() : "");
            let visible = 0;

            cards.forEach(function (card) {
                const haystack = normalizeText(card.dataset.search);
                const isVisible = haystack.includes(query);

                card.hidden = !isVisible;
                card.classList.remove("is-picked");

                if (isVisible) {
                    visible += 1;
                }
            });

            if (count) {
                count.textContent = String(visible);
            }

            if (empty) {
                empty.hidden = visible !== 0;
            }
        }

        if (search) {
            search.addEventListener("input", updateFilter);
        }

        if (random) {
            random.addEventListener("click", function () {
                const pool = visibleCards();

                if (!pool.length) {
                    return;
                }

                cards.forEach(function (card) {
                    card.classList.remove("is-picked");
                });

                const pick = pool[Math.floor(Math.random() * pool.length)];
                pick.classList.add("is-picked");
                pick.scrollIntoView({ behavior: "smooth", block: "center" });

                window.setTimeout(function () {
                    window.location.href = pick.href;
                }, 460);
            });
        }

        updateFilter();
    }

    function setupStorySession() {
        const session = document.querySelector("[data-story-session]");

        if (!session) {
            return;
        }

        const storyId = session.dataset.storyId || "current";
        const prefix = `blackstories:${storyId}`;
        const timerDisplay = session.querySelector("[data-session-timer]");
        const timerToggle = session.querySelector("[data-timer-toggle]");
        const timerReset = session.querySelector("[data-timer-reset]");
        const resetCase = session.querySelector("[data-reset-case]");
        const revealButton = session.querySelector(".reveal-btn");
        const answerContainer = revealButton
            ? document.getElementById(revealButton.dataset.target)
            : null;
        const answerText = answerContainer
            ? answerContainer.querySelector(".answer-text")
            : null;
        const image = session.querySelector(".case-photo img");

        let elapsed = Number.parseInt(storageGet(`${prefix}:elapsed`, "0"), 10);
        let running = false;
        let timerId = null;

        if (!Number.isFinite(elapsed) || elapsed < 0) {
            elapsed = 0;
        }

        function renderTimer() {
            if (timerDisplay) {
                timerDisplay.textContent = formatTime(elapsed);
            }
        }

        function stopTimer() {
            running = false;
            window.clearInterval(timerId);
            timerId = null;

            if (timerToggle) {
                timerToggle.textContent = "Iniciar";
            }
        }

        function startTimer() {
            if (running) {
                return;
            }

            running = true;

            if (timerToggle) {
                timerToggle.textContent = "Pausar";
            }

            timerId = window.setInterval(function () {
                elapsed += 1;
                storageSet(`${prefix}:elapsed`, String(elapsed));
                renderTimer();
            }, 1000);
        }

        if (timerToggle) {
            timerToggle.addEventListener("click", function () {
                if (running) {
                    stopTimer();
                } else {
                    startTimer();
                }
            });
        }

        if (timerReset) {
            timerReset.addEventListener("click", function () {
                stopTimer();
                elapsed = 0;
                storageSet(`${prefix}:elapsed`, "0");
                renderTimer();
            });
        }

        if (revealButton && answerContainer && answerText) {
            revealButton.addEventListener("click", function () {
                const originalText = revealButton.textContent;
                revealButton.classList.add("is-loading");
                revealButton.textContent = "Revelando...";
                revealButton.disabled = true;

                window.fetch(revealButton.dataset.url)
                    .then(function (response) {
                        if (!response.ok) {
                            throw new Error("Reveal failed");
                        }

                        return response.json();
                    })
                    .then(function (data) {
                        answerText.textContent = data.answer;
                        answerContainer.hidden = false;
                        revealButton.hidden = true;

                        if (resetCase) {
                            resetCase.hidden = false;
                        }

                        if (image && image.dataset.resolution) {
                            image.src = image.dataset.resolution;
                            image.closest("[data-image-frame]")?.classList.add("is-solved");
                        }

                        session.classList.add("is-solved");
                        stopTimer();
                    })
                    .catch(function () {
                        revealButton.classList.remove("is-loading");
                        revealButton.textContent = "Tentar novamente";
                        revealButton.disabled = false;

                        window.setTimeout(function () {
                            revealButton.textContent = originalText;
                        }, 1600);
                    });
            });
        }

        if (resetCase) {
            resetCase.addEventListener("click", function () {
                if (answerContainer && answerText) {
                    answerText.textContent = "";
                    answerContainer.hidden = true;
                }

                if (revealButton) {
                    revealButton.hidden = false;
                    revealButton.disabled = false;
                    revealButton.classList.remove("is-loading");
                        revealButton.textContent = "Revelar a verdade";
                }

                if (image && image.dataset.original) {
                    image.src = image.dataset.original;
                    image.closest("[data-image-frame]")?.classList.remove("is-solved");
                }

                resetCase.hidden = true;
                session.classList.remove("is-solved");
            });
        }

        renderTimer();
    }

    function setupStoryForm() {
        const form = document.querySelector("[data-story-form]");

        if (!form) {
            return;
        }

        const inputs = Array.from(form.querySelectorAll("[data-file-input]"));

        inputs.forEach(function (input) {
            input.addEventListener("change", function () {
                const key = input.dataset.fileInput;
                const preview = form.querySelector(`[data-file-preview="${key}"]`);
                const fileName = form.querySelector(`[data-file-name="${key}"]`);
                const file = input.files && input.files[0];

                if (!file) {
                    if (preview) {
                        preview.hidden = true;
                        preview.removeAttribute("src");
                    }

                    if (fileName) {
                        fileName.textContent = "Nenhum arquivo selecionado";
                    }

                    return;
                }

                if (preview) {
                    preview.src = URL.createObjectURL(file);
                    preview.hidden = false;
                }

                if (fileName) {
                    fileName.textContent = file.name;
                }
            });
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        setupLibrary();
        setupStorySession();
        setupStoryForm();
    });
})();
