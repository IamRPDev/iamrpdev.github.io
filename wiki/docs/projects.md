# Projects

Recent developments focusing on self-sovereign telemetry interception and lightweight routing infrastructure.

!!! abstract "Blackhole Webserver"
    A highly efficient, single-binary Go webserver designed for OpenWRT routers (ARM64/AMD64). It executes catch-all routing to intercept telemetric traffic, mirrors requested directory structures onto a local storage device, and serves a 1x1 tracking pixel (or simulated connectivity checks).
    [GitHub Repository](https://github.com/IamRPDev/blackhole-server)

!!! info "LuCI App: Blackhole"
    A modern, client-side rendered OpenWRT Web GUI module (LuCI) for managing the Blackhole server. Built using the latest JS view models and RPCD access control lists, allowing native router administration without CLI overhead.
    [GitHub Repository](https://github.com/IamRPDev/luci-app-blackhole)

!!! tip "OpenWRT Custom Feed"
    An automated package repository containing `.apk` and `.ipk` OpenWRT installer packages for the Blackhole ecosystem. Maintained entirely via GitHub Actions leveraging the OpenWRT SDK Docker containers for automated cross-compilation.
    [GitHub Repository](https://github.com/IamRPDev/openwrt-blackhole-feed)
