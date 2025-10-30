export default function Skills() {
    return (
        <section id="skills" className="py-20 px-6 text-white bg-black">
        <h2 className="text-3xl font-bold text-center mb-10">Skills</h2>
        <div className="max-w-4xl mx-auto grid grid-cols-1 sm:grid-cols-2 gap-8">
            <div>
            <h3 className="text-xl font-semibold mb-2">Languages</h3>
            <p className="text-zinc-400">Java, C, C++, Python, JavaScript, TypeScript, HTML, CSS</p>
            </div>
            <div>
            <h3 className="text-xl font-semibold mb-2">Frameworks</h3>
            <p className="text-zinc-400">React, Next.js, Express, Spring Boot, Tailwind CSS</p>
            </div>
            <div>
            <h3 className="text-xl font-semibold mb-2">Tools</h3>
            <p className="text-zinc-400">Git, VS Code, IntelliJ, Linux, GDB</p>
            </div>
        </div>
        </section>
    );
}