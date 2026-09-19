export default function Contact() {
    return (
        <section id="contact" className="py-20 px-4 flex flex-col items-center justify-center text-center bg-black text-white" >
        <h2 className="text-3xl font-bold mb-6">Contact Me</h2>
            <a href="mailto:justicelee.dev@gmail.com" className="text-zinc-400 hover:text-white transition mb-2">
            justicelee.dev@gmail.com
            </a>
        <div className="flex flex-col sm:flex-row gap-4 mt-6">
            <a
            href="https://drive.google.com/file/d/14exGbMtdx9VvoiP6xgKOVbtPImdn3gE3/view?usp=sharing"
            target="_blank"
            rel="noopener noreferrer"
            className="bg-white text-black px-6 py-2 rounded hover:bg-zinc-200 transition"
            >
            View Resume
            </a>
            <a
            href="https://github.com/JungeuiLee"
            target="_blank"
            rel="noopener noreferrer"
            className="bg-white text-black px-6 py-2 rounded hover:bg-zinc-200 transition"
            >
            View GitHub
            </a>
            <a
            href="https://www.linkedin.com/in/jungeui1297/"
            target="_blank"
            rel="noopener noreferrer"
            className="bg-white text-black px-6 py-2 rounded hover:bg-zinc-200 transition"
            >
            View LinkedIn
            </a>
        </div>
        </section>
    );
}