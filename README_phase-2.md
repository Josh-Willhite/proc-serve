## Synopsis

Expose subset of info available in **/proc** as json via Python Flask server.

## Example Usage

```
$ curl -sS localhost:1404/uptime
{
  "seconds_idle": "11204.45",
  "seconds_up": "11249.67"
}
$ curl -sS localhost:1404/cpuinfo
{
  "address sizes": "36 bits physical, 48 bits virtual",
  "apicid": "0",
  "bogomips": "5573.91",
  "cache size": "4096 KB",
  "cache_alignment": "64",
  "clflush size": "64",
  "core id": "0",
  "cpu MHz": "2786.957",
  "cpu cores": "1",
  "cpu family": "6",
  "cpuid level": "13",
  "flags": "fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc pni pclmulqdq monitor ssse3 cx16 sse4_1 sse4_2 popcnt aes xsave avx lahf_lm",
  "fpu": "yes",
  "fpu_exception": "yes",
  "initial apicid": "0",
  "model": "42",
  "model name": "Intel(R) Core(TM) i7-2640M CPU @ 2.80GHz",
  "physical id": "0",
  "power management": "",
  "processor": "0",
  "siblings": "1",
  "stepping": "7",
  "vendor_id": "GenuineIntel",
  "wp": "yes"
}
$ curl -sS localhost:1404/meminfo
{
  "Active": "241496 kB",
  "Active(anon)": "95072 kB",
  "Active(file)": "146424 kB",
  "AnonHugePages": "0 kB",
  "AnonPages": "94984 kB",
  "Bounce": "0 kB",
  "Buffers": "19828 kB",
  "Cached": "296016 kB",
  "CommitLimit": "250844 kB",
  "Committed_AS": "153992 kB",
  "DirectMap2M": "487424 kB",
  "DirectMap4k": "36800 kB",
  "Dirty": "0 kB",
  "HardwareCorrupted": "0 kB",
  "HugePages_Free": "0",
  "HugePages_Rsvd": "0",
  "HugePages_Surp": "0",
  "HugePages_Total": "0",
  "Hugepagesize": "2048 kB",
  "Inactive": "169312 kB",
  "Inactive(anon)": "564 kB",
  "Inactive(file)": "168748 kB",
  "KernelStack": "680 kB",
  "Mapped": "11080 kB",
  "MemFree": "39644 kB",
  "MemTotal": "501692 kB",
  "Mlocked": "0 kB",
  "NFS_Unstable": "0 kB",
  "PageTables": "2652 kB",
  "SReclaimable": "31452 kB",
  "SUnreclaim": "7868 kB",
  "Shmem": "672 kB",
  "Slab": "39320 kB",
  "SwapCached": "0 kB",
  "SwapFree": "0 kB",
  "SwapTotal": "0 kB",
  "Unevictable": "0 kB",
  "VmallocChunk": "34359712760 kB",
  "VmallocTotal": "34359738367 kB",
  "VmallocUsed": "19720 kB",
  "Writeback": "0 kB",
  "WritebackTmp": "0 kB"
}
$~
```

## Motivation

Provide simple interface to allow external monitoring of infrastructure.

## Installation

### Vagrant Python VirtualEnv (manual)
1. Setup virtualenv: ```$ virtualenv -p /usr/bin/python3 proc-serve-env```
2. Activate virtualenv: ```$ source proc-serve-env/bin/activate```
3. Clone repo: ```$ git clone https://github.com/Josh-Willhite/proc-serve.git```
4. Enter dir: ```$ cd proc-serve```
5. Install: ```$ python setup.py install```
6. Run:
```
$ python src/proc_serve.py &
$ curl localhost:1404/uptime
127.0.0.1 - - [26/Feb/2017 21:27:34] "GET /uptime HTTP/1.1" 200 -
{
  "seconds_idle": "2390.57", 
    "seconds_up": "2448.36"
}
```

### Vagrant Shell Provisioner

1. Spin up vagrant host and select NIC which you're currently using to access the net:
```
$ vagrant up
==> default: Available bridged network interfaces:
1) wlp3s0
2) enp0s25
==> default: When choosing an interface, it is usually the one that is
==> default: being used to connect to the internet.
    default: Which interface should the network bridge to?
...

==> default: Finished processing dependencies for proc-server==0.0.1
==> default: procserve start/running, process 4704
==> default: Service is listening on 192.168.11.129:1404
$ curl 192.168.11.129:1404/uptime
{
  "seconds_idle": "217.51",
    "seconds_up": "253.29"
}
```

## API Reference

- /cpuinfo (GET):
  - Returns contents of **/proc/cpuinfo** as json dict.
- /meminfo (GET):
  - Returns contents of **/proc/meminfo** as json dict.
- /uptime (GET):
  - Returns contents of **/proc/uptime** as json dict.


## Tests

Run tests as follows:
```
$ python3 -m pytest -v test_proc_serve.py
=============================== test session starts ================================
platform linux -- Python 3.5.2, pytest-3.0.6, py-1.4.32, pluggy-0.4.0 -- /usr/bin/python3
cachedir: ../.cache
rootdir: /home/josh/repos/proc-serve, inifile:
plugins: mock-1.5.0
collected 1 items

test_proc_serve.py::test_proc_to_dict PASSED

============================= 1 passed in 0.22 seconds =============================
$
```

## License

This software is offered under the MIT license. Anyone can freely use or modify it, see LICENSE.txt for details and restrictions.

