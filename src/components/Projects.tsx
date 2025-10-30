'use client'

import { useState } from "react";

const projects = [
  {
    title: "Jungeui Portfolio",
    description: "Portfolio website built with Next.js and Tailwind CSS.",
    details: "This portfolio website represents the next step in my self-taught front-end learning journey. Building upon the foundational web development skills I gained through HTML, CSS, and JavaScript, I expanded into modern frameworks and tools — using Next.js, React, TypeScript, and Tailwind CSS to create a clean, responsive, and interactive portfolio. The project focuses on design consistency, smooth user interaction, and scalability for future updates.",
    link: "https://github.com/justice-1297-dev/jungeui_website",
    image: "/jungeuiPortfolio.png",
  },
  {
    title: "GPU Image Editor",
    description: "OpenGL-based C++ image editor with real-time GPU rendering.",
    details: "Developed a C++ image editor powered by OpenGL for real-time GPU-based image processing. Implemented features such as texture loading, pixel manipulation, and shader-based color correction to achieve efficient, real-time rendering. This project deepened my understanding of GPU programming, shader pipelines, and the integration between CPU and GPU operations for visual computing.",
    link: "https://github.com/JungeuiLee/GPU_Image_Editor.git",
    image: "/GPUImageEditor.png",
  },
  {
    title: "Online store Clone",
    description: "Built a clone website while independently learning HTML, CSS, and JavaScript.",
    details: "Created a multi-page online fashion store clone while self-learning front-end development. Using only HTML, CSS, and JavaScript, I focused on replicating a realistic layout with product sections, category pages, and a responsive design. This project represents the practical application of my self-taught web fundamentals and an early step toward more advanced frameworks.",
    link: "https://github.com/JungeuiLee/randonWalk-clone.git",
    image: "/RandomWalk.png",
  },
  {
    title: "First Portfolio",
    description: "Built a personal website while independently learning HTML, CSS, and JavaScript.",
    details: "My first self-taught web project built with HTML, CSS, and JavaScript. This early portfolio helped me understand the basics of web page structure, layout design, and user interface flow. Although simple, it laid the foundation for my transition into more advanced front-end frameworks and interactive web development.",
    link: "https://github.com/JungeuiLee/personalWebsite.git",
    image: "/personalWebsite.png",
  },
];


export default function Projects() {
  const [selectedProject, setSelectedProject] = useState<null | typeof projects[0]>(null);

  return (
    <section id="projects" className="py-20 px-6 bg-black text-white relative">
      <h2 className="text-3xl font-bold mb-10 text-center">Projects</h2>

      <div className="flex flex-col gap-8 max-w-3xl mx-auto">
        {projects.map((proj, idx) => (
          <div
            key={idx}
            className="bg-zinc-800 p-6 rounded-lg shadow hover:shadow-lg cursor-pointer transition"
            onClick={() => setSelectedProject(proj)}
          >
            <h3 className="text-xl font-semibold mb-2">{proj.title}</h3>
            <p className="text-zinc-400 mb-4">{proj.description}</p>
            <span className="text-blue-400 hover:underline">Learn more →</span>
          </div>
        ))}
      </div>

      {selectedProject && (
        <div className="fixed inset-0 flex items-center justify-center bg-black/70 backdrop-blur-sm z-50">
          <div className="bg-zinc-900 p-8 rounded-xl shadow-lg max-w-lg mx-4 text-left relative">
            <button
              onClick={() => setSelectedProject(null)}
              className="absolute top-3 right-3 text-zinc-400 hover:text-white"
            >
              ✕
            </button>
            <h3 className="text-2xl font-bold mb-4">{selectedProject.title}</h3>

            {selectedProject.image && (
              <img
                src={selectedProject.image}
                alt={selectedProject.title}
                className="w-full h-auto max-h-[500px] object-contain rounded-md mb-6 border border-zinc-700"
              />
            )}

            <p className="text-zinc-300 mb-6">{selectedProject.details}</p>
            <a
              href={selectedProject.link}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-400 hover:underline"
            >
              View on GitHub →
            </a>
          </div>
        </div>
      )}
    </section>
  );
}