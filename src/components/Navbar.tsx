'use client';

import Link from 'next/link';

export default function Navbar() {
    return (
        <nav className="fixed top-0 left-0 w-full bg-black text-white py-4 px-8 flex justify-end gap-8 z-50">
        <a href="#about" className="hover:text-zinc-400 transition">About</a>
        <a href="#experience" className="hover:text-zinc-400 transition">Experience</a>
        <a href="#projects" className="hover:text-zinc-400 transition">Projects</a>
        <a href="#contact" className="hover:text-zinc-400 transition">Contact</a>
        </nav>
    );
}