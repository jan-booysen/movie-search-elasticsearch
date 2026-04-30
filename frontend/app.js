const searchInput = document.getElementById("search");
const resultsDiv = document.getElementById("results");
let timeout;

searchInput.addEventListener("input", () => {
    clearTimeout(timeout);

    timeout = setTimeout(async () => {
        const query = searchInput.value;

        if (query.length < 2) {
            resultsDiv.innerHTML = "";
            return;
        }

        try {
            const res = await fetch(`http://localhost:8000/search?q=${encodeURIComponent(query)}`);
            const data = await res.json();

            if (data.length === 0) {
                resultsDiv.innerHTML = "<p>No results found 😢</p>";
                return;
            }

            resultsDiv.innerHTML = data.map(movie => `
                <div class="card">
                    <h3>${movie.title}</h3>
                    <p class="year">${movie.year || "N/A"}</p>
                    <p class="genres">${movie.genres.join(", ")}</p>
                    <div class="tags">
                        ${movie.tags.slice(0, 5).map(t => `<span>#${t}</span>`).join(" ")}
                    </div>
                </div>
            `).join("");

        } catch (err) {
            resultsDiv.innerHTML = "<p>⚠️ Error loading data</p>";
        }

    }, 300);
});