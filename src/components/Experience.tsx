'use client'

import { useState } from 'react';
import { Briefcase, Rocket, FlaskConical, Wrench } from 'lucide-react';

type ExperienceItem = {
  id: string;
  company: string;
  role: string;
  date: string;
  badge: string;
  color: string;
  icon: React.ReactNode;
  description: string;
  website?: string;
  technologies: string[];
  achievements: string[];
};

const experiences: ExperienceItem[] = [
  {
    id: 'marine-corps',
    company: 'Republic of Korea Marine Corps',
    role: 'Tactical Communications Specialist',
    date: 'Aug 2023 – Feb 2025',
    badge: '18 months',
    color: '#2563eb',
    icon: <Briefcase size={24} />,
    description:
      'Supported mission-critical tactical communication systems in high-reliability field environments, coordinating with cross-functional units to maintain full interoperability.',
    technologies: ['TICN', 'Networking', 'Linux', 'Hardware Diagnostics'],
    achievements: [
      'Maintained mission-critical communication systems with >99% uptime in high-reliability environments',
      'Diagnosed and resolved hardware and system-level issues under time-sensitive field conditions',
      'Coordinated cross-functional operations with U.S. Marine Corps teams, ensuring full interoperability',
    ],
  },
  {
    id: 'boom-communications',
    company: 'Boom Communications',
    role: 'Software Engineer Intern',
    date: 'Mar 2025 – Aug 2025',
    badge: '6 months',
    color: '#2563eb',
    icon: <Briefcase size={24} />,
    description:
      'Maintained and extended a client-facing web interface for a media/communications company based in Daegu, South Korea.',
    technologies: ['JavaScript', 'Responsive Design', 'UI/UX', 'Web'],
    achievements: [
      'Improved layout consistency and mobile responsiveness across desktop and mobile browsers',
      'Iterated on UI changes based on feedback from engineers and designers',
      'Collaborated with engineers to support content delivery workflows and improve reliability of client deliverables',
    ],
  },
  {
    id: 'bamboo',
    company: 'Bamboo: Campus Community',
    role: 'Co-Founder & Head of Engineering',
    date: 'Jan 2026 – Present',
    badge: 'Ongoing',
    color: '#ea580c',
    icon: <Rocket size={24} />,
    description:
      'An anonymous, identity-verified campus community app for Korean international students in the U.S. — leading all engineering from the ground up.',
    technologies: ['Flutter', 'Dart', 'Firebase', 'Firestore', 'Cloud Functions', 'OTP Auth'],
    achievements: [
      "Architected the application's data model, authentication flow, and OTP-based email verification system",
      'Designed Firestore security rules and composite indexes to support a scalable, production-grade service',
      'Directed the technical roadmap across cloud infrastructure, notification systems, and Flutter/Dart client integration',
      'Grew the platform to 150+ registered users and 124+ downloads to date, with active outreach to additional campuses',
    ],
  },
  {
    id: 'ding-lab',
    company: "UMN APEX Lab",
    role: 'Undergraduate Research Assistant',
    date: 'May 2026 – Present',
    badge: 'Ongoing',
    color: '#0d9488',
    icon: <FlaskConical size={24} />,
    description:
      'Undergraduate researcher in the Algorithm-Platform Exploration for Efficient AI (APEX) Lab at the University of Minnesota, contributing to a circuit-domain foundation model project across ML systems and EDA.',
    technologies: ['CUDA', 'GPU Programming', 'PyTorch', 'Data Annotation'],
    achievements: [
      'Conducted data annotation for a circuit-domain foundation model project, correcting AI-generated descriptions of CAD, VLSI, and computer architecture figures/tables',
      'Performed GPU programming research reproducing FlashAttention (v1–v4) from first principles',
      'Implemented and validated CUDA kernels on a multi-GPU lab server (8x RTX 6000 Ada)',
      'Collaborated with a PhD student mentor through weekly research progress reviews',
    ],
  },
  {
    id: 'micro-lab-ta',
    company: 'Micro Lab TA',
    role: 'Undergraduate Teaching Assistant, University of Minnesota',
    date: 'Sep 2026 – Present',
    badge: 'Ongoing',
    color: '#475569',
    icon: <Wrench size={24} />,
    description:
      'Supports the Microlab facility at Smith Hall, University of Minnesota, keeping lab equipment and software environments running for students and researchers.',
    technologies: ['Hardware Maintenance', 'IT Support', 'Linux'],
    achievements: [
      'Maintain and troubleshoot lab equipment and software environments used by students and researchers',
      'Provide technical support and guidance to students on hardware setup, software configuration, and equipment usage',
      'Coordinate with lab management to manage inventory and uphold lab operational standards',
    ],
  },
];

function ExperienceCard({ exp }: { exp: ExperienceItem }) {
  const [selected, setSelected] = useState(false);

  return (
    <>
      <div
        onClick={() => setSelected(true)}
        className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 cursor-pointer hover:border-zinc-600 transition"
      >
        <div className="flex items-start justify-between gap-3 mb-2">
          <h3 className="font-semibold text-lg text-white">{exp.company}</h3>
          <span className="text-xs whitespace-nowrap px-3 py-1 rounded-full bg-zinc-800 text-zinc-300">
            {exp.badge}
          </span>
        </div>
        <p className="text-sm text-zinc-400">{exp.role}</p>
        <p className="text-xs text-zinc-500 mt-1">{exp.date}</p>
        <p className="text-sm text-zinc-400 mt-3">{exp.description}</p>
      </div>

      {selected && (
        <div
          className="fixed inset-0 flex items-center justify-center bg-black/70 backdrop-blur-sm z-50 px-4"
          onClick={() => setSelected(false)}
        >
          <div
            className="bg-zinc-900 p-8 rounded-xl shadow-lg max-w-lg w-full text-left relative max-h-[85vh] overflow-y-auto"
            onClick={(e) => e.stopPropagation()}
          >
            <button
              onClick={() => setSelected(false)}
              className="absolute top-3 right-3 text-zinc-400 hover:text-white"
            >
              ✕
            </button>

            <div className="mb-4">
              <h3 className="text-xl font-bold">{exp.company}</h3>
              <p className="text-zinc-300">{exp.role}</p>
              <p className="text-sm text-zinc-500">{exp.date}</p>
            </div>

            <p className="text-zinc-300 mb-4">{exp.description}</p>

            {exp.website && (
              <a
                href={exp.website}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-400 hover:underline block mb-6"
              >
                Go to Website →
              </a>
            )}

            <h4 className="text-sm font-semibold text-zinc-400 uppercase tracking-wide mb-2">
              Technologies Used
            </h4>
            <div className="flex flex-wrap gap-2 mb-6">
              {exp.technologies.map((tech) => (
                <span
                  key={tech}
                  className="px-3 py-1 rounded-full bg-zinc-700 text-sm text-zinc-200"
                >
                  {tech}
                </span>
              ))}
            </div>

            <h4 className="text-sm font-semibold text-zinc-400 uppercase tracking-wide mb-2">
              Key Achievements
            </h4>
            <ul className="list-disc list-inside space-y-1 text-zinc-300">
              {exp.achievements.map((point, idx) => (
                <li key={idx}>{point}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </>
  );
}

export default function Experience() {
  return (
    <section id="experience" className="py-20 px-4 bg-black text-white">
      <h2 className="text-3xl font-bold mb-16 text-center">Experience</h2>

      <div className="relative max-w-5xl mx-auto">
        {/* central line */}
        <div className="hidden md:block absolute left-1/2 -translate-x-1/2 top-0 bottom-0 w-px bg-zinc-700" />

        <div className="flex flex-col gap-12 md:gap-20">
          {experiences.map((exp, idx) => {
            const isLeft = idx % 2 === 0;
            return (
              <div key={exp.id} className="relative grid grid-cols-1 md:grid-cols-2 md:gap-16">
                {/* dot */}
                <div className="hidden md:block absolute left-1/2 top-8 -translate-x-1/2 w-3 h-3 rounded-full bg-white border-2 border-zinc-600 z-10" />

                {isLeft ? (
                  <>
                    <ExperienceCard exp={exp} />
                    <div />
                  </>
                ) : (
                  <>
                    <div />
                    <ExperienceCard exp={exp} />
                  </>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
