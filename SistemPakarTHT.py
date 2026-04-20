import tkinter as tk
from tkinter import ttk, messagebox

GEJALA = {
    "G1": "Nafas abnormal", "G2": "Suara serak", "G3": "Perubahan kulit",
    "G4": "Telinga penuh", "G5": "Nyeri bicara/menelan", "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher", "G8": "Pendarahan hidung", "G9": "Telinga berdenging",
    "G10": "Air liur menetes", "G11": "Perubahan suara", "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung", "G14": "Serangan vertigo", "G15": "Getah bening membesar",
    "G16": "Leher bengkak", "G17": "Hidung tersumbat", "G18": "Infeksi sinus",
    "G19": "Berat badan turun", "G20": "Nyeri telinga", "G21": "Selaput lendir merah",
    "G22": "Benjolan di leher", "G23": "Tubuh tidak seimbang", "G24": "Bola mata bergerak",
    "G25": "Nyeri wajah", "G26": "Dahi sakit", "G27": "Batuk",
    "G28": "Tumbuh di mulut", "G29": "Benjolan di leher", "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga", "G32": "Tenggorokan gatal", "G33": "Hidung meler",
    "G34": "Tuli", "G35": "Mual muntah", "G36": "Letih lesu", "G37": "Demam",
}

PENYAKIT = [
    {"nama": "Tonsilitis",                  "gejala": ["G37","G12","G5","G27","G6","G21"]},
    {"nama": "Sinusitis Maksilaris",        "gejala": ["G37","G12","G27","G17","G33","G36","G29"]},
    {"nama": "Sinusitis Frontalis",         "gejala": ["G37","G12","G27","G17","G33","G36","G21","G26"]},
    {"nama": "Sinusitis Edmoidalis",        "gejala": ["G37","G12","G27","G17","G33","G36","G21","G30","G13","G26"]},
    {"nama": "Sinusitis Sfenoidalis",       "gejala": ["G37","G12","G27","G17","G33","G36","G29","G7"]},
    {"nama": "Abses Peritonsiler",          "gejala": ["G37","G12","G6","G15","G2","G29","G10"]},
    {"nama": "Faringitis",                  "gejala": ["G37","G5","G6","G7","G15"]},
    {"nama": "Kanker Laring",               "gejala": ["G5","G27","G6","G15","G2","G19","G1"]},
    {"nama": "Deviasi Septum",              "gejala": ["G37","G17","G20","G8","G18","G25"]},
    {"nama": "Laringitis",                  "gejala": ["G37","G5","G15","G16","G32"]},
    {"nama": "Kanker Leher & Kepala",       "gejala": ["G5","G22","G8","G28","G3","G11"]},
    {"nama": "Otitis Media Akut",           "gejala": ["G37","G20","G35","G31"]},
    {"nama": "Contact Ulcers",              "gejala": ["G5","G2"]},
    {"nama": "Abses Parafaringeal",         "gejala": ["G5","G16"]},
    {"nama": "Barotitis Media",             "gejala": ["G12","G20"]},
    {"nama": "Kanker Nasofaring",           "gejala": ["G17","G8"]},
    {"nama": "Kanker Tonsil",               "gejala": ["G6","G29"]},
    {"nama": "Neuronitis Vestibularis",     "gejala": ["G35","G24"]},
    {"nama": "Meniere",                     "gejala": ["G20","G35","G14","G4"]},
    {"nama": "Tumor Syaraf Pendengaran",    "gejala": ["G12","G34","G23"]},
    {"nama": "Kanker Leher Metastatik",     "gejala": ["G29"]},
    {"nama": "Osteosklerosis",              "gejala": ["G34","G9"]},
    {"nama": "Vertigo Postular",            "gejala": ["G24"]},
]

def inferensi(gejala_dipilih: list[str]) -> list[dict]:
    if not gejala_dipilih:
        return []

    hasil = []
    for p in PENYAKIT:
        cocok = [g for g in p["gejala"] if g in gejala_dipilih]
        if not cocok:
            continue
        coverage  = len(cocok) / len(p["gejala"])   
        precision = len(cocok) / len(gejala_dipilih) 
        skor = round(coverage * 0.6 + precision * 0.4, 4)
        hasil.append({
            "nama":      p["nama"],
            "gejala":    p["gejala"],
            "cocok":     cocok,
            "coverage":  coverage,
            "precision": precision,
            "skor":      skor,
        })

    hasil.sort(key=lambda x: x["skor"], reverse=True)
    return hasil[:5]  

BG_MAIN = "#0d1117"     
BG_PANEL = "#161b22"    
FG_TEXT = "#c9d1d9"     
ACCENT_1 = "#00ffcc"    
ACCENT_2 = "#ff0055"    
FONT_MAIN = ("Consolas", 10)
FONT_TITLE = ("Consolas", 14, "bold")

class SistemPakarTHT(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("THT_SYS // TERMINAL_DIAGNOSIS v1.0")
        self.geometry("1000x700")
        self.resizable(True, True)
        self.configure(bg=BG_MAIN)

        self.var_gejala = {k: tk.BooleanVar() for k in GEJALA}
        self.var_search = tk.StringVar()
        self.var_search.trace_add("write", lambda *_: self._filter_gejala())

        self._build_ui()

    def _build_ui(self):
        header = tk.Frame(self, bg=BG_MAIN, pady=10, highlightbackground=ACCENT_1, highlightthickness=1)
        header.pack(fill="x", padx=10, pady=10)
        tk.Label(header, text="> THT_DIAGNOSIS_SYSTEM_ACTIVE", font=FONT_TITLE, fg=ACCENT_1, bg=BG_MAIN).pack(anchor="w", padx=10)
        tk.Label(header, text="> STATUS: WAITING FOR INPUT...", font=FONT_MAIN, fg=ACCENT_2, bg=BG_MAIN).pack(anchor="w", padx=10)

        body = tk.Frame(self, bg=BG_MAIN)
        body.pack(fill="both", expand=True, padx=10, pady=0)
        body.columnconfigure(0, weight=4) 
        body.columnconfigure(1, weight=3, minsize=400) 
        body.rowconfigure(0, weight=1)

        self._panel_hasil(body)
        self._panel_gejala(body)

    def _panel_gejala(self, parent):
        frame = tk.LabelFrame(parent, text=" [ INPUT_GEJALA ] ", font=FONT_MAIN, bg=BG_MAIN, fg=ACCENT_1, padx=10, pady=10, highlightbackground="#30363d")
        frame.grid(row=0, column=1, sticky="nsew", padx=(5,0), pady=(0,10))
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)

        # Search Bar terminal style
        sf = tk.Frame(frame, bg=BG_MAIN)
        sf.grid(row=0, column=0, sticky="ew", pady=(0,10))
        tk.Label(sf, text="root@tht:~$ search_gejala ", bg=BG_MAIN, fg=ACCENT_2, font=FONT_MAIN).pack(side="left")
        tk.Entry(sf, textvariable=self.var_search, font=FONT_MAIN, bg=BG_PANEL, fg=ACCENT_1, insertbackground=ACCENT_1, relief="flat").pack(side="left", fill="x", expand=True)

        # Scrollable area
        container = tk.Frame(frame, bg=BG_MAIN)
        container.grid(row=1, column=0, sticky="nsew")
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        canvas = tk.Canvas(container, bg=BG_PANEL, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.chk_frame = tk.Frame(canvas, bg=BG_PANEL)
        self.canvas_window = canvas.create_window((0, 0), window=self.chk_frame, anchor="nw")

        def _on_resize(e):
            canvas.itemconfig(self.canvas_window, width=e.width)
        canvas.bind("<Configure>", _on_resize)
        self.chk_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.chk_widgets = {}
        self._render_checkboxes()

        # Terminal Actions
        btn_frame = tk.Frame(frame, bg=BG_MAIN)
        btn_frame.grid(row=2, column=0, sticky="ew", pady=(10,0))
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        tk.Button(btn_frame, text="[ EXECUTE_DIAGNOSIS ]", font=("Consolas", 11, "bold"), bg=ACCENT_1, fg="#000", activebackground="#00cca3", relief="flat", cursor="hand2", command=self._diagnosa).grid(row=0, column=0, sticky="ew", padx=(0,5))
        tk.Button(btn_frame, text="[ CLEAR_SYS ]", font=("Consolas", 11, "bold"), bg="#30363d", fg=FG_TEXT, activebackground="#484f58", relief="flat", cursor="hand2", command=self._reset).grid(row=0, column=1, sticky="ew")

        self.lbl_count = tk.Label(frame, text="SELECTED: 0 PARAMETERS", font=FONT_MAIN, fg=ACCENT_2, bg=BG_MAIN)
        self.lbl_count.grid(row=3, column=0, sticky="w", pady=(5,0))

    def _render_checkboxes(self, filter_str=""):
        for w in self.chk_frame.winfo_children():
            w.destroy()
        self.chk_widgets.clear()

        keys = [k for k in GEJALA if filter_str.lower() in GEJALA[k].lower() or filter_str.lower() in k.lower()]
        
        # Susun dalam 2 kolom agar tidak terlalu panjang
        for i, k in enumerate(keys):
            row = i // 2
            col = i % 2
            cb = tk.Checkbutton(self.chk_frame, variable=self.var_gejala[k], text=f"[{k}] {GEJALA[k]}", font=FONT_MAIN, bg=BG_PANEL, fg=FG_TEXT, selectcolor=BG_MAIN, activebackground=BG_PANEL, activeforeground=ACCENT_1, anchor="w", command=self._update_count)
            cb.grid(row=row, column=col, sticky="w", padx=10, pady=4)
            self.chk_widgets[k] = cb

    def _filter_gejala(self):
        self._render_checkboxes(self.var_search.get())

    def _update_count(self):
        n = sum(1 for v in self.var_gejala.values() if v.get())
        self.lbl_count.config(text=f"SELECTED: {n} PARAMETERS")

    def _panel_hasil(self, parent):
        frame = tk.LabelFrame(parent, text=" [ OUTPUT_TERMINAL ] ", font=FONT_MAIN, bg=BG_MAIN, fg=ACCENT_1, padx=10, pady=10, highlightbackground="#30363d")
        frame.grid(row=0, column=0, sticky="nsew", padx=(0,5), pady=(0,10))
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        canvas = tk.Canvas(frame, bg=BG_MAIN, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.result_frame = tk.Frame(canvas, bg=BG_MAIN)
        self.result_win = canvas.create_window((0, 0), window=self.result_frame, anchor="nw")

        def _on_resize(e):
            canvas.itemconfig(self.result_win, width=e.width)
        canvas.bind("<Configure>", _on_resize)
        self.result_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self._show_placeholder()

    def _show_placeholder(self):
        for w in self.result_frame.winfo_children():
            w.destroy()
        tk.Label(self.result_frame, text="\n\n\n\n> SYSTEM IDLE...\n> AWAITING GEJALA SELECTION\n> PRESS [EXECUTE_DIAGNOSIS] TO START SCAN", font=FONT_MAIN, fg="#484f58", bg=BG_MAIN, justify="left").pack(anchor="w", padx=20)

    def _tampilkan_hasil(self, hasil):
        for w in self.result_frame.winfo_children():
            w.destroy()

        if not hasil:
            tk.Label(self.result_frame, text="\n\n> ERROR 404: NO MATCH FOUND\n> SYSTEM COULD NOT IDENTIFY DISEASE", font=FONT_TITLE, fg=ACCENT_2, bg=BG_MAIN, justify="left").pack(anchor="w", padx=20)
            return

        for i, h in enumerate(hasil):
            is_top = (i == 0)
            card_color = ACCENT_1 if is_top else FG_TEXT
            bg_color = BG_PANEL if is_top else BG_MAIN
            
            card = tk.Frame(self.result_frame, bg=bg_color, highlightbackground=card_color, highlightthickness=1)
            card.pack(fill="x", padx=5, pady=8)

            inner = tk.Frame(card, bg=bg_color, padx=15, pady=10)
            inner.pack(fill="x")

            # Label Prioritas
            rank = ">> PRIMARY_MATCH" if is_top else f"> ALTERNATIVE_{i}"
            tk.Label(inner, text=rank, font=("Consolas", 9, "bold"), fg=BG_MAIN if is_top else card_color, bg=card_color).pack(anchor="w")

            # Nama Penyakit
            tk.Label(inner, text=f"[{h['nama'].upper()}]", font=("Consolas", 14, "bold"), fg=card_color, bg=bg_color).pack(anchor="w", pady=(5,2))

            # ASCII Progress Bar untuk Skor
            skor_pct = int(h["skor"] * 100)
            filled = skor_pct // 10
            ascii_bar = "█" * filled + "░" * (10 - filled)
            
            tk.Label(inner, text=f"SYS_SCORE : [{ascii_bar}] {skor_pct}%", font=FONT_MAIN, fg=ACCENT_1, bg=bg_color).pack(anchor="w")
            tk.Label(inner, text=f"COVERAGE  : {int(h['coverage']*100)}% | PRECISION : {int(h['precision']*100)}%", font=("Consolas", 9), fg="#8b949e", bg=bg_color).pack(anchor="w", pady=(0,8))

            # Rincian Gejala bergaya Terminal List
            tk.Label(inner, text="MATCHED_RULES:", font=("Consolas", 8), fg="#8b949e", bg=bg_color).pack(anchor="w")
            
            wrap = tk.Frame(inner, bg=bg_color)
            wrap.pack(fill="x")
            
            for g in h["gejala"]:
                match = g in h["cocok"]
                prefix = "[+]" if match else "[-]"
                f_color = ACCENT_1 if match else "#484f58"
                tk.Label(wrap, text=f"{prefix} {g}", font=("Consolas", 9), fg=f_color, bg=bg_color).pack(side="left", padx=4, pady=2)

    # ── Aksi Tombol ──────────────────────────────────────────────────────────
    def _diagnosa(self):
        gejala_dipilih = [k for k, v in self.var_gejala.items() if v.get()]
        if not gejala_dipilih:
            messagebox.showwarning("SYS_WARN", "NO PARAMETERS SELECTED!")
            return
        hasil = inferensi(gejala_dipilih)
        self._tampilkan_hasil(hasil)

    def _reset(self):
        for v in self.var_gejala.values():
            v.set(False)
        self.var_search.set("")
        self._render_checkboxes()
        self._update_count()
        self._show_placeholder()

if __name__ == "__main__":
    app = SistemPakarTHT()
    app.mainloop()