'use client';

import { useState } from 'react';

const navLinks = [
    { href: '#about', label: 'About' },
    { href: '#experience', label: 'Experience' },
    { href: '#projects', label: 'Projects' },
    { href: '#skills', label: 'Skills' },
    { href: '#contact', label: 'Contact' },
];

export default function Navbar() {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <nav className="fixed top-0 left-0 w-full bg-black text-white z-50 shadow-md">
            <div className="mx-auto flex max-w-5xl flex-col px-4 sm:px-8">
                <div className="flex h-16 items-center justify-end md:justify-center">
                    <button
                        type="button"
                        className="inline-flex h-10 w-10 items-center justify-center rounded-md text-sm font-medium transition hover:bg-zinc-900 focus:outline-none focus:ring-2 focus:ring-emerald-500 md:hidden"
                        onClick={() => setIsOpen((prev) => !prev)}
                        aria-controls="primary-navigation"
                        aria-expanded={isOpen}
                    >
                        <span className="sr-only">Toggle navigation</span>
                        {isOpen ? (
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                className="h-5 w-5"
                            >
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M18 6L6 18M6 6l12 12" />
                            </svg>
                        ) : (
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                className="h-5 w-5"
                            >
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                            </svg>
                        )}
                    </button>
                    <div
                        id="primary-navigation"
                        className="hidden items-center gap-8 md:flex"
                    >
                        {navLinks.map((link) => (
                            <a
                                key={link.href}
                                href={link.href}
                                className="transition hover:text-zinc-400"
                            >
                                {link.label}
                            </a>
                        ))}
                    </div>
                </div>
                <div
                    className={`overflow-hidden transition-[max-height,opacity] duration-300 ease-in-out md:hidden ${
                        isOpen ? 'max-h-96 opacity-100' : 'max-h-0 opacity-0'
                    }`}
                >
                    <div className="flex flex-col gap-4 border-t border-zinc-800 py-4">
                        {navLinks.map((link) => (
                            <a
                                key={link.href}
                                href={link.href}
                                className="text-sm font-medium transition hover:text-zinc-400"
                                onClick={() => setIsOpen(false)}
                            >
                                {link.label}
                            </a>
                        ))}
                    </div>
                </div>
            </div>
        </nav>
    );
}
