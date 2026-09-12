const skillGroups = [
  {
    title: "Languages",
    items:
      "Python, C++, C, TypeScript, JavaScript, Java, SQL, Dart, GLSL, CUDA, OCaml",
  },
  {
    title: "Frameworks & Libraries",
    items:
      "React, Next.js, Flutter, FastAPI, Django, Express.js, Spring Boot, Tailwind CSS, PyTorch, OpenGL, FFmpeg, GLFW, FreeType, GTest",
  },
  {
    title: "Data & Infrastructure",
    items:
      "Firebase (Firestore, Auth, Cloud Functions), PostgreSQL, MySQL, MongoDB, AWS, GCP, Vercel",
  },
  {
    title: "Tools",
    items: "Git, GitHub Actions, Linux, Bash, CMake, GDB, Vite",
  },
];

export default function Skills() {
  return (
    <section id="skills" className="py-24 px-6 text-white bg-black">
      <h2 className="text-3xl font-bold text-center mb-14">Skills</h2>
      <div className="max-w-4xl mx-auto grid grid-cols-1 sm:grid-cols-2 gap-x-12 gap-y-10">
        {skillGroups.map((group) => (
          <div key={group.title}>
            <h3 className="text-lg font-semibold mb-3">{group.title}</h3>
            <p className="text-zinc-400 leading-relaxed">{group.items}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
