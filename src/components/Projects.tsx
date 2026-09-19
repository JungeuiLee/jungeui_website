import Image from "next/image";

type Project = {
  title: string;
  tech: string;
  description: string;
  image?: string;
  github?: string;
  appstore?: string;
  article?: string;
  demo?: string;
};

const projects: Project[] = [
  {
    title: "Bamboo: Campus Community",
    tech: "Flutter, Dart, Firebase (Firestore, Auth, Cloud Functions)",
    description:
      "A live iOS app on the App Store \u2014 an anonymous campus community for Korean international students in the U.S. Sign-up requires .edu email verification, so identities are verified while conversations stay anonymous. I lead engineering: the Firestore data model, the OTP email verification flow (built so that registered and unregistered addresses behave identically, preventing account enumeration), server-side notification delivery through Cloud Functions, and the security rules and composite indexes behind it. Currently expanding to additional campuses.",
    // image: "/bamboo.png",
    appstore: "https://apps.apple.com/us/app/bamboo-campus-community/id6799337020",
    github: "https://github.com/JungeuiLee/bamboo_architecture",
  },
  {
    title: "Course Scheduler (CSP)",
    tech: "Python, matplotlib",
    description:
      "Models university course scheduling as a Constraint Satisfaction Problem and compares three search strategies — plain backtracking, MRV + Degree heuristics, and MAC (AC-3) constraint propagation — across datasets of 6, 15, and 20 courses plus a deliberately unsolvable instance. MRV + Degree eliminated backtracking entirely (409 → 0) on the largest solvable case, while MAC proved unsatisfiability in a single backtrack versus 316 for plain backtracking.",
    image: "/courseSchedulerCSP.png",
    github: "https://github.com/JungeuiLee/course-scheduler-csp",
    article:
      "https://drive.google.com/file/d/16eIA5p-xOLwg4jLSJHJIepuIMavdFd1t/view?usp=sharing",
  },
  {
    title: "GPU Video Editor",
    tech: "C++, OpenGL, GLFW, FFmpeg, FreeType, GTest",
    description:
      "A desktop video editor built on a timeline model: multiple tracks hold image, video, text, and caption assets behind one unified interface, and the renderer composites them frame by frame with alpha blending. Export runs through FFmpeg (H.264/MP4, plus PNG/JPEG/BMP stills) behind a facade that hides the codec and color-space conversion. The filter system is a Strategy hierarchy \u2014 Gaussian blur, directional Sobel edge detection, threshold, greyscale, and mean blur \u2014 with CPU reference implementations verified by a GTest suite and equivalent GLSL shader paths for the interactive editor. Architecture leans on Adapter, Abstract Factory, Composite, Facade, Command, Observer, and MVC.",
    image: "/videoEditor.png",
    github: "https://github.com/JungeuiLee/GPU_Video_Editor",
  },
  {
    title: "GPU Image Editor",
    tech: "C++, OpenGL, GLSL",
    description:
      "A GPU-accelerated 2D image editor with a custom OpenGL rendering pipeline — draw and erase on images with configurable RGB colors, shader-based filters, and texture handling tuned for real-time rendering. Built around reusable classes (Application, Window, Image, Texture, ShaderProgram, Glyph, Quad) with explicit copy constructors, assignment operators, and destructors for manual memory management.",
    image: "/GPUImageEditor.png",
    github: "https://github.com/JungeuiLee/GPU_Image_Editor",
  },
  {
    title: "Jungeui Portfolio",
    tech: "Next.js, TypeScript, React, Tailwind CSS",
    description:
      "This site. Built with Next.js and TypeScript, focusing on type-safe reusable components, responsive layout, and a structure that stays easy to extend as new work gets added.",
    image: "/jungeuiPortfolio.png",
    github: "https://github.com/justice-1297-dev/jungeui_website",
    demo: "https://jungeui-website.vercel.app/",
  },
  // Temporarily hidden — early self-taught practice projects.
  // Uncomment to show them again.
  /*
  {
    title: "Online Store Clone",
    tech: "HTML, CSS, JavaScript",
    description:
      "A multi-page online fashion store clone built while self-teaching front-end fundamentals — product sections, category pages, and responsive layout using only HTML, CSS, and JavaScript.",
    image: "/RandomWalk.png",
    github: "https://github.com/JungeuiLee/randonWalk-clone",
  },
  {
    title: "First Portfolio",
    tech: "HTML, CSS, JavaScript",
    description:
      "My first self-taught web project. Covered page structure, layout design, and basic interaction, and set up the move into modern front-end frameworks.",
    image: "/personalWebsite.png",
    github: "https://github.com/JungeuiLee/personalWebsite",
  },
  */
];

export default function Projects() {
  return (
    <section id="projects" className="py-24 px-6 bg-black text-white">
      <h2 className="text-3xl font-bold mb-16 text-center">Projects</h2>

      <div className="flex flex-col gap-14 max-w-3xl mx-auto">
        {projects.map((proj) => (
          <article
            key={proj.title}
            className="bg-zinc-900 border border-zinc-800 rounded-xl p-8 hover:border-zinc-600 transition"
          >
            <h3 className="text-xl font-semibold">{proj.title}</h3>
            <p className="text-sm text-zinc-500 mt-2">{proj.tech}</p>

            {proj.image ? (
              <div className="relative w-full h-60 my-7 rounded-lg overflow-hidden bg-zinc-950 border border-zinc-800">
                <Image
                  src={proj.image}
                  alt={proj.title}
                  fill
                  sizes="(max-width: 768px) 100vw, 768px"
                  className="object-contain"
                />
              </div>
            ) : (
              <div className="mt-6" />
            )}

            <p className="text-zinc-400 leading-relaxed">{proj.description}</p>

            <div className="mt-7 flex flex-col gap-3">
              {proj.appstore && (
                <a
                  href={proj.appstore}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-400 hover:underline w-fit"
                >
                  App Store: Download the App →
                </a>
              )}
              {proj.github && (
                <a
                  href={proj.github}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-400 hover:underline w-fit"
                >
                  GitHub: Go to Repository →
                </a>
              )}
              {proj.article && (
                <a
                  href={proj.article}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-400 hover:underline w-fit"
                >
                  Article: Go to Google Drive →
                </a>
              )}
              {proj.demo && (
                <a
                  href={proj.demo}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-400 hover:underline w-fit"
                >
                  Live: Visit Site →
                </a>
              )}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
