export default function Contact() {
    return (
        <section className="py-20 px-4 flex flex-col items-center justify-center text-center bg-black text-white">
        <h2 className="text-3xl font-bold mb-6">Contact Me</h2>
            <p className="text-zinc-400 mb-2">Email: justicelee.dev@gmail.com</p>
        <div className="flex flex-col sm:flex-row gap-4 mt-6">
            <a
            href="#resume"
            className="bg-white text-black px-6 py-2 rounded hover:bg-zinc-200 transition"
            >
            View Resume
            </a>
            <a
            href="resume link"
            target="_blank"
            rel="noopener noreferrer"
            className="bg-white text-black px-6 py-2 rounded hover:bg-zinc-200 transition"
            >
            View GitHub
            </a>
            <a
            href="https://www.linkedin.com/in/jungeui-lee-49b264356/"
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