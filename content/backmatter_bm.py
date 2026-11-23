# -*- coding: utf-8 -*-
"""Bahasa Melayu front/back matter."""

HOW_TO_USE = dict(
    title="Cara menggunakan buku ini",
    kicker="Baca halaman ini sebelum bab satu",
    sections=[
        dict(h="Untuk siapa buku ini"),
        dict(p="Anda tidak perlu pengetahuan terdahulu. Bab 1 menganggap anda belum pernah membuka carta. Jika anda sudah berdagang, Bahagian II hingga IV akan memberi anda perbendaharaan kata dan set peraturan untuk apa yang sedang anda lihat, dan Bahagian V menunjukkan bagaimana kepingan itu bergabung menjadi satu pelan."),
        dict(h="Tiga pusingan bacaan"),
        dict(bullets=[
            "**Pusingan 1 — Baca.** Baca Bahagian I dan II terus tanpa berhenti untuk menghafal. Fokus pada *bentuk* hujah: konteks, struktur, kecairan, pelaksanaan.",
            "**Pusingan 2 — Buat kerja.** Kembali ke setiap bab dengan Buku Kerja terbuka dan selesaikan latihan. Di sinilah sebahagian besar pembelajaran berlaku, dan inilah pusingan yang paling ramai pembaca langkau.",
            "**Pusingan 3 — Aplikasi.** Gunakan Bahagian V dan VII sebagai manual lapangan: rancang carta sebenar (atau carta yang dimainkan semula) dengan kerangka A–B–C dan rekod setiap percubaan dalam templat jurnal.",
        ], marker="do"),
        dict(h="Struktur pengajaran yang berulang"),
        dict(p="Setiap bab konsep mengikut struktur sebelas bahagian yang sama, jadi anda sentiasa tahu di mana anda berada:"),
        dict(bullets=[
            "Takrif mesra pemula, kemudian mengapa konsep itu penting.",
            "Rupanya pada carta candle, dengan rajah beranotasi.",
            "Peraturan pengenalan langkah demi langkah, bernombor supaya boleh disemak.",
            "Sekurang-kurangnya satu contoh bullish dan satu contoh bearish jika berkaitan.",
            "Kesilapan biasa pemula, dan syarat pembatalan yang membuktikan anda salah.",
            "Latihan praktikal, diikuti serta-merta oleh jawapan dan penjelasan.",
        ], marker="info"),
        dict(h="Blok pendamping"),
        dict(p="Banyak bab berakhir dengan panel gelap kecil yang mengandungi kod QR untuk platform TIGERFX Academy yang percuma. Semuanya pilihan: tiada apa dalam buku ini bergantung padanya. **TONTON** membuka pelajaran beranimasi, **CUBA** membuka simulator carta, **UJI DIRI** membuka latihan senario, dan **ULANG KAJI** membuka pelajaran kesilapan biasa. Setiap kod menghala ke halaman yang telah disahkan wujud ketika edisi ini dihasilkan."),
        dict(h="Cara membaca rajah"),
        dict(p="Semua carta dalam buku ini bertanda **SINTETIK**. Ia ialah siri harga janaan yang dibina untuk pengajaran, bukan tangkapan skrin emas sejarah. Ini dinyatakan secara sengaja dan menonjol, kerana carta yang dipaparkan tanpa label itu menjemput pembaca mempercayai bahawa satu persediaan hipotetikal ialah hasil sebenar yang telah disahkan."),
        dict(bullets=[
            "Apabila rajah membezakan maklumat semasa analisis daripada pengesahan kemudian, satu **garis potong** putus-putus menandakan sempadan. Segala-galanya di sebelah kanannya dilukis malap: ia tidak tersedia kepada penganalisis pada masa itu.",
            "Laluan masa depan yang mungkin dilukis sebagai unjuran putus-putus samar dan dilabel sedemikian. Ia ilustrasi cabang, bukan ramalan.",
            "Harga emas pada paksi menegak bersifat ilustrasi tetapi konsisten dalaman: aritmetik dalam contoh sepadan dengan tahap yang dilukis.",
        ], marker="do"),
        dict(h="Apa yang buku ini tidak akan lakukan"),
        dict(p="Ia tidak akan menjanjikan kadar menang, pulangan bulanan, atau bahawa mana-mana corak mendedahkan niat institusi. Ia tidak akan membentangkan persediaan hipotetikal sebagai strategi yang telah disahkan. Bahagian VII menjelaskan mengapa janji seperti itu tidak jujur, dan memberi anda kaedah untuk mengukur hasil anda sendiri."),
    ],
)

NOTATION = dict(
    title="Notasi, data dan peraturan kejujuran",
    kicker="Konvensyen yang digunakan buku ini, dinyatakan sekali",
    sections=[
        dict(h="Terminologi"),
        dict(p="Terminologi Smart Money Concepts (SMC) tidak piawai. Pendidik berbeza menggunakan CHoCH, MSS dan *peralihan struktur* dengan maksud yang sedikit berbeza, dan tiada pihak berkuasa industri untuk menyelesaikannya. Daripada berpura-pura sebaliknya, setiap konsep dalam buku ini diberi **takrif operasional** — takrif yang boleh diaplikasi dan disemak — bersama nota bahawa penulis lain mungkin melabel peristiwa yang sama secara berbeza."),
        dict(table=(["Istilah di sini", "Takrif operasional dalam buku ini"], [
            ["BOS", "Penutupan candle melepasi titik swing terakhir yang disahkan, mengikut arah struktur semasa"],
            ["CHoCH", "Penutupan candle pertama yang menentang struktur semasa, melepasi swing terlindung terakhir"],
            ["MSS", "CHoCH yang disertai displacement dan, biasanya, sweep kecairan sebelumnya"],
            ["Sweep", "Harga melangkaui satu tahap dan ditutup kembali di dalamnya pada timeframe analisis"],
            ["Run", "Harga ditutup melepasi satu tahap dan meneruskan pergerakan, kekal di luarnya atau menguji semula dari sisi baharu"],
            ["FVG", "Ketidakseimbangan tiga candle: julat candle 1 tidak bertindih dengan julat candle 3, dengan candle 2 sebagai displacement"],
            ["Order block", "Candle bertentangan terakhir sebelum displacement yang memecahkan struktur"],
        ])),
        dict(h="Data"),
        dict(p="Emas (XAUUSD) disebut hingga dua perpuluhan sepanjang buku. Satu pip = 0.01, satu poin = 0.001 melainkan broker menyatakan sebaliknya. Nilai pip menganggap **kontrak piawai 100 auns** (0.01 lot = 1 auns = USD 1.00 setiap pip). Bab 37 menerangkan cara mengesahkan saiz kontrak broker anda sendiri, kerana sesetengahnya menggunakan lot 10 auns."),
        dict(h="Pip dan dolar"),
        dict(p="Jarak diberi dalam pip dengan padanan dolar dalam kurungan jika berguna, contohnya 64 pip (6.40). Harga ditulis dengan dua perpuluhan, menggunakan koma sebagai pemisah ribuan: 2,355.80."),
        dict(h="Waktu sesi"),
        dict(p="Semua waktu sesi ialah **waktu Malaysia (MYT, UTC+8)** kerana pasaran utama edisi ini ialah Malaysia. Broker pada waktu pelayan lain akan menunjukkan sempadan candle harian yang berbeza — Bab 16 menerangkan akibatnya untuk tahap hari sebelumnya."),
        dict(h="Peraturan kejujuran"),
        dict(bullets=[
            "**Boleh diperhati berbanding disimpulkan.** Data harga boleh diperhati. Kolam kecairan, niat institusi dan *order tersembunyi* ialah simpulan atau tidak dapat disahkan. Buku ini melabel yang mana satu — lihat jadual dalam Bab 13.",
            "**Tiada pandangan belakang.** Apabila rajah boleh menggoda pembaca berfikir satu entri jelas sebelum ia berkembang, garis potong dilukis dan candle kemudian dimalapkan.",
            "**Rajah sintetik.** Setiap carta ialah data harga janaan dan dilabel SINTETIK dalam kepala rajah, kaki rajah dan kapsyen.",
            "**Tiada dakwaan prestasi.** Tiada kadar menang, pulangan atau kadar kejayaan didakwa untuk mana-mana persediaan. Kemeruapan, slippage, spread dan kesilapan manusia menjadikan dakwaan sebegitu tidak bermakna tanpa sampel yang disahkan.",
            "**Aritmetik boleh diulang.** Setiap contoh berangka boleh disemak: formula dan input sentiasa ditunjukkan. Beberapa daripadanya disemak semula dalam kunci jawapan Bab 49.",
        ], marker="do"),
        dict(h="Simbol dalam rajah"),
        dict(table=(["Simbol atau warna", "Maksud"], [
            ["Cip GOLD", "Tahap kecairan atau harga entri"],
            ["Cip CYAN", "Pengesahan, peristiwa maklumat, atau fasa *B*"],
            ["HIJAU", "Struktur, candle, zon atau hasil bullish"],
            ["MERAH", "Struktur, candle, zon atau hasil bearish"],
            ["AMBER", "Peristiwa belum disahkan atau dianggap (contohnya penembusan wick)"],
            ["Garis menegak putus-putus", "Garis potong: maklumat selepas garis ini tidak tersedia semasa analisis"],
            ["Kipas putus-putus samar", "Laluan masa depan yang mungkin — ilustrasi, bukan ramalan"],
        ])),
    ],
)

GLOSSARY = [
    ("Penerimaan (acceptance)", "Harga ditutup melepasi satu tahap dan kekal di sana, bukan sekadar melaluinya dengan wick."),
    ("Julat Asia", "High dan low yang terbentuk semasa sesi Asia (sekitar 08:00–15:00 MYT untuk emas), digunakan sebagai rujukan kecairan yang dirancang awal."),
    ("Ask (tawaran)", "Harga di mana pasaran akan menjual kepada anda; harga yang lebih tinggi antara dua sebutan."),
    ("ATR", "Average True Range: ukuran julat candle biasa, kadangkala digunakan untuk menetapkan stop yang diselaras dengan kemeruapan."),
    ("Imbangan (balance)", "Kawasan harga di mana kedua-dua pihak didagangkan secara sekata; lawan kepada ketidakseimbangan."),
    ("Bes (base)", "Kelompok pendek candle yang bertindih sebelum pergerakan impulsif (lihat RBD dan DBR)."),
    ("Bid", "Harga di mana pasaran akan membeli daripada anda; harga yang lebih rendah antara dua sebutan."),
    ("BOS (Break of Structure)", "Penutupan candle melepasi titik swing terakhir yang disahkan, mengikut arah struktur semasa."),
    ("Stop pulang modal", "Mengalihkan stop-loss ke harga entri apabila dagangan dalam keuntungan. Ia mengurangkan saiz kerugian tetapi sering mengurangkan purata kemenangan."),
    ("BSL (Buy-Side Liquidity)", "Order berehat di atas pasaran — buy stop daripada peniaga penembusan dan stop-loss bagi posisi jual."),
    ("CFD", "Contract for Difference: derivatif yang membayar perbezaan harga antara pembukaan dan penutupan, tanpa memiliki aset."),
    ("CHoCH (Change of Character)", "Penutupan candle pertama yang menentang struktur semasa, melepasi titik swing terlindung terakhir."),
    ("Komisen", "Fi broker yang dikenakan setiap lot didagangkan, berasingan daripada spread."),
    ("Saiz kontrak", "Kuantiti yang diwakili satu lot piawai. Untuk emas, biasanya 100 auns troy."),
    ("Garis potong", "Dalam rajah buku ini, garis menegak putus-putus yang memisahkan maklumat tersedia semasa analisis daripada pengesahan kemudian."),
    ("Julat urus (dealing range)", "Swing high dan swing low yang mengandungi tindakan harga yang sedang dianalisis."),
    ("Zon permintaan", "Kawasan dari mana harga beredar ke atas dengan kuat; badan candle turun terakhir sebelum impuls bullish."),
    ("Displacement", "Pergerakan impulsif dengan candle berbadan lebar dan wick kecil, biasanya meninggalkan ketidakseimbangan."),
    ("Diskaun", "Separuh bawah julat urus, di bawah keseimbangan; kawasan pilihan untuk posisi beli."),
    ("Drawdown", "Penurunan ekuiti akaun daripada puncak, biasanya dinyatakan sebagai peratusan."),
    ("Keseimbangan (equilibrium)", "Tahap 50% julat urus, yang memisahkan premium daripada diskaun."),
    ("EQH / EQL", "Equal high atau equal low: dua atau lebih pivot dalam toleransi yang ditetapkan, mewujudkan kelompok kecairan."),
    ("Jangkaan (expectancy)", "Purata hasil setiap dagangan dalam gandaan R: (kadar menang × purata menang) − (kadar kalah × purata kalah)."),
    ("Struktur luaran", "Swing yang menentukan julat harga bergerak — sempadan luar."),
    ("Penembusan gagal", "Pergerakan melepasi satu tahap yang kembali ke dalamnya, memerangkap peniaga penembusan dan mencetuskan stop."),
    ("Retracement Fibonacci", "Alat yang membahagi satu leg selesai kepada nisbah (0.382, 0.5, 0.618, 0.705) untuk mencari pullback."),
    ("FVG (Fair Value Gap)", "Ketidakseimbangan tiga candle di mana julat candle pertama dan ketiga tidak bertindih."),
    ("HH / HL", "Higher high dan higher low: dua label yang bersama-sama mentakrifkan struktur bullish."),
    ("Ketidakseimbangan", "Jalur harga yang dilalui tanpa didagangkan; punca mekanikal FVG."),
    ("Struktur dalaman", "Swing lebih kecil di dalam julat luaran; struktur yang membentuk satu pullback."),
    ("Pembatalan (invalidation)", "Harga di mana alasan sesuatu dagangan tidak lagi wujud; berbeza daripada, dan biasanya sedikit melepasi, order stop-loss."),
    ("Leverage", "Nisbah antara nilai posisi dan modal akaun. Ia tidak meningkatkan risiko dengan sendirinya; saiz posisi yang melakukannya."),
    ("Kecairan", "Kemudahan melaksanakan saiz tanpa menggerakkan harga. Dalam penggunaan SMC, juga kelompok order berehat di sekitar tahap yang jelas."),
    ("Run kecairan", "Harga ditutup melalui satu tahap dan menerima di luarnya, bukan menolaknya."),
    ("Sweep kecairan", "Harga berdagang melepasi satu tahap dan ditutup kembali di dalamnya — satu lawatan, bukan penerimaan."),
    ("Lot", "Unit saiz kontrak. 1.00 lot piawai emas biasanya 100 auns."),
    ("LTF / HTF", "Timeframe lebih rendah dan lebih tinggi. LTF memberi masa; HTF memberi arah."),
    ("Margin", "Deposit yang dikunci oleh broker semasa posisi terbuka."),
    ("Mitigasi", "Penggunaan order berehat pada satu zon oleh ujian semula berturut-turut, mengurangkan kekuatan reaksi masa depannya."),
    ("MSS (Market Structure Shift)", "Dalam buku ini: CHoCH yang disertai displacement dan, biasanya, sweep sebelumnya."),
    ("Order block", "Candle bertentangan terakhir sebelum displacement yang memecahkan struktur; label deskriptif, bukan bukti order institusi."),
    ("PDH / PDL", "High dan low hari sebelumnya, diukur pada sempadan candle harian broker anda."),
    ("Pip", "Inkremen sebutan terkecil yang piawai. Untuk emas yang disebut dua perpuluhan, 1 pip = 0.01."),
    ("Poin", "Biasanya satu persepuluh pip (0.001 untuk emas)."),
    ("Premium", "Separuh atas julat urus, di atas keseimbangan; kawasan pilihan untuk posisi jual."),
    ("PWH / PWL", "High dan low minggu sebelumnya."),
    ("Skor proses", "Markah bagi pematuhan peraturan sesuatu dagangan (persediaan dinamakan, empat nombor ditulis, risiko dihormati, peraturan sesi dipatuhi), bebas daripada keuntungan."),
    ("Gandaan R", "Hasil dinyatakan dalam unit risiko awal: +2R bermaksud dua kali jumlah yang dirisikokan diperoleh."),
    ("RBD / DBR", "Rally–Base–Drop (supply) dan Drop–Base–Rally (demand): anatomi zon tiga bahagian."),
    ("Tuntutan semula (reclaim)", "Harga ditutup kembali pada sisi asal satu tahap selepas berdagang di luarnya."),
    ("Ujian semula (retest)", "Kembali ke tahap atau zon yang telah ditembusi selepas penembusan, untuk melihat sama ada ia bertahan dari sisi baharu."),
    ("Ganjaran berbanding risiko (R:R)", "Jarak sasaran dibahagi jarak stop. Kos patut dimasukkan sebelum menilai nisbah itu."),
    ("Slippage", "Perbezaan antara harga yang diminta dan harga yang dipenuhi, biasa dalam pasaran pantas."),
    ("Spread", "Perbezaan antara bid dan ask; kos yang dibayar semasa masuk."),
    ("SSL (Sell-Side Liquidity)", "Order berehat di bawah pasaran — sell stop daripada peniaga penembusan dan stop-loss bagi posisi beli."),
    ("Stop-loss", "Order yang menutup posisi pada tahap kerugian tertentu. Ia menjadi order pasaran apabila dicetuskan dan bukan harga terjamin."),
    ("Zon penawaran", "Kawasan dari mana harga beredar ke bawah dengan kuat; badan candle naik terakhir sebelum impuls bearish."),
    ("Swap", "Pembiayaan semalaman yang dikenakan atau dikreditkan pada posisi yang dipegang melepasi rollover harian."),
    ("Swing high / low", "Candle yang high (atau low) nya ialah ekstrem dalam kejiranan candle yang ditetapkan pada kedua-dua sisi."),
    ("Take profit (TP)", "Order yang menutup posisi pada tahap sasaran."),
    ("Stop bergerak (trailing)", "Stop yang dialihkan apabila dagangan berkembang. Trailing struktur hanya mengalihkannya apabila struktur bergerak."),
    ("XAUUSD", "Harga satu auns troy emas dalam dolar Amerika."),
]

REFERENCES_INTRO = (
    "Buku ini ialah sintesis pendidikan, bukan kertas penyelidikan. Sumber di bawah dipilih kerana ia stabil, boleh "
    "disahkan dan relevan dengan dakwaan dalam teks: mekanik pasaran, aritmetik risiko, asas bukti bagi analisis "
    "teknikal, dan penyelidikan tingkah laku di sebalik Bahagian VI. Ia disenaraikan supaya pembaca boleh menyemak "
    "idea asas itu secara bebas. Apabila satu dakwaan dalam buku ini bergantung pada sumber tertentu, sumber itu "
    "dinamakan. Apabila satu dakwaan ialah tafsiran penulis — sebahagian besar Smart Money Concepts — ia "
    "dibentangkan sedemikian dan bukan diatribusikan kepada kajian yang tidak wujud."
)

REFERENCES = [
    ("Bank for International Settlements (2022). *Triennial Central Bank Survey: Foreign exchange turnover in April 2022*.",
     "Konteks bagi saiz dan struktur pasaran FX global, dan bagi tumpuan aktiviti dalam sesi London dan New York yang digunakan dalam Bab 1."),
    ("World Gold Council. *Gold market statistics and demand trends* (laporan tahunan dan suku tahunan).",
     "Latar belakang peranan emas sebagai penyimpan nilai dan pemacu yang dirujuk dalam Bab 1."),
    ("CME Group. *COMEX Gold Futures (GC) contract specifications*.",
     "Konvensyen kontrak 100 auns troy yang menjadi asas aritmetik nilai pip dalam Bab 1, 5 dan 37."),
    ("European Securities and Markets Authority (ESMA). *Product intervention measures on contracts for difference* (2018, diteruskan oleh pengawal selia negara).",
     "Had leverage dan amaran risiko yang membentuk persekitaran CFD runcit seperti yang diterangkan dalam Bab 3 dan 5."),
    ("UK Financial Conduct Authority. *PS19/18: Restrictions on the sale of contracts for differences*.",
     "Rawatan pengawalseliaan selari bagi had leverage runcit, digunakan untuk perbincangan leverage dalam Bab 5."),
    ("Hull, J. C. *Options, Futures, and Other Derivatives*. Pearson.",
     "Rujukan piawai bagi mekanik niaga hadapan, margin, contango dan logik kos bawa di sebalik swap (Bab 40)."),
    ("Murphy, J. J. (1999). *Technical Analysis of the Financial Markets*. New York Institute of Finance.",
     "Rawatan klasik bagi sokongan, rintangan, trend dan corak carta yang dibandingkan dengan penggunaan SMC dalam Bab 4 dan 18."),
    ("Lo, A. W., Mamaysky, H., & Wang, J. (2000). Foundations of technical analysis: Computational algorithms, statistical inference, and empirical implementation. *Journal of Finance*, 55(4).",
     "Bukti bahawa sesetengah corak carta membawa maklumat statistik yang sederhana — bersama amaran metodologi yang menyertainya."),
    ("Sullivan, R., Timmermann, A., & White, H. (1999). Data-snooping, technical trading rule performance, and the bootstrap. *Journal of Finance*, 54(5).",
     "Masalah data-snooping: mengapa satu peraturan yang kelihatan cemerlang pada masa lalu mungkin hanya bunyi. Terus memaklumkan Bab 47 (overfitting)."),
    ("Aronson, D. R. (2007). *Evidence-Based Technical Analysis*. Wiley.",
     "Kerangka berdisiplin untuk menguji peraturan dagangan tanpa pandangan belakang atau bias pemilihan; model bagi Bab 47."),
    ("Tharp, V. K. (2006). *Trade Your Way to Financial Freedom* (ed. ke-2). McGraw-Hill.",
     "Saiz posisi, gandaan R dan jangkaan — kerangka aritmetik Bab 5, 37, 38 dan 41."),
    ("Douglas, M. (2000). *Trading in the Zone*. Prentice Hall.",
     "Pemikiran probabilistik dan psikologi melaksanakan set peraturan dalam ketidakpastian (Bab 42)."),
    ("Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.",
     "Bias kognitif — keengganan kerugian, recency, pengesahan — yang diterjemahkan oleh Bab 41 dan 42 menjadi protokol praktikal."),
    ("Barber, B. M., & Odean, T. (2000). Trading is hazardous to your wealth: The common stock investment performance of individual investors. *Journal of Finance*, 55(2).",
     "Bukti empirikal bahawa dagangan kerap merosotkan pulangan individu; konteks bagi aritmetik kos dalam Bab 38 dan 40."),
    ("Malkiel, B. G. *A Random Walk Down Wall Street* (edisi terkini). W. W. Norton.",
     "Hujah balas pasaran cekap yang perlu difahami pembaca serius sebelum menganggap mana-mana corak sebagai kelebihan."),
    ("Suruhanjaya Sekuriti Malaysia dan Bank Negara Malaysia — amaran pengguna mengenai skim dagangan forex dan emas tidak sah.",
     "Konteks pengawalseliaan tempatan bagi pendedahan risiko, relevan kepada pembaca Malaysia edisi ini."),
]

REFERENCES_NOTE = (
    "**Mengenai terminologi SMC.** Tiada literatur semakan rakan sebaya yang mentakrifkan Smart Money Concepts "
    "seperti yang digunakan dalam pendidikan runcit, dan tiada kajian terbitan yang menunjukkan bahawa *sweep "
    "kecairan* atau *order block* mendedahkan aliran order institusi. Takrif dalam buku ini oleh itu bersifat "
    "operasional: ia menerangkan tingkah laku harga yang boleh diperhati, dan ia digunakan secara konsisten supaya "
    "peraturan itu boleh diuji. Pembaca yang menemui takrif berbeza di tempat lain patut menganggap perbezaan itu "
    "sebagai isu terminologi, bukan percanggahan terhadap data harga itu sendiri."
)

DISCLAIMER = dict(
    title="Pendedahan risiko",
    kicker="Sila baca sebelum bertindak atas apa-apa dalam buku ini",
    sections=[
        dict(h="Tujuan pendidikan"),
        dict(p="Penerbitan ini disediakan untuk pendidikan sahaja. Ia bukan nasihat kewangan, bukan cadangan untuk membeli atau menjual mana-mana instrumen, dan bukan ajakan untuk membuka akaun dengan mana-mana broker. TIGERFX Academy ialah penyedia pendidikan, bukan penasihat kewangan berlesen, dan tidak menguruskan wang untuk pembaca."),
        dict(h="Risiko kerugian adalah nyata"),
        dict(p="Dagangan pertukaran asing, emas dan kontrak perbezaan membawa risiko kerugian yang besar dan tidak sesuai untuk semua orang. Leverage membesarkan kedua-dua keuntungan dan kerugian, dan anda mungkin kehilangan lebih daripada deposit awal anda bergantung pada instrumen, broker dan bidang kuasa anda. Anda tidak sepatutnya berdagang dengan wang yang anda tidak mampu untuk hilang sepenuhnya."),
        dict(bullets=[
            "Peniaga runcit kerap kehilangan wang. Pendedahan pengawal selia di beberapa bidang kuasa melaporkan bahawa majoriti akaun CFD runcit mengalami kerugian.",
            "Prestasi lalu — termasuk mana-mana contoh dalam buku ini — tidak menunjukkan hasil masa depan.",
            "Tiada persediaan, kerangka atau set peraturan boleh menghapuskan kemungkinan kerugian. Setiap dagangan dalam buku ini mempunyai syarat pembatalan justeru kerana ia boleh salah.",
        ], marker="mistake"),
        dict(h="Batasan contoh"),
        dict(p="Semua carta ialah data sintetik yang dijana untuk pengajaran. Contoh berangka bersifat ilustrasi dan dikira daripada tahap yang dilukis; ia bukan rekod dagangan yang diambil, dan bukan bukti keuntungan. Apabila kajian kes menunjukkan dagangan yang rugi, ia dimasukkan secara sengaja kerana persediaan yang sah juga kalah."),
        dict(h="Risiko pelaksanaan, broker dan teknologi"),
        dict(p="Spread, slippage, komisen, swap dan gangguan platform mempengaruhi hasil sebenar dengan cara yang tidak mampu ditunjukkan oleh carta. Order stop-loss tidak terjamin; harga boleh melangkau melepasinya. Broker berbeza menyebut harga yang sedikit berbeza. Sebelum berdagang, sahkan spesifikasi kontrak, leverage, keperluan margin dan polisi pelaksanaan dengan broker anda sendiri."),
        dict(h="Bidang kuasa"),
        dict(p="Peraturan derivatif runcit berbeza secara meluas. Pembaca di Malaysia patut merujuk Suruhanjaya Sekuriti Malaysia dan Bank Negara Malaysia bagi kedudukan pengawalseliaan semasa, dan pembaca di tempat lain patut merujuk pengawal selia mereka sendiri. Tiada apa dalam buku ini bertujuan melanggar undang-undang tempatan."),
        dict(h="Tiada jaminan ketepatan"),
        dict(p="Segala usaha telah dibuat untuk menyemak aritmetik, terminologi dan label rajah dalam edisi ini, dan laporan produksi yang disertakan mendokumenkan kerja itu. Kesilapan masih boleh wujud; pembetulan dialu-alukan melalui laman web TIGERFX Academy. Penulis dan penerbit tidak bertanggungjawab atas sebarang kerugian yang timbul daripada penggunaan bahan ini."),
        dict(h="Dapatkan nasihat bebas"),
        dict(p="Jika anda tidak pasti sama ada dagangan sesuai untuk anda, dapatkan nasihat penasihat kewangan berlesen yang bebas dan yang boleh menilai keadaan anda. Jangan bergantung pada media sosial, kursus atau buku — termasuk buku ini — sebagai ganti nasihat kewangan peribadi."),
    ],
)

ABOUT = dict(
    title="Tentang TIGERFX Academy",
    kicker="Belajar. Analisa. Berlatih. Faham.",
    sections=[
        dict(p="TIGERFX Academy ialah platform pendidikan dagangan dwibahasa (Bahasa Melayu dan Inggeris) yang dibina untuk pemula yang ingin memahami pasaran dan bukan menghafal isyarat. Kurikulumnya mengikut laluan lima peringkat yang sama seperti buku ini: asas pasaran, membaca tindakan harga, Smart Money Concepts, strategi dan pelaksanaan, dan makmal latihan lanjutan."),
        dict(p="Platform ini menyediakan pelajaran beranimasi, simulator carta dengan alat melukis dan main semula bar, latihan berasaskan senario dengan maklum balas penaakulan, dan kit risiko yang merangkumi kotak pasir saiz posisi serta jam sesi dalam waktu Malaysia. Ia percuma digunakan, tidak memerlukan pendaftaran, dan menggunakan data pengajaran sintetik sepanjang masa."),
        dict(h="Apa yang Academy sengaja tidak lakukan"),
        dict(bullets=[
            "Ia tidak menjanjikan pulangan, kadar menang atau *isyarat*.",
            "Ia tidak memerlukan anda membuka akaun broker untuk belajar.",
            "Ia tidak membentangkan hasil sintetik sebagai prestasi.",
        ], marker="mistake"),
        dict(h="Di mana untuk meneruskan"),
        dict(p="Mulakan dengan laluan pembelajaran dan kerjakan tahap yang sepadan dengan kefahaman semasa anda. Pembaca buku ini akan mendapati Tahap 3 paling berguna untuk melatih konsep SMC dalam Bahagian II hingga IV, dan mod main semula bar dalam simulator sesuai untuk latihan 100 persediaan yang disyorkan dalam Bab 47."),
    ],
)

INDEX_TERMS = [
    "Penerimaan", "Julat Asia", "BOS", "Stop pulang modal", "BSL", "CHoCH", "Garis potong", "Julat urus",
    "Zon permintaan", "Displacement", "Diskaun", "Drawdown", "Keseimbangan", "EQH", "EQL", "Jangkaan",
    "Struktur luaran", "Penembusan gagal", "Fibonacci", "FVG", "HH/HL", "Ketidakseimbangan", "Struktur dalaman",
    "Pembatalan", "Leverage", "Kecairan", "Run kecairan", "Sweep kecairan", "Lot", "Margin",
    "Mitigasi", "MSS", "Order block", "PDH/PDL", "Pip", "Premium", "Skor proses", "Gandaan R",
    "RBD/DBR", "Tuntutan semula", "Ujian semula", "Ganjaran berbanding risiko", "Slippage", "Spread", "SSL",
    "Stop-loss", "Zon penawaran", "Swap", "Swing high", "Swing low", "Stop bergerak", "XAUUSD",
]
