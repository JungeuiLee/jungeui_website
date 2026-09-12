export default function About() {
  return (
    <section
      id="about"
      className="py-24 px-6 flex justify-center items-center bg-black text-white"
    >
      <div className="max-w-3xl text-center">
        <h2 className="text-3xl font-bold mb-8">About Me</h2>
        <p className="text-zinc-400 text-lg leading-relaxed">
          Computer Science undergraduate at the University of Minnesota – Twin Cities,
          working across GPU and ML systems research, full-stack engineering, and
          early-stage product development.
        </p>
        <p className="text-zinc-400 text-lg leading-relaxed mt-6">
          I&apos;m currently an undergraduate research assistant in a GPU and ML systems
          lab, contributing to a circuit-domain foundation model project. Alongside that I
          lead engineering for Bamboo, an anonymous campus community app now live on the
          App Store, where I own the data model, authentication, and cloud infrastructure
          end to end.
        </p>
        <p className="text-zinc-400 text-lg leading-relaxed mt-6">
          What connects them is an interest in systems-level performance attached to
          something people actually use — whether that means a GPU rendering pipeline, a
          filter running in a shader, or the backend behind a shipped app.
        </p>
      </div>
    </section>
  );
}
