'use client'

import {
  VerticalTimeline,
  VerticalTimelineElement,
} from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';

import { Briefcase, GraduationCap } from 'lucide-react';

export default function () {
    return (
        <section id="experience" className="py-20 px-4 bg-black text-white">
        <h2 className="text-3xl font-bold mb-10 text-center">Experience</h2>
        <VerticalTimeline lineColor="#888">
            <VerticalTimelineElement
            date="2021 – 2027"
            icon={<GraduationCap size={20} />}
            iconStyle={{ background: '#6b21a8', color: '#fff' }}
            contentStyle={{ background: '#0a0a0a', color: '#fff', border: '1px solid #333' }}
            >
            <h3 className="font-semibold text-lg">University of Minnesota</h3>
            <p className="text-sm text-zinc-400">Computer Science Major</p>
            </VerticalTimelineElement>

            <VerticalTimelineElement
            date="2023 - 2025"
            icon={<Briefcase size={20} />}
            iconStyle={{ background: '#2563eb', color: '#fff' }}
            contentStyle={{ background: '#0a0a0a', color: '#fff', border: '1px solid #333' }}
            >
            <h3 className="font-semibold text-lg">Republic of Korea Marine Corps</h3>
            <p className="text-sm text-zinc-400">
                Tactical Communications Specialist
            </p>
            </VerticalTimelineElement>

            <VerticalTimelineElement
            date="2025 - 2025"
            icon={<Briefcase size={20} />}
            iconStyle={{ background: '#2563eb', color: '#fff' }}
            contentStyle={{ background: '#0a0a0a', color: '#fff', border: '1px solid #333' }}
            >
            <h3 className="font-semibold text-lg">Boom Communications</h3>
            <p className="text-sm text-zinc-400">
                Software Engineer Intern
            </p>
            </VerticalTimelineElement>


        </VerticalTimeline>
        </section>
    );
}