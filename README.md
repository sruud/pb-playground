# Pedalboard Playground

This is a small sandbox for exploring audio plugin testing and signal processing using [Spotify's Pedalboard](https://github.com/spotify/pedalboard), JUCE-based VSTs, and other audio libraries.

## Goals

- Experiment with plugin chains and signal transformation using Python
- Practice writing tests for audio effects
- Learn how to integrate Pedalboard with VSTs and analyze results

## Getting Started

### Requirements

[![Python](https://img.shields.io/badge/python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)

- macOS or Windows with audio support
- pluginval (optional for advanced VST validation)
- You can download pluginval from [their GitHub Releases page](https://github.com/Tracktion/pluginval/releases)

### Third-party Installation

###### _Chocolatey (Windows):_

```shell
> choco install pluginval
```

### Create and activate a virtual environment

**macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```powershell
python -m venv venv
.\venv\Scripts\activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```
