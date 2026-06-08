# OpenWRT Ecosystem Projects

Advanced networking and telemetry interception tools specifically designed for the OpenWRT embedded platform.

## Blackhole Webserver

!!! abstract "Go / OpenWRT Architecture"
    A highly efficient, single-binary Go webserver designed for OpenWRT routers (ARM64/AMD64). It executes catch-all routing to intercept telemetric traffic, mirrors requested directory structures onto a local storage device, and serves a 1x1 tracking pixel (or simulated connectivity checks).
    [GitHub Repository](https://github.com/IamRPDev/blackhole-server)

## LuCI App: Blackhole

!!! info "OpenWRT Web GUI Integration"
    A modern, client-side rendered OpenWRT Web GUI module (LuCI) for managing the Blackhole server. Built using the latest JS view models and RPCD access control lists, allowing native router administration without CLI overhead.
    [GitHub Repository](https://github.com/IamRPDev/luci-app-blackhole)

## OpenWRT Custom Feed

!!! tip "Automated Package Management"
    An automated package repository containing `.apk` and `.ipk` OpenWRT installer packages for the Blackhole ecosystem. Maintained entirely via GitHub Actions leveraging the OpenWRT SDK Docker containers for automated cross-compilation.
    [GitHub Repository](https://github.com/IamRPDev/openwrt-blackhole-feed)
