'use client'

import { useEffect, useState } from "react";

export default function Hero() {  
    const [mnTime, setMnTime] = useState("")
    const [seoulTime, setSeoulTime] = useState("")

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
        <h1 className="text-4xl md:text-6xl font-bold mb-4">Jungeui Lee</h1>
        <p className="text-lg md:text-xl text-zinc-400 max-w-xl">
            Computer Science @ University of Minnesota - Twin Cities
        </p>
        <p className="text-lg md:text-xl text-zinc-400 max-w-xl">
            A passionate Computer Science student building full-stack applications.
        </p>
        <div className="mb-4 flex flex-col sm:flex-row gap-4 text-sm text-zinc-400">
            <p className="italic">🇺🇸 TIME IN MINNEAPOLIS - {mnTime}</p>
            <p className="italic">🇰🇷 TIME IN SEOUL - {seoulTime}</p>
        </div>
        </section>
    );
}