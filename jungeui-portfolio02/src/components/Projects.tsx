const projects = [
  {
    title: "Dotori College Essay Assistant",
    description: "AI-powered admissions assistant using Next.js, Spring Boot, and PostgreSQL.",
    link: "https://github.com/EuljeHoon/dotori-web",
  },
  {
    title: "GPU Image Editor",
    description: "OpenGL-based C++ image editor with real-time GPU rendering.",
    link: "https://github.com/EuljeHoon/GPU_Image_Editor",
  },
  {
    title: "Jehoon Portfolio",
    description: "Portfolio website built with Next.js and Tailwind CSS.",
    link: "https://github.com/EuljeHoon/jehoon_website",
  },
];

export default function Projects() {
    return (
        <section id="projects" className="py-20 px-6 bg-black text-white">
        <h2 className="text-3xl font-bold mb-10 text-center">Projects</h2>
        <div className="flex flex-col gap-8 max-w-3xl mx-auto">
            {projects.map((proj, idx) => (
            <div key={idx} className="bg-zinc-800 p-6 rounded-lg shadow hover:shadow-lg transition">
                <h3 className="text-xl font-semibold mb-2">{proj.title}</h3>
                <p className="text-zinc-400 mb-4">{proj.description}</p>
                <a
                href={proj.link}
                className="text-blue-400 hover:underline"
                target="_blank"
                rel="noopener noreferrer"
                >
                View on GitHub →
                </a>
            </div>
            ))}
        </div>
        </section>
    );
}