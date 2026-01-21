document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("warga-list");
    const form = document.getElementById("warga-form");

    const apiUrl = "http://127.0.0.1:8000/api/warga/";

    function renderWarga(warga) {
        const li = document.createElement("li");

        li.innerHTML = `
            <div class="bubble-header">
                <div class="nama">${warga.nama_lengkap}</div>
                <div class="nik">${warga.nik}</div>
            </div>
            <div class="alamat">${warga.alamat}</div>
            <div class="telepon">📞 ${warga.no_telepon || "-"}</div>
        `;

        return li;
    }

    function loadWarga() {
        container.innerHTML = "<li class='empty'>Memuat data...</li>";

        fetch(apiUrl)
            .then(res => res.json())
            .then(data => {
                container.innerHTML = "";

                if (data.results.length === 0) {
                    container.innerHTML = "<li class='empty'>Belum ada data warga</li>";
                    return;
                }

                data.results.forEach(warga => {
                    container.appendChild(renderWarga(warga));
                });
            })
            .catch(err => {
                container.innerHTML = "<li class='empty'>Gagal memuat data</li>";
                console.error(err);
            });
    }

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const data = {
            nik: document.getElementById("nik").value,
            nama_lengkap: document.getElementById("nama").value,
            alamat: document.getElementById("alamat").value,
            no_telepon: document.getElementById("telepon").value
        };

        fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                // "Authorization": "Token ISI_TOKEN_JIKA_PERLU"
            },
            body: JSON.stringify(data)
        })
        .then(res => {
            if (!res.ok) throw new Error("Gagal menambah warga");
            return res.json();
        })
        .then(() => {
            form.reset();
            loadWarga();
        })
        .catch(err => {
            alert("Gagal menyimpan data");
            console.error(err);
        });
    });

    loadWarga();
});
