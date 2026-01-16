'use client'

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function Hero() {  
    const [mnTime, setMnTime] = useState("")
    const [seoulTime, setSeoulTime] = useState("")
    const router = useRouter();

    useEffect(()=> {
        const updateTime = () => {
            const now = new Date();
            const mnOptions: Intl.DateTimeFormatOptions = {
                timeZone: "America/Chicago",
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit",
                hour12: false,
            };
            const krOptions:Intl.DateTimeFormatOptions = {
                timeZone: "Asia/Seoul",
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit",
                hour12: false,
            };
        setMnTime(new Intl.DateTimeFormat("en-US", mnOptions).format(now));
        setSeoulTime(new Intl.DateTimeFormat("en-US", krOptions).format(now));
        };

        updateTime();
        const interval = setInterval(updateTime, 1000);
        return ()=> clearInterval(interval);
    }, []);




    return (
        <section className="min-h-screen flex flex-col justify-center items-center text-center px-4">
        <h1 className="text-4xl md:text-6xl font-bold mb-4">
        <a
            href="https://www.linkedin.com/in/jungeui-lee-49b264356/"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-blue-400 transition-colors duration-300"
        >
            Jungeui Lee
        </a>
        </h1>
        <p className="text-lg md:text-xl text-zinc-400 max-w-xl">
            Computer Science @ University of Minnesota - Twin Cities
        </p>
        <p className="text-lg md:text-xl text-zinc-400 max-w-3xl">
            CS undergraduate focused on backend systems and data workflows. — where design meets logic.
        </p>
        <div className="mb-4 flex flex-col sm:flex-row gap-4 text-sm text-zinc-400">
            <p className="italic cursor-pointer hover:text-blue-400 transition">
            {/* onClick={() => router.push('/usa')} */}
            🇺🇸 TIME IN MINNEAPOLIS - {mnTime}
            </p>
            <p className="italic cursor-pointer hover:text-blue-400 transition">
            {/* onClick={() => router.push('/korea')} */}
            🇰🇷 TIME IN SEOUL - {seoulTime}
            </p>
        </div>
        </section>
    );
}