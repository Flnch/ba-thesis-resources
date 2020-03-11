# Bachelor thesis resource overview
This repository contains an overview of the publicly available resources of my bachelor thesis, such as source code or results.

- Thesis title: Design and implementation of a stealthy OpenWPM web scraper
- Supervisor: Dr. Ir. Hugo Jonker
- University and program: Radboud University, NL, [computing science](https://www.ru.nl/english/education/bachelors/computing-science/)

## Source code
- [Stealth version of OpenWPM](https://github.com/Flnch/OpenWPM/tree/issue-448-webdriver_attr) (on the git branch `issue-448-webdriver_attr`*)
  - The main addition of the stealth version is spoofing a revealing JavaScript property. This spoofing functionality is also available as a [stand-alone Firefox extension](https://github.com/Flnch/stealth-extension).
- [OpenWPM measurement version](https://github.com/Flnch/OpenWPM/tree/measurement) (on the git branch `measurement`*)
- [webdriver testpage](https://github.com/Flnch/webdriver-testpage): A simple test page to test whether the original value of spoofed `window.navigator` objects can be revealed inside iframes.

\*: Note after changing the branch it is necessary to rebuild OpenWPM's instrumentation extension (run `build-extension.sh`) to resemble the code version of the changed branch.

## Results/data
- `results/BrowserBasedBotFP` contains the data captured with the BrowserBasedBotFP tool.  
  For easy inspection and comparisons, rename a database to `fpdb.db` and use BrowserBasedBotFP's analysis functionality.
  - `fpdb[measurement-chapter].db`: Data from the experiment in the measurement chapter
- `results/jstemplate` contains the data captured with the JavaScript template attack tool.  
  For easy inspection and comparisons, rename a measurement file to `data.json` and open it with the JavaScript template framework.
  - `data[measurement-chapter].json`: Data from the experiment in the measurement chapter
- `analysisOfHTTPHeader.pcapng` contains Wireshark captures of different browser and automation combinations to investigate the attribute order inside the HTTP packets.

## Used tools
- [BrowserBasedBotFP](https://github.com/bkrumnow/BrowserBasedBotFP): Framework to measure bot detection related fingerprinting properties ([corresponding paper](http://www.open.ou.nl/hjo/papers/ESORICS19.pdf))
- [JavaScript template attacks](https://github.com/IAIK/jstemplate): Framework to measure JavaScript differences betweeen browser environments ([corresponding paper](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_01B-4_Schwarz_paper.pdf))
- [BDScanner (fork)](https://github.com/Flnch/BDScanner): Framework using OpenWPM to analyze URLs for their bot detection activity ([corresponding paper](http://www.open.ou.nl/hjo/papers/ESORICS19.pdf))  
  (In my fork, the software dependencies are updated to the newest version)

`BrowserBasedBotFP` and `JavaScript template attacks` run on the same ports but that can be changed to run them at the same time.
