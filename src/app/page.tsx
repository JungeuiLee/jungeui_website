import Hero from "@/components/Hero";
import About from "@/components/About";
import Experience from "@/components/Experience";
import Projects from "@/components/Projects";
import Skills from "@/components/Skills";
import Contact from "@/components/Contact";

export default function Home() {
  return (
    <main className="bg-black text-white font-sans">
      <Hero />
      <About />
      <Experience />
      <Projects />
      <Skills />
      <Contact />
    </main>
  );
}