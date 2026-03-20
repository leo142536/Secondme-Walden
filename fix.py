with open("build_html.py", "r", encoding="utf-8") as f:
    text = f.read()
import re
text = re.sub(r'user_body_match = re\.search\(.*?# Add existing screens', 'merged_html += user_body_content\n\n# Add existing screens', text, flags=re.DOTALL)
text = 'user_body_content = """\\n' + """
<!-- Immersive Background Elements -->
<div class="immersive-bg">
<div class="blob w-[800px] h-[800px] bg-[#d1fae5] -top-40 -left-40"></div>
<div class="blob w-[600px] h-[600px] bg-[#fdf2f8] top-1/2 -right-20" style="animation-delay: -5s;"></div>
<div class="blob w-[700px] h-[700px] bg-[#e0f2fe] -bottom-40 left-1/4" style="animation-delay: -10s;"></div>
<!-- Forest Texture Overlay -->
<div class="absolute inset-0 opacity-10 pointer-events-none mix-blend-overlay" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuBuKvTv35aSdduM_Xe41k8C80VP568Wv0gMprz62qH0dnzVJiwnfxKuPPb3r05LIW2Mt0__NtJVXJ4-zqsCun6VdVkDntZV1vR5G_LOOs9na5bHFvS5Y0VZTn1tDRc_goXNWRZhorY76_QboAiFCeNe0YPn2t1B0h69zDHTlKPVDZAdwC5vAWGrmxZmJH294O3byM3aHhqawkDgGJPJBAwEo77Ln9_tTSyeQsIwuZyhPDgd3ZhwezyjaRg-WRLnliIKVgfW70rmuLbg');"></div>
</div>
<!-- TopAppBar -->
<nav class="bg-white/30 backdrop-blur-2xl fixed top-0 w-full z-50 border-b border-white/20">
<div class="flex justify-between items-center px-8 py-5 w-full max-w-[1440px] mx-auto">
<span class="text-3xl font-serif italic font-black text-emerald-950">Walden</span>
<div class="flex items-center gap-10">
<div class="hidden md:flex items-center gap-10 font-serif italic tracking-wider text-lg">
<a class="text-emerald-900 font-black border-b-2 border-emerald-900" href="#">Breathe</a>
<a class="text-emerald-800/60 hover:text-emerald-900 transition-all" href="#">Reflect</a>
<a class="text-emerald-800/60 hover:text-emerald-900 transition-all" href="#">Garden</a>
</div>
<div class="flex items-center gap-4">
<button class="material-symbols-outlined text-emerald-950 p-3 hover:bg-white/40 rounded-full transition-all text-2xl">settings</button>
<button class="material-symbols-outlined text-emerald-950 p-3 hover:bg-white/40 rounded-full transition-all text-2xl">eco</button>
</div>
</div>
</div>
</nav>
<main class="pt-28 pb-40 px-6 w-full max-w-[1440px] mx-auto space-y-12">
<!-- Hero Section: Full Screen Feel -->
<section class="relative h-[600px] rounded-[3rem] overflow-hidden flex items-center justify-center shadow-2xl">
<img alt="Forest Background" class="absolute inset-0 w-full h-full object-cover scale-105 hover:scale-100 transition-transform duration-[10s]" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBXmNGl_js19_T3kOOrYRuwSSmvXZUKiQVIO6tjtX33WDDGUCpwnZ4z6GS82qNyFuH5mRyAVeuJ8FkShSB7znuhzszWv3aEJ6lYcmRrC61_4qBuZAvwnw2s_S9ID5Nc4gAkEGWldM6uIpUedcdPQ_45MBeszqI8n7Hc_DEr3AUSHzKZpTAwMcDUGYYyrYwPnUdCQ54JPFf1MpC0W4R7BwxSnDiEEUPXh3s1MeGVXO5b1gr9nsxf990TpEgZFox_MowHzg1_pSQEU3hY"/>
<div class="absolute inset-0 bg-gradient-to-tr from-emerald-900/40 via-transparent to-rose-200/20"></div>
<div class="relative z-10 w-full max-w-4xl px-8">
<div class="glass-card p-16 rounded-[2.5rem] shadow-2xl text-center border-white/40">
<h2 class="serif-text text-5xl md:text-6xl text-emerald-950 mb-8 font-black leading-[1.3]">
                    您的心灵已经漫游太久，<br/>此刻，让呼吸带您归家。
                </h2>
<p class="text-emerald-900/80 text-xl font-medium tracking-wide leading-relaxed max-w-2xl mx-auto">
                    Your digital fatigue is at 78%. The meadow invites you to set down the screen and find stillness for a moment.
                </p>
</div>
</div>
</section>
<!-- Intervention Dashboard: Expanded Bento Grid -->
<div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-stretch">
<!-- Digital Fatigue Indicator -->
<div class="md:col-span-8 glass-card rounded-[3rem] p-12 flex flex-col justify-between min-h-[450px]">
<div class="relative z-10">
<div class="flex items-center gap-4 mb-6">
<span class="material-symbols-outlined text-primary text-5xl">water_drop</span>
<h3 class="serif-text text-4xl text-emerald-950 font-black tracking-tight">数字疲劳监测 <span class="text-2xl font-normal opacity-60">Fatigue Index</span></h3>
</div>
<p class="text-emerald-900/70 text-xl max-w-xl mb-12 font-medium">
                    The current workload has reached a threshold. We recommend a 15-minute garden meditation to restore your creative energy.
                </p>
</div>
<div class="relative h-64 flex items-end gap-4 px-4">
<div class="flex-1 bg-emerald-700/10 rounded-t-[2rem] h-[40%] hover:h-[50%] transition-all duration-500"></div>
<div class="flex-1 bg-emerald-700/15 rounded-t-[2rem] h-[60%] hover:h-[70%] transition-all duration-500"></div>
<div class="flex-1 bg-emerald-700/40 rounded-t-[2rem] h-[95%] hover:h-[100%] transition-all duration-500"></div>
<div class="flex-1 bg-emerald-700/20 rounded-t-[2rem] h-[50%] hover:h-[60%] transition-all duration-500"></div>
<div class="flex-1 bg-emerald-700/10 rounded-t-[2rem] h-[30%] hover:h-[40%] transition-all duration-500"></div>
<div class="flex-1 bg-emerald-700/25 rounded-t-[2rem] h-[45%] hover:h-[55%] transition-all duration-500"></div>
<div class="flex-1 bg-emerald-700/10 rounded-t-[2rem] h-[20%] hover:h-[30%] transition-all duration-500"></div>
</div>
</div>
<!-- Screen Time -->
<div class="md:col-span-4 glass-card rounded-[3rem] p-12 flex flex-col items-center justify-center text-center">
<div class="relative w-56 h-56 flex items-center justify-center mb-10">
<svg class="w-full h-full -rotate-90">
<circle class="text-emerald-100/50" cx="112" cy="112" fill="transparent" r="100" stroke="currentColor" stroke-width="12"></circle>
<circle class="text-emerald-700" cx="112" cy="112" fill="transparent" r="100" stroke="currentColor" stroke-dasharray="628" stroke-dashoffset="150" stroke-linecap="round" stroke-width="12"></circle>
</svg>
<div class="absolute inset-0 flex flex-col items-center justify-center">
<span class="material-symbols-outlined text-emerald-800 text-4xl mb-1">eco</span>
<span class="text-5xl font-black text-emerald-950">6.4h</span>
</div>
</div>
<h4 class="serif-text text-3xl text-emerald-950 font-black">Screen Usage</h4>
<p class="text-lg text-emerald-900/60 mt-4 font-bold">12% decrease from yesterday</p>
</div>
<!-- Breathe Card: Immersive Background within Card -->
<div class="md:col-span-12 relative overflow-hidden glass-card rounded-[3rem] p-16 flex flex-col md:flex-row items-center gap-12 group">
<div class="absolute inset-0 bg-gradient-to-r from-emerald-100/20 to-purple-100/20 pointer-events-none"></div>
<div class="flex-1 relative z-10">
<span class="material-symbols-outlined text-emerald-700 text-6xl mb-6 inline-block" style="font-variation-settings: 'FILL' 1;">air</span>
<h3 class="serif-text text-5xl text-emerald-950 font-black mb-6">呼吸练习：林间晨雾</h3>
<p class="text-emerald-900/70 text-2xl font-medium leading-relaxed max-w-3xl">
                    A sensory-guided breathing session to clear mental fog. Visualized by soft gradients of mint and lavender, designed to mimic the rhythm of dawn.
                </p>
</div>
<button onclick="startDebate()" class="relative z-10 bg-emerald-950 text-white px-16 py-7 rounded-full text-2xl font-black shadow-2xl hover:bg-emerald-800 hover:scale-105 active:scale-95 transition-all duration-300">
                开始干预 (Start Session)
            </button>
</div>
</div>
<!-- Integrated Language Toggle -->
<div class="flex justify-center pb-12">
<div class="glass-card rounded-full p-2 flex items-center shadow-xl border-white/50">
<button class="flex items-center gap-3 px-8 py-4 rounded-full bg-emerald-950 text-white font-black shadow-lg">
<span class="material-symbols-outlined text-xl">language</span>
<span class="font-serif text-lg">English (EN)</span>
</button>
<button class="flex items-center gap-3 px-8 py-4 rounded-full text-emerald-900/60 hover:text-emerald-900 font-bold transition-colors">
<span class="material-symbols-outlined text-xl">translate</span>
<span class="font-serif text-lg">Chinese (ZH)</span>
</button>
</div>
</div>
</main>
<!-- BottomNavBar -->
<nav class="fixed bottom-0 left-0 w-full z-50 flex justify-around items-center px-10 pb-10 pt-6 bg-white/40 backdrop-blur-3xl rounded-t-[4rem] border-t border-white/30 hidden md:flex">
<a class="flex flex-col items-center justify-center bg-emerald-950 text-white rounded-[2.5rem] px-8 py-4 shadow-xl scale-110" href="#">
<span class="material-symbols-outlined text-3xl" style="font-variation-settings: 'FILL' 1;">air</span>
<span class="font-sans text-xs font-black tracking-[0.2em] uppercase mt-2">Breathe</span>
</a>
<a class="flex flex-col items-center justify-center text-emerald-950/40 hover:text-emerald-950 transition-all px-8 py-4" href="#">
<span class="material-symbols-outlined text-3xl">auto_awesome</span>
<span class="font-sans text-xs font-bold tracking-[0.2em] uppercase mt-2">Reflect</span>
</a>
<a class="flex flex-col items-center justify-center text-emerald-950/40 hover:text-emerald-950 transition-all px-8 py-4" href="#">
<span class="material-symbols-outlined text-3xl">psychology</span>
<span class="font-sans text-xs font-bold tracking-[0.2em] uppercase mt-2">Garden</span>
</a>
<a class="flex flex-col items-center justify-center text-emerald-950/40 hover:text-emerald-950 transition-all px-8 py-4" href="#">
<span class="material-symbols-outlined text-3xl">person</span>
<span class="font-sans text-xs font-bold tracking-[0.2em] uppercase mt-2">Profile</span>
</a>
</nav>
""" + '\n' + text

with open("build_html.py", "w", encoding="utf-8") as f:
    f.write(text)
