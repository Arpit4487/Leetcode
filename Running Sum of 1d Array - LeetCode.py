<!DOCTYPE html>
<!-- saved from url=(0054)https://leetcode.com/problems/running-sum-of-1d-array/ -->
<html lang="en" class="dark" style="color-scheme: dark;"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style>.ͼ1.cm-focused {outline: 1px dotted #212121;}
.ͼ1 {position: relative !important; box-sizing: border-box; display: flex !important; flex-direction: column;}
.ͼ1 .cm-scroller {display: flex !important; align-items: flex-start !important; font-family: monospace; line-height: 1.4; height: 100%; overflow-x: auto; position: relative; z-index: 0; overflow-anchor: none;}
.ͼ1 .cm-content[contenteditable=true] {-webkit-user-modify: read-write-plaintext-only;}
.ͼ1 .cm-content {margin: 0; flex-grow: 2; flex-shrink: 0; display: block; white-space: pre; word-wrap: normal; box-sizing: border-box; min-height: 100%; padding: 4px 0; outline: none;}
.ͼ1 .cm-lineWrapping {white-space: pre-wrap; white-space: break-spaces; word-break: break-word; overflow-wrap: anywhere; flex-shrink: 1;}
.ͼ2 .cm-content {caret-color: black;}
.ͼ3 .cm-content {caret-color: white;}
.ͼ1 .cm-line {display: block; padding: 0 2px 0 6px;}
.ͼ1 .cm-layer > * {position: absolute;}
.ͼ1 .cm-layer {position: absolute; left: 0; top: 0; contain: size style;}
.ͼ2 .cm-selectionBackground {background: #d9d9d9;}
.ͼ3 .cm-selectionBackground {background: #222;}
.ͼ2.cm-focused > .cm-scroller > .cm-selectionLayer .cm-selectionBackground {background: #d7d4f0;}
.ͼ3.cm-focused > .cm-scroller > .cm-selectionLayer .cm-selectionBackground {background: #233;}
.ͼ1 .cm-cursorLayer {pointer-events: none;}
.ͼ1.cm-focused > .cm-scroller > .cm-cursorLayer {animation: steps(1) cm-blink 1.2s infinite;}
@keyframes cm-blink {50% {opacity: 0;}}
@keyframes cm-blink2 {50% {opacity: 0;}}
.ͼ1 .cm-cursor, .ͼ1 .cm-dropCursor {border-left: 1.2px solid black; margin-left: -0.6px; pointer-events: none;}
.ͼ1 .cm-cursor {display: none;}
.ͼ3 .cm-cursor {border-left-color: #444;}
.ͼ1 .cm-dropCursor {position: absolute;}
.ͼ1.cm-focused > .cm-scroller > .cm-cursorLayer .cm-cursor {display: block;}
.ͼ1 .cm-iso {unicode-bidi: isolate;}
.ͼ1 .cm-announced {position: fixed; top: -10000px;}
@media print {.ͼ1 .cm-announced {display: none;}}
.ͼ2 .cm-activeLine {background-color: #cceeff44;}
.ͼ3 .cm-activeLine {background-color: #99eeff33;}
.ͼ2 .cm-specialChar {color: red;}
.ͼ3 .cm-specialChar {color: #f78;}
.ͼ1 .cm-gutters {flex-shrink: 0; display: flex; height: 100%; box-sizing: border-box; inset-inline-start: 0; z-index: 200;}
.ͼ2 .cm-gutters {background-color: #f5f5f5; color: #6c6c6c; border-right: 1px solid #ddd;}
.ͼ3 .cm-gutters {background-color: #333338; color: #ccc;}
.ͼ1 .cm-gutter {display: flex !important; flex-direction: column; flex-shrink: 0; box-sizing: border-box; min-height: 100%; overflow: hidden;}
.ͼ1 .cm-gutterElement {box-sizing: border-box;}
.ͼ1 .cm-lineNumbers .cm-gutterElement {padding: 0 3px 0 5px; min-width: 20px; text-align: right; white-space: nowrap;}
.ͼ2 .cm-activeLineGutter {background-color: #e2f2ff;}
.ͼ3 .cm-activeLineGutter {background-color: #222227;}
.ͼ1 .cm-panels {box-sizing: border-box; position: sticky; left: 0; right: 0; z-index: 300;}
.ͼ2 .cm-panels {background-color: #f5f5f5; color: black;}
.ͼ2 .cm-panels-top {border-bottom: 1px solid #ddd;}
.ͼ2 .cm-panels-bottom {border-top: 1px solid #ddd;}
.ͼ3 .cm-panels {background-color: #333338; color: white;}
.ͼ1 .cm-tab {display: inline-block; overflow: hidden; vertical-align: bottom;}
.ͼ1 .cm-widgetBuffer {vertical-align: text-top; height: 1em; width: 0; display: inline;}
.ͼ1 .cm-placeholder {color: #888; display: inline-block; vertical-align: top;}
.ͼ1 .cm-highlightSpace:before {content: attr(data-display); position: absolute; pointer-events: none; color: #888;}
.ͼ1 .cm-highlightTab {background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="200" height="20"><path stroke="%23888" stroke-width="1" fill="none" d="M1 10H196L190 5M190 15L196 10M197 4L197 16"/></svg>'); background-size: auto 100%; background-position: right 90%; background-repeat: no-repeat;}
.ͼ1 .cm-trailingSpace {background-color: #ff332255;}
.ͼ1 .cm-button {vertical-align: middle; color: inherit; font-size: 70%; padding: .2em 1em; border-radius: 1px;}
.ͼ2 .cm-button:active {background-image: linear-gradient(#b4b4b4, #d0d3d6);}
.ͼ2 .cm-button {background-image: linear-gradient(#eff1f5, #d9d9df); border: 1px solid #888;}
.ͼ3 .cm-button:active {background-image: linear-gradient(#111, #333);}
.ͼ3 .cm-button {background-image: linear-gradient(#393939, #111); border: 1px solid #888;}
.ͼ1 .cm-textfield {vertical-align: middle; color: inherit; font-size: 70%; border: 1px solid silver; padding: .2em .5em;}
.ͼ2 .cm-textfield {background-color: white;}
.ͼ3 .cm-textfield {border: 1px solid #555; background-color: inherit;}
.ͼ2 {--indent-marker-bg-color: #d3d3d3; --indent-marker-active-bg-color: #939393;}
.ͼ3 {--indent-marker-bg-color: #404040; --indent-marker-active-bg-color: #707070;}
.ͼ1 .cm-line {position: relative;}
.ͼ1 .cm-indent-markers::before {content: ""; position: absolute; top: 0; left: 2px; right: 0; bottom: 0; background: var(--indent-markers); pointer-events: none; z-index: -1;}
.ͼ2 {--indent-marker-bg-color: #d3d3d3; --indent-marker-active-bg-color: #939393;}
.ͼ3 {--indent-marker-bg-color: #404040; --indent-marker-active-bg-color: #707070;}
.ͼ1 .cm-line {position: relative;}
.ͼ1 .cm-indent-markers::before {content: ""; position: absolute; top: 0; left: 2px; right: 0; bottom: 0; background: var(--indent-markers); pointer-events: none; z-index: -1;}
.ͼ2 {--indent-marker-bg-color: #d3d3d3; --indent-marker-active-bg-color: #939393;}
.ͼ3 {--indent-marker-bg-color: #404040; --indent-marker-active-bg-color: #707070;}
.ͼ1 .cm-line {position: relative;}
.ͼ1 .cm-indent-markers::before {content: ""; position: absolute; top: 0; left: 2px; right: 0; bottom: 0; background: var(--indent-markers); pointer-events: none; z-index: -1;}
.ͼ2 {--indent-marker-bg-color: #d3d3d3; --indent-marker-active-bg-color: #939393;}
.ͼ3 {--indent-marker-bg-color: #404040; --indent-marker-active-bg-color: #707070;}
.ͼ1 .cm-line {position: relative;}
.ͼ1 .cm-indent-markers::before {content: ""; position: absolute; top: 0; left: 2px; right: 0; bottom: 0; background: var(--indent-markers); pointer-events: none; z-index: -1;}
.ͼ2 {--indent-marker-bg-color: #d3d3d3; --indent-marker-active-bg-color: #939393;}
.ͼ3 {--indent-marker-bg-color: #404040; --indent-marker-active-bg-color: #707070;}
.ͼ1 .cm-line {position: relative;}
.ͼ1 .cm-indent-markers::before {content: ""; position: absolute; top: 0; left: 2px; right: 0; bottom: 0; background: var(--indent-markers); pointer-events: none; z-index: -1;}
.ͼ2 {--indent-marker-bg-color: #d3d3d3; --indent-marker-active-bg-color: #939393;}
.ͼ3 {--indent-marker-bg-color: #404040; --indent-marker-active-bg-color: #707070;}
.ͼ1 .cm-line {position: relative;}
.ͼ1 .cm-indent-markers::before {content: ""; position: absolute; top: 0; left: 2px; right: 0; bottom: 0; background: var(--indent-markers); pointer-events: none; z-index: -1;}
.ͼ2 {--indent-marker-bg-color: #d3d3d3; --indent-marker-active-bg-color: #939393;}
.ͼ3 {--indent-marker-bg-color: #404040; --indent-marker-active-bg-color: #707070;}
.ͼ1 .cm-line {position: relative;}
.ͼ1 .cm-indent-markers::before {content: ""; position: absolute; top: 0; left: 2px; right: 0; bottom: 0; background: var(--indent-markers); pointer-events: none; z-index: -1;}
.ͼ2 {--indent-marker-bg-color: #d3d3d3; --indent-marker-active-bg-color: #939393;}
.ͼ3 {--indent-marker-bg-color: #404040; --indent-marker-active-bg-color: #707070;}
.ͼ1 .cm-line {position: relative;}
.ͼ1 .cm-indent-markers::before {content: ""; position: absolute; top: 0; left: 2px; right: 0; bottom: 0; background: var(--indent-markers); pointer-events: none; z-index: -1;}
.ͼ2 {--indent-marker-bg-color: #d3d3d3; --indent-marker-active-bg-color: #939393;}
.ͼ3 {--indent-marker-bg-color: #404040; --indent-marker-active-bg-color: #707070;}
.ͼ1 .cm-line {position: relative;}
.ͼ1 .cm-indent-markers::before {content: ""; position: absolute; top: 0; left: 2px; right: 0; bottom: 0; background: var(--indent-markers); pointer-events: none; z-index: -1;}
.ͼ1 .cm-selectionMatch {background-color: #99ff7780;}
.ͼ1 .cm-searchMatch .cm-selectionMatch {background-color: transparent;}
.ͼ1 .cm-foldPlaceholder {background-color: #eee; border: 1px solid #ddd; color: #888; border-radius: .2em; margin: 0 1px; padding: 0 1px; cursor: pointer;}
.ͼ1 .cm-foldGutter span {padding: 0 1px; cursor: pointer;}
.ͼ79 {color: #569cd6;}
.ͼ7a {color: #c586c0;}
.ͼ7b {color: #9cdcfe;}
.ͼ7c {font-weight: bold; color: #9cdcfe;}
.ͼ7d {color: #4ec9b0;}
.ͼ7e {color: #dcdcaa;}
.ͼ7f {color: #b5cea8;}
.ͼ7g {color: #d4d4d4;}
.ͼ7h {color: #d16969;}
.ͼ7i {color: #ce9178;}
.ͼ7j {color: #808080;}
.ͼ7k {font-weight: bold;}
.ͼ7l {font-style: italic;}
.ͼ7m {text-decoration: line-through;}
.ͼ7n {color: #6a9955;}
.ͼ7o {color: #6a9955; text-decoration: underline;}
.ͼ7p {color: #ff0000;}
.ͼ78 .cm-gutters {background-color: #262626; color: #838383;}
.ͼ78 {background-color: transparent; color: #d4d4d4;}
.ͼ78.cm-editor .cm-scroller {font-family: Menlo, Monaco, Consolas, "Andale Mono", "Ubuntu Mono", "Courier New", monospace;}
.ͼ78 .cm-content {caret-color: #c6c6c6;}
.ͼ78 .cm-cursor, .ͼ78 .cm-dropCursor {border-left-color: #c6c6c6;}
.ͼ78 .cm-activeLine {background-color: #ffffff0f;}
.ͼ78 .cm-activeLineGutter {color: #fff; background-color: #ffffff0f;}
.ͼ78.cm-focused .cm-selectionBackground, .ͼ78 .cm-line::selection, .ͼ78 .cm-selectionLayer .cm-selectionBackground, .ͼ78 .cm-content ::selection {background: #6199ff2f !important;}
.ͼ78 .cm-selectionMatch {background-color: #72a1ff59;}
.ͼ6q {color: #569cd6;}
.ͼ6r {color: #c586c0;}
.ͼ6s {color: #9cdcfe;}
.ͼ6t {font-weight: bold; color: #9cdcfe;}
.ͼ6u {color: #4ec9b0;}
.ͼ6v {color: #dcdcaa;}
.ͼ6w {color: #b5cea8;}
.ͼ6x {color: #d4d4d4;}
.ͼ6y {color: #d16969;}
.ͼ6z {color: #ce9178;}
.ͼ70 {color: #808080;}
.ͼ71 {font-weight: bold;}
.ͼ72 {font-style: italic;}
.ͼ73 {text-decoration: line-through;}
.ͼ74 {color: #6a9955;}
.ͼ75 {color: #6a9955; text-decoration: underline;}
.ͼ76 {color: #ff0000;}
.ͼ6p .cm-gutters {background-color: #262626; color: #838383;}
.ͼ6p {background-color: transparent; color: #d4d4d4;}
.ͼ6p.cm-editor .cm-scroller {font-family: Menlo, Monaco, Consolas, "Andale Mono", "Ubuntu Mono", "Courier New", monospace;}
.ͼ6p .cm-content {caret-color: #c6c6c6;}
.ͼ6p .cm-cursor, .ͼ6p .cm-dropCursor {border-left-color: #c6c6c6;}
.ͼ6p .cm-activeLine {background-color: #ffffff0f;}
.ͼ6p .cm-activeLineGutter {color: #fff; background-color: #ffffff0f;}
.ͼ6p.cm-focused .cm-selectionBackground, .ͼ6p .cm-line::selection, .ͼ6p .cm-selectionLayer .cm-selectionBackground, .ͼ6p .cm-content ::selection {background: #6199ff2f !important;}
.ͼ6p .cm-selectionMatch {background-color: #72a1ff59;}
.ͼ67 {color: #569cd6;}
.ͼ68 {color: #c586c0;}
.ͼ69 {color: #9cdcfe;}
.ͼ6a {font-weight: bold; color: #9cdcfe;}
.ͼ6b {color: #4ec9b0;}
.ͼ6c {color: #dcdcaa;}
.ͼ6d {color: #b5cea8;}
.ͼ6e {color: #d4d4d4;}
.ͼ6f {color: #d16969;}
.ͼ6g {color: #ce9178;}
.ͼ6h {color: #808080;}
.ͼ6i {font-weight: bold;}
.ͼ6j {font-style: italic;}
.ͼ6k {text-decoration: line-through;}
.ͼ6l {color: #6a9955;}
.ͼ6m {color: #6a9955; text-decoration: underline;}
.ͼ6n {color: #ff0000;}
.ͼ66 .cm-gutters {background-color: #262626; color: #838383;}
.ͼ66 {background-color: transparent; color: #d4d4d4;}
.ͼ66.cm-editor .cm-scroller {font-family: Menlo, Monaco, Consolas, "Andale Mono", "Ubuntu Mono", "Courier New", monospace;}
.ͼ66 .cm-content {caret-color: #c6c6c6;}
.ͼ66 .cm-cursor, .ͼ66 .cm-dropCursor {border-left-color: #c6c6c6;}
.ͼ66 .cm-activeLine {background-color: #ffffff0f;}
.ͼ66 .cm-activeLineGutter {color: #fff; background-color: #ffffff0f;}
.ͼ66.cm-focused .cm-selectionBackground, .ͼ66 .cm-line::selection, .ͼ66 .cm-selectionLayer .cm-selectionBackground, .ͼ66 .cm-content ::selection {background: #6199ff2f !important;}
.ͼ66 .cm-selectionMatch {background-color: #72a1ff59;}
.ͼ5o {color: #569cd6;}
.ͼ5p {color: #c586c0;}
.ͼ5q {color: #9cdcfe;}
.ͼ5r {font-weight: bold; color: #9cdcfe;}
.ͼ5s {color: #4ec9b0;}
.ͼ5t {color: #dcdcaa;}
.ͼ5u {color: #b5cea8;}
.ͼ5v {color: #d4d4d4;}
.ͼ5w {color: #d16969;}
.ͼ5x {color: #ce9178;}
.ͼ5y {color: #808080;}
.ͼ5z {font-weight: bold;}
.ͼ60 {font-style: italic;}
.ͼ61 {text-decoration: line-through;}
.ͼ62 {color: #6a9955;}
.ͼ63 {color: #6a9955; text-decoration: underline;}
.ͼ64 {color: #ff0000;}
.ͼ5n .cm-gutters {background-color: #262626; color: #838383;}
.ͼ5n {background-color: transparent; color: #d4d4d4;}
.ͼ5n.cm-editor .cm-scroller {font-family: Menlo, Monaco, Consolas, "Andale Mono", "Ubuntu Mono", "Courier New", monospace;}
.ͼ5n .cm-content {caret-color: #c6c6c6;}
.ͼ5n .cm-cursor, .ͼ5n .cm-dropCursor {border-left-color: #c6c6c6;}
.ͼ5n .cm-activeLine {background-color: #ffffff0f;}
.ͼ5n .cm-activeLineGutter {color: #fff; background-color: #ffffff0f;}
.ͼ5n.cm-focused .cm-selectionBackground, .ͼ5n .cm-line::selection, .ͼ5n .cm-selectionLayer .cm-selectionBackground, .ͼ5n .cm-content ::selection {background: #6199ff2f !important;}
.ͼ5n .cm-selectionMatch {background-color: #72a1ff59;}
.ͼ4l {color: #569cd6;}
.ͼ4m {color: #c586c0;}
.ͼ4n {color: #9cdcfe;}
.ͼ4o {font-weight: bold; color: #9cdcfe;}
.ͼ4p {color: #4ec9b0;}
.ͼ4q {color: #dcdcaa;}
.ͼ4r {color: #b5cea8;}
.ͼ4s {color: #d4d4d4;}
.ͼ4t {color: #d16969;}
.ͼ4u {color: #ce9178;}
.ͼ4v {color: #808080;}
.ͼ4w {font-weight: bold;}
.ͼ4x {font-style: italic;}
.ͼ4y {text-decoration: line-through;}
.ͼ4z {color: #6a9955;}
.ͼ50 {color: #6a9955; text-decoration: underline;}
.ͼ51 {color: #ff0000;}
.ͼ4k .cm-gutters {background-color: #262626; color: #838383;}
.ͼ4k {background-color: transparent; color: #d4d4d4;}
.ͼ4k.cm-editor .cm-scroller {font-family: Menlo, Monaco, Consolas, "Andale Mono", "Ubuntu Mono", "Courier New", monospace;}
.ͼ4k .cm-content {caret-color: #c6c6c6;}
.ͼ4k .cm-cursor, .ͼ4k .cm-dropCursor {border-left-color: #c6c6c6;}
.ͼ4k .cm-activeLine {background-color: #ffffff0f;}
.ͼ4k .cm-activeLineGutter {color: #fff; background-color: #ffffff0f;}
.ͼ4k.cm-focused .cm-selectionBackground, .ͼ4k .cm-line::selection, .ͼ4k .cm-selectionLayer .cm-selectionBackground, .ͼ4k .cm-content ::selection {background: #6199ff2f !important;}
.ͼ4k .cm-selectionMatch {background-color: #72a1ff59;}
.ͼ42 {color: #569cd6;}
.ͼ43 {color: #c586c0;}
.ͼ44 {color: #9cdcfe;}
.ͼ45 {font-weight: bold; color: #9cdcfe;}
.ͼ46 {color: #4ec9b0;}
.ͼ47 {color: #dcdcaa;}
.ͼ48 {color: #b5cea8;}
.ͼ49 {color: #d4d4d4;}
.ͼ4a {color: #d16969;}
.ͼ4b {color: #ce9178;}
.ͼ4c {color: #808080;}
.ͼ4d {font-weight: bold;}
.ͼ4e {font-style: italic;}
.ͼ4f {text-decoration: line-through;}
.ͼ4g {color: #6a9955;}
.ͼ4h {color: #6a9955; text-decoration: underline;}
.ͼ4i {color: #ff0000;}
.ͼ41 .cm-gutters {background-color: #262626; color: #838383;}
.ͼ41 {background-color: transparent; color: #d4d4d4;}
.ͼ41.cm-editor .cm-scroller {font-family: Menlo, Monaco, Consolas, "Andale Mono", "Ubuntu Mono", "Courier New", monospace;}
.ͼ41 .cm-content {caret-color: #c6c6c6;}
.ͼ41 .cm-cursor, .ͼ41 .cm-dropCursor {border-left-color: #c6c6c6;}
.ͼ41 .cm-activeLine {background-color: #ffffff0f;}
.ͼ41 .cm-activeLineGutter {color: #fff; background-color: #ffffff0f;}
.ͼ41.cm-focused .cm-selectionBackground, .ͼ41 .cm-line::selection, .ͼ41 .cm-selectionLayer .cm-selectionBackground, .ͼ41 .cm-content ::selection {background: #6199ff2f !important;}
.ͼ41 .cm-selectionMatch {background-color: #72a1ff59;}
.ͼ3j {color: #569cd6;}
.ͼ3k {color: #c586c0;}
.ͼ3l {color: #9cdcfe;}
.ͼ3m {font-weight: bold; color: #9cdcfe;}
.ͼ3n {color: #4ec9b0;}
.ͼ3o {color: #dcdcaa;}
.ͼ3p {color: #b5cea8;}
.ͼ3q {color: #d4d4d4;}
.ͼ3r {color: #d16969;}
.ͼ3s {color: #ce9178;}
.ͼ3t {color: #808080;}
.ͼ3u {font-weight: bold;}
.ͼ3v {font-style: italic;}
.ͼ3w {text-decoration: line-through;}
.ͼ3x {color: #6a9955;}
.ͼ3y {color: #6a9955; text-decoration: underline;}
.ͼ3z {color: #ff0000;}
.ͼ3i .cm-gutters {background-color: #262626; color: #838383;}
.ͼ3i {background-color: transparent; color: #d4d4d4;}
.ͼ3i.cm-editor .cm-scroller {font-family: Menlo, Monaco, Consolas, "Andale Mono", "Ubuntu Mono", "Courier New", monospace;}
.ͼ3i .cm-content {caret-color: #c6c6c6;}
.ͼ3i .cm-cursor, .ͼ3i .cm-dropCursor {border-left-color: #c6c6c6;}
.ͼ3i .cm-activeLine {background-color: #ffffff0f;}
.ͼ3i .cm-activeLineGutter {color: #fff; background-color: #ffffff0f;}
.ͼ3i.cm-focused .cm-selectionBackground, .ͼ3i .cm-line::selection, .ͼ3i .cm-selectionLayer .cm-selectionBackground, .ͼ3i .cm-content ::selection {background: #6199ff2f !important;}
.ͼ3i .cm-selectionMatch {background-color: #72a1ff59;}
.ͼ30 {color: #569cd6;}
.ͼ31 {color: #c586c0;}
.ͼ32 {color: #9cdcfe;}
.ͼ33 {font-weight: bold; color: #9cdcfe;}
.ͼ34 {color: #4ec9b0;}
.ͼ35 {color: #dcdcaa;}
.ͼ36 {color: #b5cea8;}
.ͼ37 {color: #d4d4d4;}
.ͼ38 {color: #d16969;}
.ͼ39 {color: #ce9178;}
.ͼ3a {color: #808080;}
.ͼ3b {font-weight: bold;}
.ͼ3c {font-style: italic;}
.ͼ3d {text-decoration: line-through;}
.ͼ3e {color: #6a9955;}
.ͼ3f {color: #6a9955; text-decoration: underline;}
.ͼ3g {color: #ff0000;}
.ͼ2z .cm-gutters {background-color: #262626; color: #838383;}
.ͼ2z {background-color: transparent; color: #d4d4d4;}
.ͼ2z.cm-editor .cm-scroller {font-family: Menlo, Monaco, Consolas, "Andale Mono", "Ubuntu Mono", "Courier New", monospace;}
.ͼ2z .cm-content {caret-color: #c6c6c6;}
.ͼ2z .cm-cursor, .ͼ2z .cm-dropCursor {border-left-color: #c6c6c6;}
.ͼ2z .cm-activeLine {background-color: #ffffff0f;}
.ͼ2z .cm-activeLineGutter {color: #fff; background-color: #ffffff0f;}
.ͼ2z.cm-focused .cm-selectionBackground, .ͼ2z .cm-line::selection, .ͼ2z .cm-selectionLayer .cm-selectionBackground, .ͼ2z .cm-content ::selection {background: #6199ff2f !important;}
.ͼ2z .cm-selectionMatch {background-color: #72a1ff59;}
.ͼ2a {color: #569cd6;}
.ͼ2b {color: #c586c0;}
.ͼ2c {color: #9cdcfe;}
.ͼ2d {font-weight: bold; color: #9cdcfe;}
.ͼ2e {color: #4ec9b0;}
.ͼ2f {color: #dcdcaa;}
.ͼ2g {color: #b5cea8;}
.ͼ2h {color: #d4d4d4;}
.ͼ2i {color: #d16969;}
.ͼ2j {color: #ce9178;}
.ͼ2k {color: #808080;}
.ͼ2l {font-weight: bold;}
.ͼ2m {font-style: italic;}
.ͼ2n {text-decoration: line-through;}
.ͼ2o {color: #6a9955;}
.ͼ2p {color: #6a9955; text-decoration: underline;}
.ͼ2q {color: #ff0000;}
.ͼ29 .cm-gutters {background-color: #262626; color: #838383;}
.ͼ29 {background-color: transparent; color: #d4d4d4;}
.ͼ29.cm-editor .cm-scroller {font-family: Menlo, Monaco, Consolas, "Andale Mono", "Ubuntu Mono", "Courier New", monospace;}
.ͼ29 .cm-content {caret-color: #c6c6c6;}
.ͼ29 .cm-cursor, .ͼ29 .cm-dropCursor {border-left-color: #c6c6c6;}
.ͼ29 .cm-activeLine {background-color: #ffffff0f;}
.ͼ29 .cm-activeLineGutter {color: #fff; background-color: #ffffff0f;}
.ͼ29.cm-focused .cm-selectionBackground, .ͼ29 .cm-line::selection, .ͼ29 .cm-selectionLayer .cm-selectionBackground, .ͼ29 .cm-content ::selection {background: #6199ff2f !important;}
.ͼ29 .cm-selectionMatch {background-color: #72a1ff59;}
.ͼ5 {color: #404740;}
.ͼ6 {text-decoration: underline;}
.ͼ7 {text-decoration: underline; font-weight: bold;}
.ͼ8 {font-style: italic;}
.ͼ9 {font-weight: bold;}
.ͼa {text-decoration: line-through;}
.ͼb {color: #708;}
.ͼc {color: #219;}
.ͼd {color: #164;}
.ͼe {color: #a11;}
.ͼf {color: #e40;}
.ͼg {color: #00f;}
.ͼh {color: #30a;}
.ͼi {color: #085;}
.ͼj {color: #167;}
.ͼk {color: #256;}
.ͼl {color: #00c;}
.ͼm {color: #940;}
.ͼn {color: #f00;}
.ͼ8a {height: auto;}
.ͼ8a .cm-scroller {height: 100% !important;}
.ͼ89 {height: auto;}
.ͼ89 .cm-scroller {height: 100% !important;}
.ͼ88 {height: auto;}
.ͼ88 .cm-scroller {height: 100% !important;}
.ͼ87 {height: auto;}
.ͼ87 .cm-scroller {height: 100% !important;}
.ͼ7y {height: auto;}
.ͼ7y .cm-scroller {height: 100% !important;}
.ͼ7x {height: auto;}
.ͼ7x .cm-scroller {height: 100% !important;}
.ͼ7w {height: auto;}
.ͼ7w .cm-scroller {height: 100% !important;}
.ͼ7v {height: auto;}
.ͼ7v .cm-scroller {height: 100% !important;}
.ͼ5m {height: auto;}
.ͼ5m .cm-scroller {height: 100% !important;}
.ͼ5l {height: auto;}
.ͼ5l .cm-scroller {height: 100% !important;}
.ͼ5k {height: auto;}
.ͼ5k .cm-scroller {height: 100% !important;}
.ͼ5j {height: auto;}
.ͼ5j .cm-scroller {height: 100% !important;}
.ͼ5a {height: auto;}
.ͼ5a .cm-scroller {height: 100% !important;}
.ͼ59 {height: auto;}
.ͼ59 .cm-scroller {height: 100% !important;}
.ͼ58 {height: auto;}
.ͼ58 .cm-scroller {height: 100% !important;}
.ͼ57 {height: auto;}
.ͼ57 .cm-scroller {height: 100% !important;}
.ͼ2y {height: auto;}
.ͼ2y .cm-scroller {height: 100% !important;}
.ͼ2x {height: auto;}
.ͼ2x .cm-scroller {height: 100% !important;}
.ͼ2w {height: auto;}
.ͼ2w .cm-scroller {height: 100% !important;}
.ͼ2v {height: auto;}
.ͼ2v .cm-scroller {height: 100% !important;}
.ͼ2t {height: auto;}
.ͼ2t .cm-scroller {height: 100% !important;}
.ͼ4 .cm-line ::selection, .ͼ4 .cm-line::selection {background-color: transparent !important;}
.ͼ4 .cm-line {caret-color: transparent !important;}
.ͼ4 .cm-content :focus::selection, .ͼ4 .cm-content :focus ::selection {background-color: Highlight !important;}
.ͼ4 .cm-content :focus {caret-color: initial !important;}
.ͼ4 .cm-content {caret-color: transparent !important;}
</style><meta name="viewport" content="width=device-width"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@LeetCode"><meta property="og:image" content="https://leetcode.com/static/images/LeetCode_Sharing.png"><meta property="og:locale" content="en_US"><meta property="og:site_name" content="LeetCode"><title>Running Sum of 1d Array - LeetCode</title><meta name="robots" content="index,follow"><meta property="og:url" content="https://leetcode.com/problems/running-sum-of-1d-array/description"><meta property="og:title" content="Running Sum of 1d Array - LeetCode"><meta name="description" content="Can you solve this real interview question? Running Sum of 1d Array - Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:


Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:


Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:


Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


 

Constraints:

 * 1 &lt;= nums.length &lt;= 1000
 * -10^6 &lt;= nums[i] &lt;= 10^6"><meta property="og:description" content="Can you solve this real interview question? Running Sum of 1d Array - Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:


Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:


Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:


Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


 

Constraints:

 * 1 &lt;= nums.length &lt;= 1000
 * -10^6 &lt;= nums[i] &lt;= 10^6"><meta name="next-head-count" content="13"><script type="text/javascript" async="" src="./Running Sum of 1d Array - LeetCode_files/js"></script><script type="text/javascript" async="" src="./Running Sum of 1d Array - LeetCode_files/analytics.js.download"></script><script type="text/javascript" async="" src="./Running Sum of 1d Array - LeetCode_files/gio.js.download"></script><script type="text/javascript"><!-- NREUM: (4) --></script><style type="text/css">:root, :host {
  --fa-font-solid: normal 900 1em/1 "Font Awesome 6 Solid";
  --fa-font-regular: normal 400 1em/1 "Font Awesome 6 Regular";
  --fa-font-light: normal 300 1em/1 "Font Awesome 6 Light";
  --fa-font-thin: normal 100 1em/1 "Font Awesome 6 Thin";
  --fa-font-duotone: normal 900 1em/1 "Font Awesome 6 Duotone";
  --fa-font-sharp-solid: normal 900 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-regular: normal 400 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-light: normal 300 1em/1 "Font Awesome 6 Sharp";
  --fa-font-brands: normal 400 1em/1 "Font Awesome 6 Brands";
}

svg:not(:root).svg-inline--fa, svg:not(:host).svg-inline--fa {
  overflow: visible;
  box-sizing: content-box;
}

.svg-inline--fa {
  display: var(--fa-display, inline-block);
  height: 1em;
  overflow: visible;
  vertical-align: -0.125em;
}
.svg-inline--fa.fa-2xs {
  vertical-align: 0.1em;
}
.svg-inline--fa.fa-xs {
  vertical-align: 0em;
}
.svg-inline--fa.fa-sm {
  vertical-align: -0.0714285705em;
}
.svg-inline--fa.fa-lg {
  vertical-align: -0.2em;
}
.svg-inline--fa.fa-xl {
  vertical-align: -0.25em;
}
.svg-inline--fa.fa-2xl {
  vertical-align: -0.3125em;
}
.svg-inline--fa.fa-pull-left {
  margin-right: var(--fa-pull-margin, 0.3em);
  width: auto;
}
.svg-inline--fa.fa-pull-right {
  margin-left: var(--fa-pull-margin, 0.3em);
  width: auto;
}
.svg-inline--fa.fa-li {
  width: var(--fa-li-width, 2em);
  top: 0.25em;
}
.svg-inline--fa.fa-fw {
  width: var(--fa-fw-width, 1.25em);
}

.fa-layers svg.svg-inline--fa {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
}

.fa-layers-counter, .fa-layers-text {
  display: inline-block;
  position: absolute;
  text-align: center;
}

.fa-layers {
  display: inline-block;
  height: 1em;
  position: relative;
  text-align: center;
  vertical-align: -0.125em;
  width: 1em;
}
.fa-layers svg.svg-inline--fa {
  -webkit-transform-origin: center center;
          transform-origin: center center;
}

.fa-layers-text {
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  -webkit-transform-origin: center center;
          transform-origin: center center;
}

.fa-layers-counter {
  background-color: var(--fa-counter-background-color, #ff253a);
  border-radius: var(--fa-counter-border-radius, 1em);
  box-sizing: border-box;
  color: var(--fa-inverse, #fff);
  line-height: var(--fa-counter-line-height, 1);
  max-width: var(--fa-counter-max-width, 5em);
  min-width: var(--fa-counter-min-width, 1.5em);
  overflow: hidden;
  padding: var(--fa-counter-padding, 0.25em 0.5em);
  right: var(--fa-right, 0);
  text-overflow: ellipsis;
  top: var(--fa-top, 0);
  -webkit-transform: scale(var(--fa-counter-scale, 0.25));
          transform: scale(var(--fa-counter-scale, 0.25));
  -webkit-transform-origin: top right;
          transform-origin: top right;
}

.fa-layers-bottom-right {
  bottom: var(--fa-bottom, 0);
  right: var(--fa-right, 0);
  top: auto;
  -webkit-transform: scale(var(--fa-layers-scale, 0.25));
          transform: scale(var(--fa-layers-scale, 0.25));
  -webkit-transform-origin: bottom right;
          transform-origin: bottom right;
}

.fa-layers-bottom-left {
  bottom: var(--fa-bottom, 0);
  left: var(--fa-left, 0);
  right: auto;
  top: auto;
  -webkit-transform: scale(var(--fa-layers-scale, 0.25));
          transform: scale(var(--fa-layers-scale, 0.25));
  -webkit-transform-origin: bottom left;
          transform-origin: bottom left;
}

.fa-layers-top-right {
  top: var(--fa-top, 0);
  right: var(--fa-right, 0);
  -webkit-transform: scale(var(--fa-layers-scale, 0.25));
          transform: scale(var(--fa-layers-scale, 0.25));
  -webkit-transform-origin: top right;
          transform-origin: top right;
}

.fa-layers-top-left {
  left: var(--fa-left, 0);
  right: auto;
  top: var(--fa-top, 0);
  -webkit-transform: scale(var(--fa-layers-scale, 0.25));
          transform: scale(var(--fa-layers-scale, 0.25));
  -webkit-transform-origin: top left;
          transform-origin: top left;
}

.fa-1x {
  font-size: 1em;
}

.fa-2x {
  font-size: 2em;
}

.fa-3x {
  font-size: 3em;
}

.fa-4x {
  font-size: 4em;
}

.fa-5x {
  font-size: 5em;
}

.fa-6x {
  font-size: 6em;
}

.fa-7x {
  font-size: 7em;
}

.fa-8x {
  font-size: 8em;
}

.fa-9x {
  font-size: 9em;
}

.fa-10x {
  font-size: 10em;
}

.fa-2xs {
  font-size: 0.625em;
  line-height: 0.1em;
  vertical-align: 0.225em;
}

.fa-xs {
  font-size: 0.75em;
  line-height: 0.0833333337em;
  vertical-align: 0.125em;
}

.fa-sm {
  font-size: 0.875em;
  line-height: 0.0714285718em;
  vertical-align: 0.0535714295em;
}

.fa-lg {
  font-size: 1.25em;
  line-height: 0.05em;
  vertical-align: -0.075em;
}

.fa-xl {
  font-size: 1.5em;
  line-height: 0.0416666682em;
  vertical-align: -0.125em;
}

.fa-2xl {
  font-size: 2em;
  line-height: 0.03125em;
  vertical-align: -0.1875em;
}

.fa-fw {
  text-align: center;
  width: 1.25em;
}

.fa-ul {
  list-style-type: none;
  margin-left: var(--fa-li-margin, 2.5em);
  padding-left: 0;
}
.fa-ul > li {
  position: relative;
}

.fa-li {
  left: calc(var(--fa-li-width, 2em) * -1);
  position: absolute;
  text-align: center;
  width: var(--fa-li-width, 2em);
  line-height: inherit;
}

.fa-border {
  border-color: var(--fa-border-color, #eee);
  border-radius: var(--fa-border-radius, 0.1em);
  border-style: var(--fa-border-style, solid);
  border-width: var(--fa-border-width, 0.08em);
  padding: var(--fa-border-padding, 0.2em 0.25em 0.15em);
}

.fa-pull-left {
  float: left;
  margin-right: var(--fa-pull-margin, 0.3em);
}

.fa-pull-right {
  float: right;
  margin-left: var(--fa-pull-margin, 0.3em);
}

.fa-beat {
  -webkit-animation-name: fa-beat;
          animation-name: fa-beat;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, ease-in-out);
          animation-timing-function: var(--fa-animation-timing, ease-in-out);
}

.fa-bounce {
  -webkit-animation-name: fa-bounce;
          animation-name: fa-bounce;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.28, 0.84, 0.42, 1));
          animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.28, 0.84, 0.42, 1));
}

.fa-fade {
  -webkit-animation-name: fa-fade;
          animation-name: fa-fade;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
          animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
}

.fa-beat-fade {
  -webkit-animation-name: fa-beat-fade;
          animation-name: fa-beat-fade;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
          animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
}

.fa-flip {
  -webkit-animation-name: fa-flip;
          animation-name: fa-flip;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, ease-in-out);
          animation-timing-function: var(--fa-animation-timing, ease-in-out);
}

.fa-shake {
  -webkit-animation-name: fa-shake;
          animation-name: fa-shake;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, linear);
          animation-timing-function: var(--fa-animation-timing, linear);
}

.fa-spin {
  -webkit-animation-name: fa-spin;
          animation-name: fa-spin;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 2s);
          animation-duration: var(--fa-animation-duration, 2s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, linear);
          animation-timing-function: var(--fa-animation-timing, linear);
}

.fa-spin-reverse {
  --fa-animation-direction: reverse;
}

.fa-pulse,
.fa-spin-pulse {
  -webkit-animation-name: fa-spin;
          animation-name: fa-spin;
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, steps(8));
          animation-timing-function: var(--fa-animation-timing, steps(8));
}

@media (prefers-reduced-motion: reduce) {
  .fa-beat,
.fa-bounce,
.fa-fade,
.fa-beat-fade,
.fa-flip,
.fa-pulse,
.fa-shake,
.fa-spin,
.fa-spin-pulse {
    -webkit-animation-delay: -1ms;
            animation-delay: -1ms;
    -webkit-animation-duration: 1ms;
            animation-duration: 1ms;
    -webkit-animation-iteration-count: 1;
            animation-iteration-count: 1;
    -webkit-transition-delay: 0s;
            transition-delay: 0s;
    -webkit-transition-duration: 0s;
            transition-duration: 0s;
  }
}
@-webkit-keyframes fa-beat {
  0%, 90% {
    -webkit-transform: scale(1);
            transform: scale(1);
  }
  45% {
    -webkit-transform: scale(var(--fa-beat-scale, 1.25));
            transform: scale(var(--fa-beat-scale, 1.25));
  }
}
@keyframes fa-beat {
  0%, 90% {
    -webkit-transform: scale(1);
            transform: scale(1);
  }
  45% {
    -webkit-transform: scale(var(--fa-beat-scale, 1.25));
            transform: scale(var(--fa-beat-scale, 1.25));
  }
}
@-webkit-keyframes fa-bounce {
  0% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
  10% {
    -webkit-transform: scale(var(--fa-bounce-start-scale-x, 1.1), var(--fa-bounce-start-scale-y, 0.9)) translateY(0);
            transform: scale(var(--fa-bounce-start-scale-x, 1.1), var(--fa-bounce-start-scale-y, 0.9)) translateY(0);
  }
  30% {
    -webkit-transform: scale(var(--fa-bounce-jump-scale-x, 0.9), var(--fa-bounce-jump-scale-y, 1.1)) translateY(var(--fa-bounce-height, -0.5em));
            transform: scale(var(--fa-bounce-jump-scale-x, 0.9), var(--fa-bounce-jump-scale-y, 1.1)) translateY(var(--fa-bounce-height, -0.5em));
  }
  50% {
    -webkit-transform: scale(var(--fa-bounce-land-scale-x, 1.05), var(--fa-bounce-land-scale-y, 0.95)) translateY(0);
            transform: scale(var(--fa-bounce-land-scale-x, 1.05), var(--fa-bounce-land-scale-y, 0.95)) translateY(0);
  }
  57% {
    -webkit-transform: scale(1, 1) translateY(var(--fa-bounce-rebound, -0.125em));
            transform: scale(1, 1) translateY(var(--fa-bounce-rebound, -0.125em));
  }
  64% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
  100% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
}
@keyframes fa-bounce {
  0% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
  10% {
    -webkit-transform: scale(var(--fa-bounce-start-scale-x, 1.1), var(--fa-bounce-start-scale-y, 0.9)) translateY(0);
            transform: scale(var(--fa-bounce-start-scale-x, 1.1), var(--fa-bounce-start-scale-y, 0.9)) translateY(0);
  }
  30% {
    -webkit-transform: scale(var(--fa-bounce-jump-scale-x, 0.9), var(--fa-bounce-jump-scale-y, 1.1)) translateY(var(--fa-bounce-height, -0.5em));
            transform: scale(var(--fa-bounce-jump-scale-x, 0.9), var(--fa-bounce-jump-scale-y, 1.1)) translateY(var(--fa-bounce-height, -0.5em));
  }
  50% {
    -webkit-transform: scale(var(--fa-bounce-land-scale-x, 1.05), var(--fa-bounce-land-scale-y, 0.95)) translateY(0);
            transform: scale(var(--fa-bounce-land-scale-x, 1.05), var(--fa-bounce-land-scale-y, 0.95)) translateY(0);
  }
  57% {
    -webkit-transform: scale(1, 1) translateY(var(--fa-bounce-rebound, -0.125em));
            transform: scale(1, 1) translateY(var(--fa-bounce-rebound, -0.125em));
  }
  64% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
  100% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
}
@-webkit-keyframes fa-fade {
  50% {
    opacity: var(--fa-fade-opacity, 0.4);
  }
}
@keyframes fa-fade {
  50% {
    opacity: var(--fa-fade-opacity, 0.4);
  }
}
@-webkit-keyframes fa-beat-fade {
  0%, 100% {
    opacity: var(--fa-beat-fade-opacity, 0.4);
    -webkit-transform: scale(1);
            transform: scale(1);
  }
  50% {
    opacity: 1;
    -webkit-transform: scale(var(--fa-beat-fade-scale, 1.125));
            transform: scale(var(--fa-beat-fade-scale, 1.125));
  }
}
@keyframes fa-beat-fade {
  0%, 100% {
    opacity: var(--fa-beat-fade-opacity, 0.4);
    -webkit-transform: scale(1);
            transform: scale(1);
  }
  50% {
    opacity: 1;
    -webkit-transform: scale(var(--fa-beat-fade-scale, 1.125));
            transform: scale(var(--fa-beat-fade-scale, 1.125));
  }
}
@-webkit-keyframes fa-flip {
  50% {
    -webkit-transform: rotate3d(var(--fa-flip-x, 0), var(--fa-flip-y, 1), var(--fa-flip-z, 0), var(--fa-flip-angle, -180deg));
            transform: rotate3d(var(--fa-flip-x, 0), var(--fa-flip-y, 1), var(--fa-flip-z, 0), var(--fa-flip-angle, -180deg));
  }
}
@keyframes fa-flip {
  50% {
    -webkit-transform: rotate3d(var(--fa-flip-x, 0), var(--fa-flip-y, 1), var(--fa-flip-z, 0), var(--fa-flip-angle, -180deg));
            transform: rotate3d(var(--fa-flip-x, 0), var(--fa-flip-y, 1), var(--fa-flip-z, 0), var(--fa-flip-angle, -180deg));
  }
}
@-webkit-keyframes fa-shake {
  0% {
    -webkit-transform: rotate(-15deg);
            transform: rotate(-15deg);
  }
  4% {
    -webkit-transform: rotate(15deg);
            transform: rotate(15deg);
  }
  8%, 24% {
    -webkit-transform: rotate(-18deg);
            transform: rotate(-18deg);
  }
  12%, 28% {
    -webkit-transform: rotate(18deg);
            transform: rotate(18deg);
  }
  16% {
    -webkit-transform: rotate(-22deg);
            transform: rotate(-22deg);
  }
  20% {
    -webkit-transform: rotate(22deg);
            transform: rotate(22deg);
  }
  32% {
    -webkit-transform: rotate(-12deg);
            transform: rotate(-12deg);
  }
  36% {
    -webkit-transform: rotate(12deg);
            transform: rotate(12deg);
  }
  40%, 100% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
}
@keyframes fa-shake {
  0% {
    -webkit-transform: rotate(-15deg);
            transform: rotate(-15deg);
  }
  4% {
    -webkit-transform: rotate(15deg);
            transform: rotate(15deg);
  }
  8%, 24% {
    -webkit-transform: rotate(-18deg);
            transform: rotate(-18deg);
  }
  12%, 28% {
    -webkit-transform: rotate(18deg);
            transform: rotate(18deg);
  }
  16% {
    -webkit-transform: rotate(-22deg);
            transform: rotate(-22deg);
  }
  20% {
    -webkit-transform: rotate(22deg);
            transform: rotate(22deg);
  }
  32% {
    -webkit-transform: rotate(-12deg);
            transform: rotate(-12deg);
  }
  36% {
    -webkit-transform: rotate(12deg);
            transform: rotate(12deg);
  }
  40%, 100% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
  }
}
.fa-rotate-90 {
  -webkit-transform: rotate(90deg);
          transform: rotate(90deg);
}

.fa-rotate-180 {
  -webkit-transform: rotate(180deg);
          transform: rotate(180deg);
}

.fa-rotate-270 {
  -webkit-transform: rotate(270deg);
          transform: rotate(270deg);
}

.fa-flip-horizontal {
  -webkit-transform: scale(-1, 1);
          transform: scale(-1, 1);
}

.fa-flip-vertical {
  -webkit-transform: scale(1, -1);
          transform: scale(1, -1);
}

.fa-flip-both,
.fa-flip-horizontal.fa-flip-vertical {
  -webkit-transform: scale(-1, -1);
          transform: scale(-1, -1);
}

.fa-rotate-by {
  -webkit-transform: rotate(var(--fa-rotate-angle, none));
          transform: rotate(var(--fa-rotate-angle, none));
}

.fa-stack {
  display: inline-block;
  vertical-align: middle;
  height: 2em;
  position: relative;
  width: 2.5em;
}

.fa-stack-1x,
.fa-stack-2x {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
  z-index: var(--fa-stack-z-index, auto);
}

.svg-inline--fa.fa-stack-1x {
  height: 1em;
  width: 1.25em;
}
.svg-inline--fa.fa-stack-2x {
  height: 2em;
  width: 2.5em;
}

.fa-inverse {
  color: var(--fa-inverse, #fff);
}

.sr-only,
.fa-sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.sr-only-focusable:not(:focus),
.fa-sr-only-focusable:not(:focus) {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.svg-inline--fa .fa-primary {
  fill: var(--fa-primary-color, currentColor);
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa .fa-secondary {
  fill: var(--fa-secondary-color, currentColor);
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-primary {
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-secondary {
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa mask .fa-primary,
.svg-inline--fa mask .fa-secondary {
  fill: black;
}

.fad.fa-inverse,
.fa-duotone.fa-inverse {
  color: var(--fa-inverse, #fff);
}</style><link rel="preload" href="./Running Sum of 1d Array - LeetCode_files/fd7b307e73120519.css" as="style"><link rel="stylesheet" href="./Running Sum of 1d Array - LeetCode_files/fd7b307e73120519.css" data-n-g=""><link rel="preload" href="./Running Sum of 1d Array - LeetCode_files/c50af6a0173d8aa1.css" as="style"><link rel="stylesheet" href="./Running Sum of 1d Array - LeetCode_files/c50af6a0173d8aa1.css" data-n-p=""><noscript data-n-css=""></noscript><script defer="" nomodule="" src="./Running Sum of 1d Array - LeetCode_files/polyfills-c67a75d1b6f99dc8.js.download"></script><script src="./Running Sum of 1d Array - LeetCode_files/webpack-e0f5f8fae02d677e.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/framework-ac6550882a30386c.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/main-20ba256579e3d931.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/_app-24fcb4182fadb1df.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/328748d6-f8aebf2739a65688.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/c829854d-4ee7c3a4992d5fe7.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/e6848cf3-e709bce199e80e90.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/ee9ce975-2f7c2440a1b84e5e.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/c6bbd088-e4a386c2e4944442.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/f5d5890c-b5db13af837a2748.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/2cca2479-b4c6e203e834f259.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/d3048c20-a96db8198c3fafa3.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/e7372cb8-0b8e608449d0f2ba.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/d59bccd2-3e6c09545275e206.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/7dfef39c-bec8f1b6a137f5ef.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/c46d6b60-4ee2bbc1b979c6f9.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/ea88be26-43b75960b55a0567.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/4b358913-7b696ad89d9cddd0.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/bee240a3-1e8a74efd7d88816.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/cf44d55e-7af3818bd7ed3f6d.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/175675d1-7d4214c893a8873b.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/599b58c7-50bf4b8dc14658e6.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/469a8bf9-6df889f2f4df379a.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/4ad82c5e-802f4c2ef21482b5.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/37bf9728-2a4994f71ede73fb.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/82c1d43a-db7582efb1cf0077.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/60d8647c-a27d9fb5c129e9f4.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/74c95677-c54b68bdf1febed1.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/129-07e4846883f0f080.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/4948-e7abee6742cde155.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/845-9230e138fcfc363b.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/6037-09e9706ea68ef985.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/8592-d594385ddc5565c1.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/6908-ab6ec363cb64b8b1.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/8931-82276d15517b38e1.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/9148-98341db4a24cd68f.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/88-8e63f06639cc5a43.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/5435-d1e235a6273fb577.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/3832-48b3115bd3929885.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/9950-53d6d326580ec968.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/2058-8a440931e807fc33.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/8817-f60ae9497a8c8c8b.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/6246-c7dff37765207b36.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/5872-5e078be9cc936d88.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/7448-3b178f01575c6aa4.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/6461-da7615dac396de8c.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/7405-29185980b1449e92.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/3358-1e248756112d96ea.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/3874-f7d6b6231b97ea39.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/1565-f90eea035ff5e89b.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/1516-1fc06ab8132bd0c9.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/9761-5b0437aba099fa04.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/477-19cb2a330cf823ab.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/8712-2f130e9fd7ef6856.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/3386-5fd5d0bdea427297.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/9326-346b376de000c8bb.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/5253-b4a6f79b7881d3ce.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/5384-531d6c5e3f93d387.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/1184-40dc458b101bf34b.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/7826-316eb73b4f1565a8.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/4415-547805211d8029a9.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/8421-3182e833aea54298.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/6347-71c1a228c7d5d3a0.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/2959-b1a33b160e408da5.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/2089-eedec41c8d6c2b2b.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/7845-ca6c37e5c51cc521.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/8048-a7c801c175975067.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/[[...tab]]-8f64cdf5ddf1cae5.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/_buildManifest.js.download" defer=""></script><script src="./Running Sum of 1d Array - LeetCode_files/_ssgManifest.js.download" defer=""></script><style type="text/css">.transform-component-module_wrapper__7HFJe {
  position: relative;
  width: -moz-fit-content;
  width: fit-content;
  height: -moz-fit-content;
  height: fit-content;
  overflow: hidden;
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none;
  margin: 0;
  padding: 0;
}
.transform-component-module_content__uCDPE {
  display: flex;
  flex-wrap: wrap;
  width: -moz-fit-content;
  width: fit-content;
  height: -moz-fit-content;
  height: fit-content;
  margin: 0;
  padding: 0;
  transform-origin: 0% 0%;
}
.transform-component-module_content__uCDPE img {
  pointer-events: none;
}
</style><style id="74316">.C6UnP>div{max-width:100%;padding:0 12px}
/*# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL3NoYXJlZC9jb21wb25lbnRzL25hdi9uYXZiYXIvaW5kZXguaXNvLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQSxXQUNFLGNBQWUsQ0FDZixjQUNGIiwic291cmNlc0NvbnRlbnQiOlsiLmJhbm5lckNvbnRlbnRXaWR0aEZ1bGw+ZGl2IHtcbiAgbWF4LXdpZHRoOiAxMDAlO1xuICBwYWRkaW5nOiAwIDEycHg7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style id="32232">.elfjS pre{border-color:var(--border-tertiary);border-left-width:2px;color:var(--text-secondary);font-family:Menlo,sans-serif;font-size:.875rem;line-height:1.25rem;margin-bottom:1rem;margin-top:1rem;overflow:visible;padding-left:1rem;white-space:pre-wrap}.elfjS pre strong{--tw-text-opacity:1;color:rgb(38 38 38/var(--tw-text-opacity))}.dark .elfjS pre strong{--tw-text-opacity:1;color:rgb(255 255 255/var(--tw-text-opacity))}.elfjS a{--tw-text-opacity:1;color:rgb(0 122 255/var(--tw-text-opacity))}.dark .elfjS a{--tw-text-opacity:1;color:rgb(10 132 255/var(--tw-text-opacity))}.elfjS ul{list-style-type:disc}.elfjS ol,.elfjS ul{margin-bottom:1rem;margin-left:1rem;margin-right:1rem}.elfjS ol{list-style-type:decimal}.elfjS li{margin-bottom:.75rem}.elfjS p{margin-bottom:1rem}.elfjS code{background-color:#000a2008;border-color:#0000000d;border-radius:5px;border-width:1px;color:#262626bf;font-family:Menlo,sans-serif;font-size:.75rem;line-height:1rem;padding:.125rem;white-space:pre-wrap}.dark .elfjS code{background-color:#ffffff12;border-color:#f7faff1f;color:#eff1f6bf}.elfjS blockquote{border-color:#0000000d;border-left-width:4px;color:#262626bf;padding-left:1rem}.dark .elfjS blockquote{border-color:#f7faff1f;color:#eff1f6bf}.content-example-testcase{--tw-text-opacity:1;color:rgb(38 38 38/var(--tw-text-opacity));font-size:1rem;font-weight:500;line-height:1.5rem;margin-bottom:1rem}.dark .content-example-testcase{--tw-text-opacity:1;color:rgb(255 255 255/var(--tw-text-opacity))}.elfjS img{height:auto!important;max-width:100%}.elfjS .exRnx{--tw-text-opacity:1;color:rgb(38 38 38/var(--tw-text-opacity));font-size:1rem;font-weight:500;line-height:1.5rem;margin-bottom:1rem}:is(.dKYIq .elfjS .exRnx){--tw-text-opacity:1;color:rgb(38 38 38/var(--tw-text-opacity))}.example-block{border-color:var(--border-tertiary);border-left-width:2px;color:var(--text-secondary);font-size:14px;margin-bottom:1rem;margin-top:1rem;overflow:visible;padding-left:1rem}.example-block pre{border-left-width:0;border-style:none;padding-left:0}.example-block .example-io{font-family:Menlo,sans-serif;font-size:.85rem}.example-block pre.example-io{overflow:auto;white-space:pre}.elfjS table{--tw-text-opacity:1;border-radius:.5rem;border-style:hidden;box-shadow:0 0 0 1px #e5e5e5;color:rgb(38 38 38/var(--tw-text-opacity));margin-bottom:.75rem}.dark .elfjS table{--tw-border-opacity:1;--tw-text-opacity:1;border-color:rgb(74 74 74/var(--tw-border-opacity));box-shadow:0 0 0 1px #424242;color:rgb(255 255 255/var(--tw-text-opacity))}.elfjS table th{--tw-border-opacity:1;background-color:#000a200d;border-color:rgb(223 223 223/var(--tw-border-opacity));border-width:1px;font-weight:500;padding:.5rem .625rem}.elfjS table th:first-child{border-top-left-radius:.5rem}.elfjS table th:last-child{border-top-right-radius:.5rem}.dark .elfjS table th{--tw-border-opacity:1;background-color:#ffffff1a;border-color:rgb(74 74 74/var(--tw-border-opacity))}.elfjS table td{--tw-border-opacity:1;border-color:rgb(223 223 223/var(--tw-border-opacity));border-width:1px;padding:.5rem .625rem}.dark .elfjS table td{--tw-border-opacity:1;border-color:rgb(74 74 74/var(--tw-border-opacity))}.elfjS .language-md .table{display:inline!important}
/*# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL21vZHVsZXMvcHJvYmxlbXMvY29tcG9uZW50cy9kZXNjcmlwdGlvbi9Db250ZW50L0hUTUxDb250ZW50Lmlzby5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQ0UsV0FBQSxtQ0FBOEgsQ0FBOUgscUJBQThILENBQTlILDJCQUE4SCxDQUE5SCw0QkFBOEgsQ0FBOUgsaUJBQThILENBQTlILG1CQUE4SCxDQUE5SCxrQkFBOEgsQ0FBOUgsZUFBOEgsQ0FBOUgsZ0JBQThILENBQTlILGlCQUE4SCxDQUE5SCxvQkFBOEgsQ0FJOUgsa0JBQUEsbUJBQW1CLENBQW5CLDBDQUFtQixDQUluQix3QkFBQSxtQkFBd0IsQ0FBeEIsNkNBQXdCLENBSXhCLFNBQUEsbUJBQWtCLENBQWxCLDJDQUFrQixDQUlsQixlQUFBLG1CQUF1QixDQUF2Qiw0Q0FBdUIsQ0FJdkIsVUFBQSxvQkFBMEIsQ0FJMUIsb0JBSkEsa0JBQTBCLENBQTFCLGdCQUEwQixDQUExQixpQkFJNkIsQ0FBN0IsVUFBQSx1QkFBNkIsQ0FJN0IsVUFBQSxvQkFBVyxDQUlYLFNBQUEsa0JBQVcsQ0FJWCxZQUFBLDBCQUFrSCxDQUFsSCxzQkFBa0gsQ0FBbEgsaUJBQWtILENBQWxILGdCQUFrSCxDQUFsSCxlQUFrSCxDQUFsSCw0QkFBa0gsQ0FBbEgsZ0JBQWtILENBQWxILGdCQUFrSCxDQUFsSCxlQUFrSCxDQUFsSCxvQkFBa0gsQ0FJbEgsa0JBQUEsMEJBQTZELENBQTdELHNCQUE2RCxDQUE3RCxlQUE2RCxDQUk3RCxrQkFBQSxzQkFBb0QsQ0FBcEQscUJBQW9ELENBQXBELGVBQW9ELENBQXBELGlCQUFvRCxDQUlwRCx3QkFBQSxzQkFBOEMsQ0FBOUMsZUFBOEMsQ0FJOUMsMEJBQUEsbUJBQThDLENBQTlDLDBDQUE4QyxDQUE5QyxjQUE4QyxDQUE5QyxlQUE4QyxDQUE5QyxrQkFBOEMsQ0FBOUMsa0JBQThDLENBSTlDLGdDQUFBLG1CQUF3QixDQUF4Qiw2Q0FBd0IsQ0FHMUIsV0FFRSxxQkFBdUIsQ0FEdkIsY0FFRixDQUdFLGNBQUEsbUJBQWdFLENBQWhFLDBDQUFnRSxDQUFoRSxjQUFnRSxDQUFoRSxlQUFnRSxDQUFoRSxrQkFBZ0UsQ0FBaEUsa0JBQWdFLENBQWhFLDBCQUFBLG1CQUFnRSxDQUFoRSwwQ0FBZ0UsQ0FJaEUsZUFBQSxtQ0FBbUcsQ0FBbkcscUJBQW1HLENBQW5HLDJCQUFtRyxDQUFuRyxjQUFtRyxDQUFuRyxrQkFBbUcsQ0FBbkcsZUFBbUcsQ0FBbkcsZ0JBQW1HLENBQW5HLGlCQUFtRyxDQUVqRyxtQkFBQSxtQkFBa0MsQ0FBbEMsaUJBQWtDLENBQWxDLGNBQWtDLENBR2xDLDJCQUFBLDRCQUFnQyxDQUFoQyxnQkFBZ0MsQ0FHaEMsOEJBQUEsYUFBbUMsQ0FBbkMsZUFBbUMsQ0FJdkMsYUFFRSxtQkFBaUQsQ0FBakQsbUJBQWlELENBQWpELG1CQUFpRCxDQURqRCw0QkFBNkIsQ0FDN0IsMENBQWlELENBQWpELG9CQUNGLENBRUEsbUJBRUUscUJBQTJDLENBQTNDLG1CQUEyQyxDQUEzQyxtREFBMkMsQ0FEM0MsNEJBQTZCLENBQzdCLDZDQUNGLENBR0UsZ0JBQUEscUJBQW1FLENBQW5FLDBCQUFtRSxDQUFuRSxzREFBbUUsQ0FBbkUsZ0JBQW1FLENBQW5FLGVBQW1FLENBQW5FLHFCQUFtRSxDQUluRSw0QkFBQSw0QkFBb0IsQ0FJcEIsMkJBQUEsNkJBQW9CLENBSXBCLHNCQUFBLHFCQUF3QyxDQUF4QywwQkFBd0MsQ0FBeEMsbURBQXdDLENBSXhDLGdCQUFBLHFCQUE2QyxDQUE3QyxzREFBNkMsQ0FBN0MsZ0JBQTZDLENBQTdDLHFCQUE2QyxDQUk3QyxzQkFBQSxxQkFBeUIsQ0FBekIsbURBQXlCLENBRzNCLDJCQUtFLHdCQUNGIiwic291cmNlc0NvbnRlbnQiOlsiLmh0bWwgcHJlIHtcbiAgQGFwcGx5IGJvcmRlci1ib3JkZXItdGVydGlhcnkgZm9udC1tZW5sbyB0ZXh0LXRleHQtc2Vjb25kYXJ5IG15LTQgb3ZlcmZsb3ctdmlzaWJsZSB3aGl0ZXNwYWNlLXByZS13cmFwIGJvcmRlci1sLTIgcGwtNCB0ZXh0LXNtO1xufVxuXG4uaHRtbCBwcmUgc3Ryb25nIHtcbiAgQGFwcGx5IHRleHQtbGFiZWwtMTtcbn1cblxuOmdsb2JhbCguZGFyaykgLmh0bWwgcHJlIHN0cm9uZyB7XG4gIEBhcHBseSB0ZXh0LWRhcmstbGFiZWwtMTtcbn1cblxuLmh0bWwgYSB7XG4gIEBhcHBseSB0ZXh0LWJsdWUtcztcbn1cblxuOmdsb2JhbCguZGFyaykgLmh0bWwgYSB7XG4gIEBhcHBseSB0ZXh0LWRhcmstYmx1ZS1zO1xufVxuXG4uaHRtbCB1bCB7XG4gIEBhcHBseSBteC00IG1iLTQgbGlzdC1kaXNjO1xufVxuXG4uaHRtbCBvbCB7XG4gIEBhcHBseSBteC00IG1iLTQgbGlzdC1kZWNpbWFsO1xufVxuXG4uaHRtbCBsaSB7XG4gIEBhcHBseSBtYi0zO1xufVxuXG4uaHRtbCBwIHtcbiAgQGFwcGx5IG1iLTQ7XG59XG5cbi5odG1sIGNvZGUge1xuICBAYXBwbHkgYm9yZGVyLWRpdmlkZXItMyBiZy1maWxsLTQgZm9udC1tZW5sbyB0ZXh0LWxhYmVsLTIgd2hpdGVzcGFjZS1wcmUtd3JhcCByb3VuZGVkIGJvcmRlciBweC0wLjUgcHktMC41IHRleHQteHM7XG59XG5cbjpnbG9iYWwoLmRhcmspIC5odG1sIGNvZGUge1xuICBAYXBwbHkgYm9yZGVyLWRhcmstZGl2aWRlci0zIGJnLWRhcmstZmlsbC00IHRleHQtZGFyay1sYWJlbC0yO1xufVxuXG4uaHRtbCBibG9ja3F1b3RlIHtcbiAgQGFwcGx5IGJvcmRlci1kaXZpZGVyLTMgdGV4dC1sYWJlbC0yIGJvcmRlci1sLTQgcGwtNDtcbn1cblxuOmdsb2JhbCguZGFyaykgLmh0bWwgYmxvY2txdW90ZSB7XG4gIEBhcHBseSBib3JkZXItZGFyay1kaXZpZGVyLTMgdGV4dC1kYXJrLWxhYmVsLTI7XG59XG5cbjpnbG9iYWwoLmNvbnRlbnQtZXhhbXBsZS10ZXN0Y2FzZSkge1xuICBAYXBwbHkgdGV4dC1sYWJlbC0xIG1iLTQgdGV4dC1iYXNlIGZvbnQtbWVkaXVtO1xufVxuXG46Z2xvYmFsKC5kYXJrIC5jb250ZW50LWV4YW1wbGUtdGVzdGNhc2UpIHtcbiAgQGFwcGx5IHRleHQtZGFyay1sYWJlbC0xO1xufVxuXG4uaHRtbCBpbWcge1xuICBtYXgtd2lkdGg6IDEwMCU7XG4gIGhlaWdodDogYXV0byAhaW1wb3J0YW50O1xufVxuXG4uaHRtbCAuZXhhbXBsZSB7XG4gIEBhcHBseSB0ZXh0LWxhYmVsLTEgZGFyazp0ZXh0LWxhYmVsLTEgbWItNCB0ZXh0LWJhc2UgZm9udC1tZWRpdW07XG59XG5cbjpnbG9iYWwoLmV4YW1wbGUtYmxvY2spIHtcbiAgQGFwcGx5IGJvcmRlci1ib3JkZXItdGVydGlhcnkgdGV4dC10ZXh0LXNlY29uZGFyeSBteS00IG92ZXJmbG93LXZpc2libGUgYm9yZGVyLWwtMiBwbC00IHRleHQtWzE0cHhdO1xuICBwcmUge1xuICAgIEBhcHBseSBib3JkZXItbC0wIGJvcmRlci1ub25lIHBsLTA7XG4gIH1cbiAgOmdsb2JhbCguZXhhbXBsZS1pbykge1xuICAgIEBhcHBseSBmb250LW1lbmxvIHRleHQtWzAuODVyZW1dO1xuICB9XG4gIHByZTpnbG9iYWwoLmV4YW1wbGUtaW8pIHtcbiAgICBAYXBwbHkgb3ZlcmZsb3ctYXV0byB3aGl0ZXNwYWNlLXByZTtcbiAgfVxufVxuXG4uaHRtbCB0YWJsZSB7XG4gIGJveC1zaGFkb3c6IDAgMCAwIDFweCAjZTVlNWU1O1xuICBAYXBwbHkgdGV4dC1sYWJlbC0xIG1iLTMgcm91bmRlZC1sZyBib3JkZXItaGlkZGVuO1xufVxuXG46Z2xvYmFsKC5kYXJrKSAuaHRtbCB0YWJsZSB7XG4gIGJveC1zaGFkb3c6IDAgMCAwIDFweCAjNDI0MjQyO1xuICBAYXBwbHkgYm9yZGVyLWRhcmstZ3JheS00IHRleHQtZGFyay1sYWJlbC0xO1xufVxuXG4uaHRtbCB0YWJsZSB0aCB7XG4gIEBhcHBseSBib3JkZXItZ3JheS00IGJnLWZpbGwtMyBib3JkZXItWzFweF0gcHgtMi41IHB5LTIgZm9udC1tZWRpdW07XG59XG5cbi5odG1sIHRhYmxlIHRoOmZpcnN0LWNoaWxkIHtcbiAgQGFwcGx5IHJvdW5kZWQtdGwtbGc7XG59XG5cbi5odG1sIHRhYmxlIHRoOmxhc3QtY2hpbGQge1xuICBAYXBwbHkgcm91bmRlZC10ci1sZztcbn1cblxuOmdsb2JhbCguZGFyaykgLmh0bWwgdGFibGUgdGgge1xuICBAYXBwbHkgYm9yZGVyLWRhcmstZ3JheS00IGJnLWRhcmstZmlsbC0zO1xufVxuXG4uaHRtbCB0YWJsZSB0ZCB7XG4gIEBhcHBseSBib3JkZXItZ3JheS00IGJvcmRlci1bMXB4XSBweC0yLjUgcHktMjtcbn1cblxuOmdsb2JhbCguZGFyaykgLmh0bWwgdGFibGUgdGQge1xuICBAYXBwbHkgYm9yZGVyLWRhcmstZ3JheS00O1xufVxuXG4uaHRtbCA6Z2xvYmFsKC5sYW5ndWFnZS1tZCAudGFibGUpIHtcbiAgLypcbiAgICBGSVhNRTogdGFpbHdpbmQtY3NzIGAudGFibGVgIGNvbmZsaWN0IHdpdGggaGlnaGxpZ2h0LmpzIGAudGFibGVgLFxuICAgICAgICAgICB3aGljaCBqdXN0IGhhdmUgZGlmZmVyZW50IG1lYW5pbmdzIGJ1dCB3aXRoIHRoZSBzYW1lIG5hbWVcbiAgICAgKi9cbiAgZGlzcGxheTogaW5saW5lICFpbXBvcnRhbnQ7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style id="60213">[contenteditable=true]:empty:before{color:#3c3c434d;content:attr(placeholder);display:block}.dark [contenteditable=true]:empty:before{color:#ebebf54d}
/*# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL21vZHVsZXMvcHJvYmxlbXMvY29tcG9uZW50cy90ZXN0Y2FzZS90ZXN0Y2FzZS1pbnB1dC5pc28uY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBLG9DQUdFLGVBQTJCLENBRjNCLHlCQUEwQixDQUMxQixhQUVGLENBRUEsMENBQ0UsZUFDRiIsInNvdXJjZXNDb250ZW50IjpbIjpnbG9iYWwoW2NvbnRlbnRlZGl0YWJsZT0ndHJ1ZSddOmVtcHR5OmJlZm9yZSkge1xuICBjb250ZW50OiBhdHRyKHBsYWNlaG9sZGVyKTtcbiAgZGlzcGxheTogYmxvY2s7XG4gIGNvbG9yOiByZ2IoNjAsIDYwLCA2NywgMC4zKTtcbn1cblxuOmdsb2JhbCguZGFyayBbY29udGVudGVkaXRhYmxlPSd0cnVlJ106ZW1wdHk6YmVmb3JlKSB7XG4gIGNvbG9yOiByZ2IoMjM1LCAyMzUsIDI0NSwgMC4zKTtcbn1cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style type="text/css"></style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-aria-container {
	position: absolute; /* try to hide from window but not from screen readers */
	left:-999em;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -------------------- IE10 remove auto clear button -------------------- */

::-ms-clear {
	display: none;
}

/* All widgets */
/* I am not a big fan of this rule */
.monaco-editor .editor-widget input {
	color: inherit;
}

/* -------------------- Editor -------------------- */

.monaco-editor {
	position: relative;
	overflow: visible;
	-webkit-text-size-adjust: 100%;
}

/* -------------------- Misc -------------------- */

.monaco-editor .overflow-guard {
	position: relative;
	overflow: hidden;
}

.monaco-editor .view-overlays {
	position: absolute;
	top: 0;
}

/*
.monaco-editor .auto-closed-character {
	opacity: 0.3;
}
*/
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .inputarea {
	min-width: 0;
	min-height: 0;
	margin: 0;
	padding: 0;
	position: absolute;
	outline: none !important;
	resize: none;
	border: none;
	overflow: hidden;
	color: transparent;
	background-color: transparent;
}
/*.monaco-editor .inputarea {
	position: fixed !important;
	width: 800px !important;
	height: 500px !important;
	top: initial !important;
	left: initial !important;
	bottom: 0 !important;
	right: 0 !important;
	color: black !important;
	background: white !important;
	line-height: 15px !important;
	font-size: 14px !important;
}*/
.monaco-editor .inputarea.ime-input {
	z-index: 10;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .line-numbers {
	font-variant-numeric: tabular-nums;
	position: absolute;
	text-align: right;
	display: inline-block;
	vertical-align: middle;
	box-sizing: border-box;
	cursor: default;
	height: 100%;
}

.monaco-editor .relative-current-line-number {
	text-align: left;
	display: inline-block;
	width: 100%;
}

.monaco-editor .margin-view-overlays .line-numbers.lh-odd {
	margin-top: 1px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-mouse-cursor-text {
	cursor: text;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line.current-line-margin.current-line-margin-both {
	border-right: 0;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cdr = core decorations rendering (div)
*/
.monaco-editor .lines-content .cdr {
	position: absolute;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Arrows */
.monaco-scrollable-element > .scrollbar > .scra {
	cursor: pointer;
	font-size: 11px !important;
}

.monaco-scrollable-element > .visible {
	opacity: 1;

	/* Background rule added for IE9 - to allow clicks on dom node */
	background:rgba(0,0,0,0);

	transition: opacity 100ms linear;
}
.monaco-scrollable-element > .invisible {
	opacity: 0;
	pointer-events: none;
}
.monaco-scrollable-element > .invisible.fade {
	transition: opacity 800ms linear;
}

/* Scrollable Content Inset Shadow */
.monaco-scrollable-element > .shadow {
	position: absolute;
	display: none;
}
.monaco-scrollable-element > .shadow.top {
	display: block;
	top: 0;
	left: 3px;
	height: 3px;
	width: 100%;
}
.monaco-scrollable-element > .shadow.left {
	display: block;
	top: 3px;
	left: 0;
	height: 100%;
	width: 3px;
}
.monaco-scrollable-element > .shadow.top-left-corner {
	display: block;
	top: 0;
	left: 0;
	height: 3px;
	width: 3px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .glyph-margin {
	position: absolute;
	top: 0;
}

/*
	Keeping name short for faster parsing.
	cgmr = core glyph margin rendering (div)
*/
.monaco-editor .margin-view-overlays .cgmr {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .lines-content .core-guide {
	position: absolute;
	box-sizing: border-box;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Uncomment to see lines flashing when they're painted */
/*.monaco-editor .view-lines > .view-line {
	background-color: none;
	animation-name: flash-background;
	animation-duration: 800ms;
}
@keyframes flash-background {
	0%   { background-color: lightgreen; }
	100% { background-color: none }
}*/

.mtkcontrol {
	color: rgb(255, 255, 255) !important;
	background: rgb(150, 0, 0) !important;
}

.monaco-editor.no-user-select .lines-content,
.monaco-editor.no-user-select .view-line,
.monaco-editor.no-user-select .view-lines {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-editor.enable-user-select {
	user-select: initial;
	-webkit-user-select: initial;
	-ms-user-select: initial;
}

.monaco-editor .view-lines {
	white-space: nowrap;
}

.monaco-editor .view-line {
	position: absolute;
	width: 100%;
}

.monaco-editor .mtkz {
	display: inline-block;
}

/* TODO@tokenization bootstrap fix */
/*.monaco-editor .view-line > span > span {
	float: none;
	min-height: inherit;
	margin-left: inherit;
}*/
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .lines-decorations {
	position: absolute;
	top: 0;
	background: white;
}

/*
	Keeping name short for faster parsing.
	cldr = core lines decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cldr {
	position: absolute;
	height: 100%;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cmdr = core margin decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cmdr {
	position: absolute;
	left: 0;
	width: 100%;
	height: 100%;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* START cover the case that slider is visible on mouseover */
.monaco-editor .minimap.slider-mouseover .minimap-slider {
	opacity: 0;
	transition: opacity 100ms linear;
}
.monaco-editor .minimap.slider-mouseover:hover .minimap-slider {
	opacity: 1;
}
.monaco-editor .minimap.slider-mouseover .minimap-slider.active {
	opacity: 1;
}
/* END cover the case that slider is visible on mouseover */

.monaco-editor .minimap-shadow-hidden {
	position: absolute;
	width: 0;
}
.monaco-editor .minimap-shadow-visible {
	position: absolute;
	left: -6px;
	width: 6px;
}
.monaco-editor.no-minimap-shadow .minimap-shadow-visible {
	position: absolute;
	left: -1px;
	width: 1px;
}

/* 0.5s fade in/out for the minimap */
.minimap.autohide {
	opacity: 0.0;
	transition: opacity 0.5s;
}
.minimap.autohide:hover {
	opacity: 1.0;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .overlayWidgets {
	position: absolute;
	top: 0;
	left:0;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-ruler {
	position: absolute;
	top: 0;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .scroll-decoration {
	position: absolute;
	top: 0;
	left: 0;
	height: 6px;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cslr = core selections layer rendering (div)
*/
.monaco-editor .lines-content .cslr {
	position: absolute;
}

.monaco-editor			.top-left-radius		{ border-top-left-radius: 3px; }
.monaco-editor			.bottom-left-radius		{ border-bottom-left-radius: 3px; }
.monaco-editor			.top-right-radius		{ border-top-right-radius: 3px; }
.monaco-editor			.bottom-right-radius	{ border-bottom-right-radius: 3px; }

.monaco-editor.hc-black .top-left-radius		{ border-top-left-radius: 0; }
.monaco-editor.hc-black .bottom-left-radius		{ border-bottom-left-radius: 0; }
.monaco-editor.hc-black .top-right-radius		{ border-top-right-radius: 0; }
.monaco-editor.hc-black .bottom-right-radius	{ border-bottom-right-radius: 0; }

.monaco-editor.hc-light .top-left-radius		{ border-top-left-radius: 0; }
.monaco-editor.hc-light .bottom-left-radius		{ border-bottom-left-radius: 0; }
.monaco-editor.hc-light .top-right-radius		{ border-top-right-radius: 0; }
.monaco-editor.hc-light .bottom-right-radius	{ border-bottom-right-radius: 0; }
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .cursors-layer {
	position: absolute;
	top: 0;
}

.monaco-editor .cursors-layer > .cursor {
	position: absolute;
	overflow: hidden;
}

/* -- smooth-caret-animation -- */
.monaco-editor .cursors-layer.cursor-smooth-caret-animation > .cursor {
	transition: all 80ms;
}

/* -- block-outline-style -- */
.monaco-editor .cursors-layer.cursor-block-outline-style > .cursor {
	box-sizing: border-box;
	background: transparent !important;
	border-style: solid;
	border-width: 1px;
}

/* -- underline-style -- */
.monaco-editor .cursors-layer.cursor-underline-style > .cursor {
	border-bottom-width: 2px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

/* -- underline-thin-style -- */
.monaco-editor .cursors-layer.cursor-underline-thin-style > .cursor {
	border-bottom-width: 1px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

@keyframes monaco-cursor-smooth {
	0%,
	20% {
		opacity: 1;
	}
	60%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-phase {
	0%,
	20% {
		opacity: 1;
	}
	90%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-expand {
	0%,
	20% {
		transform: scaleY(1);
	}
	80%,
	100% {
		transform: scaleY(0);
	}
}

.cursor-smooth {
	animation: monaco-cursor-smooth 0.5s ease-in-out 0s 20 alternate;
}

.cursor-phase {
	animation: monaco-cursor-phase 0.5s ease-in-out 0s 20 alternate;
}

.cursor-expand > .cursor {
	animation: monaco-cursor-expand 0.5s ease-in-out 0s 20 alternate;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .blockDecorations-container {
	position: absolute;
	top: 0;
}

.monaco-editor .blockDecorations-block {
	position: absolute;
	box-sizing: border-box;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .bracket-match {
	box-sizing: border-box;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor.vs .dnd-target,
.monaco-editor.hc-light .dnd-target {
	border-right: 2px dotted black;
	color: white; /* opposite of black */
}
.monaco-editor.vs-dark .dnd-target {
	border-right: 2px dotted #AEAFAD;
	color: #51504f; /* opposite of #AEAFAD */
}
.monaco-editor.hc-black .dnd-target {
	border-right: 2px dotted #fff;
	color: #000; /* opposite of #fff */
}

.monaco-editor.mouse-default .view-lines,
.monaco-editor.vs-dark.mac.mouse-default .view-lines,
.monaco-editor.hc-black.mac.mouse-default .view-lines,
.monaco-editor.hc-light.mac.mouse-default .view-lines {
	cursor: default;
}
.monaco-editor.mouse-copy .view-lines,
.monaco-editor.vs-dark.mac.mouse-copy .view-lines,
.monaco-editor.hc-black.mac.mouse-copy .view-lines,
.monaco-editor.hc-light.mac.mouse-copy .view-lines {
	cursor: copy;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-custom-toggle {
	margin-left: 2px;
	float: left;
	cursor: pointer;
	overflow: hidden;
	width: 20px;
	height: 20px;
	border-radius: 3px;
	border: 1px solid transparent;
	padding: 1px;
	box-sizing:	border-box;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-custom-toggle:hover {
	background-color: var(--vscode-inputOption-hoverBackground);
}

.hc-black .monaco-custom-toggle:hover,
.hc-light .monaco-custom-toggle:hover {
	border: 1px dashed var(--vscode-focusBorder);
}

.hc-black .monaco-custom-toggle,
.hc-light .monaco-custom-toggle {
	background: none;
}

.hc-black .monaco-custom-toggle:hover,
.hc-light .monaco-custom-toggle:hover {
	background: none;
}

.monaco-custom-toggle.monaco-checkbox {
	height: 18px;
	width: 18px;
	border: 1px solid transparent;
	border-radius: 3px;
	margin-right: 9px;
	margin-left: 0px;
	padding: 0px;
	opacity: 1;
	background-size: 16px !important;
}

/* hide check when unchecked */
.monaco-custom-toggle.monaco-checkbox:not(.checked)::before {
	visibility: hidden;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

:root {
	--sash-size: 4px;
}

.monaco-sash {
	position: absolute;
	z-index: 35;
	touch-action: none;
}

.monaco-sash.disabled {
	pointer-events: none;
}

.monaco-sash.mac.vertical {
	cursor: col-resize;
}

.monaco-sash.vertical.minimum {
	cursor: e-resize;
}

.monaco-sash.vertical.maximum {
	cursor: w-resize;
}

.monaco-sash.mac.horizontal {
	cursor: row-resize;
}

.monaco-sash.horizontal.minimum {
	cursor: s-resize;
}

.monaco-sash.horizontal.maximum {
	cursor: n-resize;
}

.monaco-sash.disabled {
	cursor: default !important;
	pointer-events: none !important;
}

.monaco-sash.vertical {
	cursor: ew-resize;
	top: 0;
	width: var(--sash-size);
	height: 100%;
}

.monaco-sash.horizontal {
	cursor: ns-resize;
	left: 0;
	width: 100%;
	height: var(--sash-size);
}

.monaco-sash:not(.disabled) > .orthogonal-drag-handle {
	content: " ";
	height: calc(var(--sash-size) * 2);
	width: calc(var(--sash-size) * 2);
	z-index: 100;
	display: block;
	cursor: all-scroll;
	position: absolute;
}

.monaco-sash.horizontal.orthogonal-edge-north:not(.disabled)
	> .orthogonal-drag-handle.start,
.monaco-sash.horizontal.orthogonal-edge-south:not(.disabled)
	> .orthogonal-drag-handle.end {
	cursor: nwse-resize;
}

.monaco-sash.horizontal.orthogonal-edge-north:not(.disabled)
	> .orthogonal-drag-handle.end,
.monaco-sash.horizontal.orthogonal-edge-south:not(.disabled)
	> .orthogonal-drag-handle.start {
	cursor: nesw-resize;
}

.monaco-sash.vertical > .orthogonal-drag-handle.start {
	left: calc(var(--sash-size) * -0.5);
	top: calc(var(--sash-size) * -1);
}
.monaco-sash.vertical > .orthogonal-drag-handle.end {
	left: calc(var(--sash-size) * -0.5);
	bottom: calc(var(--sash-size) * -1);
}
.monaco-sash.horizontal > .orthogonal-drag-handle.start {
	top: calc(var(--sash-size) * -0.5);
	left: calc(var(--sash-size) * -1);
}
.monaco-sash.horizontal > .orthogonal-drag-handle.end {
	top: calc(var(--sash-size) * -0.5);
	right: calc(var(--sash-size) * -1);
}

.monaco-sash:before {
	content: '';
	pointer-events: none;
	position: absolute;
	width: 100%;
	height: 100%;
	transition: background-color 0.1s ease-out;
	background: transparent;
}

.monaco-sash.vertical:before {
	width: var(--sash-hover-size);
	left: calc(50% - (var(--sash-hover-size) / 2));
}

.monaco-sash.horizontal:before {
	height: var(--sash-hover-size);
	top: calc(50% - (var(--sash-hover-size) / 2));
}

.pointer-events-disabled {
	pointer-events: none !important;
}

/** Debug **/

.monaco-sash.debug {
	background: cyan;
}

.monaco-sash.debug.disabled {
	background: rgba(0, 255, 255, 0.2);
}

.monaco-sash.debug:not(.disabled) > .orthogonal-drag-handle {
	background: red;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Find widget */
.monaco-editor .find-widget {
	position: absolute;
	z-index: 35;
	height: 33px;
	overflow: hidden;
	line-height: 19px;
	transition: transform 200ms linear;
	padding: 0 4px;
	box-sizing: border-box;
	transform: translateY(calc(-100% - 10px)); /* shadow (10px) */
}

.monaco-workbench.reduce-motion .monaco-editor .find-widget {
	transition: transform 0ms linear;
}

.monaco-editor .find-widget textarea {
	margin: 0px;
}

.monaco-editor .find-widget.hiddenEditor {
	display: none;
}

/* Find widget when replace is toggled on */
.monaco-editor .find-widget.replaceToggled > .replace-part {
	display: flex;
}

.monaco-editor .find-widget.visible  {
	transform: translateY(0);
}

.monaco-editor .find-widget .monaco-inputbox.synthetic-focus {
	outline: 1px solid -webkit-focus-ring-color;
	outline-offset: -1px;
}

.monaco-editor .find-widget .monaco-inputbox .input {
	background-color: transparent;
	min-height: 0;
}

.monaco-editor .find-widget .monaco-findInput .input {
	font-size: 13px;
}

.monaco-editor .find-widget > .find-part,
.monaco-editor .find-widget > .replace-part {
	margin: 4px 0 0 17px;
	font-size: 12px;
	display: flex;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox,
.monaco-editor .find-widget > .replace-part .monaco-inputbox {
	min-height: 25px;
}


.monaco-editor .find-widget > .replace-part .monaco-inputbox > .ibwrapper > .mirror {
	padding-right: 22px;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox > .ibwrapper > .input,
.monaco-editor .find-widget > .find-part .monaco-inputbox > .ibwrapper > .mirror,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .ibwrapper > .input,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .ibwrapper > .mirror {
	padding-top: 2px;
	padding-bottom: 2px;
}

.monaco-editor .find-widget > .find-part .find-actions {
	height: 25px;
	display: flex;
	align-items: center;
}

.monaco-editor .find-widget > .replace-part .replace-actions {
	height: 25px;
	display: flex;
	align-items: center;
}

.monaco-editor .find-widget .monaco-findInput {
	vertical-align: middle;
	display: flex;
	flex:1;
}

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element {
	/* Make sure textarea inherits the width correctly */
	width: 100%;
}

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element .scrollbar.vertical {
	/* Hide vertical scrollbar */
	opacity: 0;
}

.monaco-editor .find-widget .matchesCount {
	display: flex;
	flex: initial;
	margin: 0 0 0 3px;
	padding: 2px 0 0 2px;
	height: 25px;
	vertical-align: middle;
	box-sizing: border-box;
	text-align: center;
	line-height: 23px;
}

.monaco-editor .find-widget .button {
	width: 16px;
	height: 16px;
	padding: 3px;
	border-radius: 5px;
	display: flex;
	flex: initial;
	margin-left: 3px;
	background-position: center center;
	background-repeat: no-repeat;
	cursor: pointer;
	display: flex;
	align-items: center;
	justify-content: center;
}

/* find in selection button */
.monaco-editor .find-widget .codicon-find-selection {
	width: 22px;
	height: 22px;
	padding: 3px;
	border-radius: 5px;
}

.monaco-editor .find-widget .button.left {
	margin-left: 0;
	margin-right: 3px;
}

.monaco-editor .find-widget .button.wide {
	width: auto;
	padding: 1px 6px;
	top: -1px;
}

.monaco-editor .find-widget .button.toggle {
	position: absolute;
	top: 0;
	left: 3px;
	width: 18px;
	height: 100%;
	border-radius: 0;
	box-sizing: border-box;
}

.monaco-editor .find-widget .button.toggle.disabled {
	display: none;
}

.monaco-editor .find-widget .disabled {
	color: var(--vscode-disabledForeground);
	cursor: default;
}

.monaco-editor .find-widget > .replace-part {
	display: none;
}

.monaco-editor .find-widget > .replace-part > .monaco-findInput {
	position: relative;
	display: flex;
	vertical-align: middle;
	flex: auto;
	flex-grow: 0;
	flex-shrink: 0;
}

.monaco-editor .find-widget > .replace-part > .monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

/* REDUCED */
.monaco-editor .find-widget.reduced-find-widget .matchesCount {
	display:none;
}

/* NARROW (SMALLER THAN REDUCED) */
.monaco-editor .find-widget.narrow-find-widget {
	max-width: 257px !important;
}

/* COLLAPSED (SMALLER THAN NARROW) */
.monaco-editor .find-widget.collapsed-find-widget {
	max-width: 170px !important;
}

.monaco-editor .find-widget.collapsed-find-widget .button.previous,
.monaco-editor .find-widget.collapsed-find-widget .button.next,
.monaco-editor .find-widget.collapsed-find-widget .button.replace,
.monaco-editor .find-widget.collapsed-find-widget .button.replace-all,
.monaco-editor .find-widget.collapsed-find-widget > .find-part .monaco-findInput .controls {
	display:none;
}

.monaco-editor .findMatch {
	animation-duration: 0;
	animation-name: inherit !important;
}

.monaco-editor .find-widget .monaco-sash {
	left: 0 !important;
}

.monaco-editor.hc-black .find-widget .button:before {
	position: relative;
	top: 1px;
	left: 2px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-action-bar {
	white-space: nowrap;
	height: 100%;
}

.monaco-action-bar .actions-container {
	display: flex;
	margin: 0 auto;
	padding: 0;
	height: 100%;
	width: 100%;
	align-items: center;
}

.monaco-action-bar.vertical .actions-container {
	display: inline-block;
}

.monaco-action-bar .action-item {
	display: block;
	align-items: center;
	justify-content: center;
	cursor: pointer;
	position: relative;  /* DO NOT REMOVE - this is the key to preventing the ghosting icon bug in Chrome 42 */
}

.monaco-action-bar .action-item.disabled {
	cursor: default;
}

.monaco-action-bar .action-item .icon,
.monaco-action-bar .action-item .codicon {
	display: block;
}

.monaco-action-bar .action-item .codicon {
	display: flex;
	align-items: center;
	width: 16px;
	height: 16px;
}

.monaco-action-bar .action-label {
	font-size: 11px;
	padding: 3px;
	border-radius: 5px;
}

.monaco-action-bar .action-item.disabled .action-label,
.monaco-action-bar .action-item.disabled .action-label::before,
.monaco-action-bar .action-item.disabled .action-label:hover {
	opacity: 0.6;
}

/* Vertical actions */

.monaco-action-bar.vertical {
	text-align: left;
}

.monaco-action-bar.vertical .action-item {
	display: block;
}

.monaco-action-bar.vertical .action-label.separator {
	display: block;
	border-bottom: 1px solid #bbb;
	padding-top: 1px;
	margin-left: .8em;
	margin-right: .8em;
}

.monaco-action-bar .action-item .action-label.separator {
	width: 1px;
	height: 16px;
	margin: 5px 4px !important;
	cursor: default;
	min-width: 1px;
	padding: 0;
	background-color: #bbb;
}

.secondary-actions .monaco-action-bar .action-label {
	margin-left: 6px;
}

/* Action Items */
.monaco-action-bar .action-item.select-container {
	overflow: hidden; /* somehow the dropdown overflows its container, we prevent it here to not push */
	flex: 1;
	max-width: 170px;
	min-width: 60px;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-right: 10px;
}

.monaco-action-bar .action-item.action-dropdown-item {
	display: flex;
}

.monaco-action-bar .action-item.action-dropdown-item > .action-label {
	margin-right: 1px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-inputbox {
	position: relative;
	display: block;
	padding: 0;
	box-sizing:	border-box;

	/* Customizable */
	font-size: inherit;
}

.monaco-inputbox.idle {
	border: 1px solid transparent;
}

.monaco-inputbox > .ibwrapper > .input,
.monaco-inputbox > .ibwrapper > .mirror {

	/* Customizable */
	padding: 4px;
}

.monaco-inputbox > .ibwrapper {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-inputbox > .ibwrapper > .input {
	display: inline-block;
	box-sizing:	border-box;
	width: 100%;
	height: 100%;
	line-height: inherit;
	border: none;
	font-family: inherit;
	font-size: inherit;
	resize: none;
	color: inherit;
}

.monaco-inputbox > .ibwrapper > input {
	text-overflow: ellipsis;
}

.monaco-inputbox > .ibwrapper > textarea.input {
	display: block;
	-ms-overflow-style: none; /* IE 10+: hide scrollbars */
	scrollbar-width: none; /* Firefox: hide scrollbars */
	outline: none;
}

.monaco-inputbox > .ibwrapper > textarea.input::-webkit-scrollbar {
	display: none; /* Chrome + Safari: hide scrollbar */
}

.monaco-inputbox > .ibwrapper > textarea.input.empty {
	white-space: nowrap;
}

.monaco-inputbox > .ibwrapper > .mirror {
	position: absolute;
	display: inline-block;
	width: 100%;
	top: 0;
	left: 0;
	box-sizing: border-box;
	white-space: pre-wrap;
	visibility: hidden;
	word-wrap: break-word;
}

/* Context view */

.monaco-inputbox-container {
	text-align: right;
}

.monaco-inputbox-container .monaco-inputbox-message {
	display: inline-block;
	overflow: hidden;
	text-align: left;
	width: 100%;
	box-sizing:	border-box;
	padding: 0.4em;
	font-size: 12px;
	line-height: 17px;
	margin-top: -1px;
	word-wrap: break-word;
}

/* Action bar support */
.monaco-inputbox .monaco-action-bar {
	position: absolute;
	right: 2px;
	top: 4px;
}

.monaco-inputbox .monaco-action-bar .action-item {
	margin-left: 2px;
}

.monaco-inputbox .monaco-action-bar .action-item .codicon {
	background-repeat: no-repeat;
	width: 16px;
	height: 16px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- Find input ---------- */

.monaco-findInput {
	position: relative;
}

.monaco-findInput .monaco-inputbox {
	font-size: 13px;
	width: 100%;
}

.monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

.vs .monaco-findInput.disabled {
	background-color: #E1E1E1;
}

/* Theming */
.vs-dark .monaco-findInput.disabled {
	background-color: #333;
}

/* Highlighting */
.monaco-findInput.highlight-0 .controls,
.hc-light .monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-0 100ms linear 0s;
}

.monaco-findInput.highlight-1 .controls,
.hc-light .monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-1 100ms linear 0s;
}

.hc-black .monaco-findInput.highlight-0 .controls,
.vs-dark  .monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-dark-0 100ms linear 0s;
}

.hc-black .monaco-findInput.highlight-1 .controls,
.vs-dark  .monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-dark-1 100ms linear 0s;
}

@keyframes monaco-findInput-highlight-0 {
	0% { background: rgba(253, 255, 0, 0.8); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-1 {
	0% { background: rgba(253, 255, 0, 0.8); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}

@keyframes monaco-findInput-highlight-dark-0 {
	0% { background: rgba(255, 255, 255, 0.44); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-dark-1 {
	0% { background: rgba(255, 255, 255, 0.44); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .margin-view-overlays .codicon-folding-manual-collapsed,
.monaco-editor .margin-view-overlays .codicon-folding-manual-expanded,
.monaco-editor .margin-view-overlays .codicon-folding-expanded,
.monaco-editor .margin-view-overlays .codicon-folding-collapsed {
	cursor: pointer;
	opacity: 0;
	transition: opacity 0.5s;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 140%;
	margin-left: 2px;
}

.monaco-editor .margin-view-overlays:hover .codicon,
.monaco-editor .margin-view-overlays .codicon.codicon-folding-collapsed,
.monaco-editor .margin-view-overlays .codicon.codicon-folding-manual-collapsed,
.monaco-editor .margin-view-overlays .codicon.alwaysShowFoldIcons {
	opacity: 1;
}

.monaco-editor .inline-folded:after {
	color: grey;
	margin: 0.1em 0.2em 0 0.2em;
	content: "⋯";
	display: inline;
	line-height: 1em;
	cursor: pointer;
}

</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .goto-definition-link {
	text-decoration: underline;
	cursor: pointer;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .peekview-widget .head {
	box-sizing: border-box;
	display: flex;
	justify-content: space-between;
	flex-wrap: nowrap;
}

.monaco-editor .peekview-widget .head .peekview-title {
	display: flex;
	align-items: center;
	font-size: 13px;
	margin-left: 20px;
	min-width: 0;
	text-overflow: ellipsis;
	overflow: hidden;
}

.monaco-editor .peekview-widget .head .peekview-title.clickable {
	cursor: pointer;
}

.monaco-editor .peekview-widget .head .peekview-title .dirname:not(:empty) {
	font-size: 0.9em;
	margin-left: 0.5em;
	text-overflow: ellipsis;
	overflow: hidden;
}

.monaco-editor .peekview-widget .head .peekview-title .meta {
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}

.monaco-editor .peekview-widget .head .peekview-title .dirname {
	white-space: nowrap;
}

.monaco-editor .peekview-widget .head .peekview-title .filename {
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .peekview-widget .head .peekview-title .meta:not(:empty)::before {
	content: '-';
	padding: 0 0.3em;
}

.monaco-editor .peekview-widget .head .peekview-actions {
	flex: 1;
	text-align: right;
	padding-right: 2px;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar {
	display: inline-block;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar,
.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar > .actions-container {
	height: 100%;
}

.monaco-editor .peekview-widget > .body {
	border-top: 1px solid;
	position: relative;
}

.monaco-editor .peekview-widget .head .peekview-title .codicon {
	margin-right: 4px;
}

.monaco-editor .peekview-widget .monaco-list .monaco-list-row.focused .codicon {
	color: inherit !important;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .zone-widget {
	position: absolute;
	z-index: 10;
}


.monaco-editor .zone-widget .zone-widget-container {
	border-top-style: solid;
	border-bottom-style: solid;
	border-top-width: 0;
	border-bottom-width: 0;
	position: relative;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-dropdown {
	height: 100%;
	padding: 0;
}

.monaco-dropdown > .dropdown-label {
	cursor: pointer;
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.monaco-dropdown > .dropdown-label > .action-label.disabled {
	cursor: default;
}

.monaco-dropdown-with-primary {
	display: flex !important;
	flex-direction: row;
	border-radius: 5px;
}

.monaco-dropdown-with-primary > .action-container > .action-label {
	margin-right: 0;
}

.monaco-dropdown-with-primary > .dropdown-action-container > .monaco-dropdown > .dropdown-label .codicon[class*='codicon-'] {
	font-size: 12px;
	padding-left: 0px;
	padding-right: 0px;
	line-height: 16px;
	margin-left: -3px;
}

.monaco-dropdown-with-primary > .dropdown-action-container > .monaco-dropdown > .dropdown-label > .action-label {
	display: block;
	background-size: 16px;
	background-position: center center;
	background-repeat: no-repeat;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-action-bar .action-item.menu-entry .action-label.icon {
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	background-position: 50%;
	background-size: 16px;
}


.monaco-dropdown-with-default {
	display: flex !important;
	flex-direction: row;
	border-radius: 5px;
}

.monaco-dropdown-with-default > .action-container > .action-label {
	margin-right: 0;
}

.monaco-dropdown-with-default > .action-container.menu-entry > .action-label.icon {
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	background-position: 50%;
	background-size: 16px;
}

.monaco-dropdown-with-default > .dropdown-action-container > .monaco-dropdown > .dropdown-label .codicon[class*='codicon-'] {
	font-size: 12px;
	padding-left: 0px;
	padding-right: 0px;
	line-height: 16px;
	margin-left: -3px;
}

.monaco-dropdown-with-default > .dropdown-action-container > .monaco-dropdown > .dropdown-label > .action-label {
	display: block;
	background-size: 16px;
	background-position: center center;
	background-repeat: no-repeat;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-list {
	position: relative;
	height: 100%;
	width: 100%;
	white-space: nowrap;
}

.monaco-list.mouse-support {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-list > .monaco-scrollable-element {
	height: 100%;
}

.monaco-list-rows {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-list.horizontal-scrolling .monaco-list-rows {
	width: auto;
	min-width: 100%;
}

.monaco-list-row {
	position: absolute;
	box-sizing: border-box;
	overflow: hidden;
	width: 100%;
}

.monaco-list.mouse-support .monaco-list-row {
	cursor: pointer;
	touch-action: none;
}

/* for OS X ballistic scrolling */
.monaco-list-row.scrolling {
	display: none !important;
}

/* Focus */
.monaco-list.element-focused,
.monaco-list.selection-single,
.monaco-list.selection-multiple {
	outline: 0 !important;
}

/* Dnd */
.monaco-drag-image {
	display: inline-block;
	padding: 1px 7px;
	border-radius: 10px;
	font-size: 12px;
	position: absolute;
	z-index: 1000;
}

/* Filter */

.monaco-list-type-filter-message {
	position: absolute;
	box-sizing: border-box;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	padding: 40px 1em 1em 1em;
	text-align: center;
	white-space: normal;
	opacity: 0.7;
	pointer-events: none;
}

.monaco-list-type-filter-message:empty {
	display: none;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-split-view2 {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-split-view2 > .sash-container {
	position: absolute;
	width: 100%;
	height: 100%;
	pointer-events: none;
}

.monaco-split-view2 > .sash-container > .monaco-sash {
	pointer-events: initial;
}

.monaco-split-view2 > .monaco-scrollable-element {
	width: 100%;
	height: 100%;
}

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container {
	width: 100%;
	height: 100%;
	white-space: nowrap;
	position: relative;
}

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container > .split-view-view {
	white-space: initial;
	position: absolute;
}

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container > .split-view-view:not(.visible) {
	display: none;
}

.monaco-split-view2.vertical > .monaco-scrollable-element > .split-view-container > .split-view-view {
	width: 100%;
}

.monaco-split-view2.horizontal > .monaco-scrollable-element > .split-view-container > .split-view-view {
	height: 100%;
}

.monaco-split-view2.separator-border > .monaco-scrollable-element > .split-view-container > .split-view-view:not(:first-child)::before {
	content: ' ';
	position: absolute;
	top: 0;
	left: 0;
	z-index: 5;
	pointer-events: none;
	background-color: var(--separator-border);
}

.monaco-split-view2.separator-border.horizontal > .monaco-scrollable-element > .split-view-container > .split-view-view:not(:first-child)::before {
	height: 100%;
	width: 1px;
}

.monaco-split-view2.separator-border.vertical > .monaco-scrollable-element > .split-view-container > .split-view-view:not(:first-child)::before {
	height: 1px;
	width: 100%;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-table {
	display: flex;
	flex-direction: column;
	position: relative;
	height: 100%;
	width: 100%;
	white-space: nowrap;
}

.monaco-table > .monaco-split-view2 {
	border-bottom: 1px solid transparent;
}

.monaco-table > .monaco-list {
	flex: 1;
}

.monaco-table-tr {
	display: flex;
	height: 100%;
}

.monaco-table-th {
	width: 100%;
	height: 100%;
	font-weight: bold;
	overflow: hidden;
	text-overflow: ellipsis;
}

.monaco-table-th,
.monaco-table-td {
	box-sizing: border-box;
	flex-shrink: 0;
	overflow: hidden;
	white-space: nowrap;
	text-overflow: ellipsis;
}

.monaco-table > .monaco-split-view2 .monaco-sash.vertical::before {
	content: "";
	position: absolute;
	left: calc(var(--sash-size) / 2);
	width: 0;
	border-left: 1px solid transparent;
}

.monaco-table > .monaco-split-view2,
.monaco-table > .monaco-split-view2 .monaco-sash.vertical::before {
	transition: border-color 0.2s ease-out;
}
/*
.monaco-table:hover > .monaco-split-view2,
.monaco-table:hover > .monaco-split-view2 .monaco-sash.vertical::before {
	border-color: rgba(204, 204, 204, 0.2);
} */
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-tl-row {
	display: flex;
	height: 100%;
	align-items: center;
	position: relative;
}

.monaco-tl-indent {
	height: 100%;
	position: absolute;
	top: 0;
	left: 16px;
	pointer-events: none;
}

.hide-arrows .monaco-tl-indent {
	left: 12px;
}

.monaco-tl-indent > .indent-guide {
	display: inline-block;
	box-sizing: border-box;
	height: 100%;
	border-left: 1px solid transparent;
}

.monaco-tl-indent > .indent-guide {
	transition: border-color 0.1s linear;
}

.monaco-tl-twistie,
.monaco-tl-contents {
	height: 100%;
}

.monaco-tl-twistie {
	font-size: 10px;
	text-align: right;
	padding-right: 6px;
	flex-shrink: 0;
	width: 16px;
	display: flex !important;
	align-items: center;
	justify-content: center;
	transform: translateX(3px);
}

.monaco-tl-contents {
	flex: 1;
	overflow: hidden;
}

.monaco-tl-twistie::before {
	border-radius: 20px;
}

.monaco-tl-twistie.collapsed::before {
	transform: rotate(-90deg);
}

.monaco-tl-twistie.codicon-tree-item-loading::before {
	/* Use steps to throttle FPS to reduce CPU usage */
	animation: codicon-spin 1.25s steps(30) infinite;
}

.monaco-tree-type-filter {
	position: absolute;
	top: 0;
	display: flex;
	padding: 3px;
	transition: top 0.3s;
	max-width: 200px;
	z-index: 100;
	margin: 0 6px;
}

.monaco-tree-type-filter.disabled {
	top: -40px;
}

.monaco-tree-type-filter-grab {
	display: flex !important;
	align-items: center;
	justify-content: center;
	cursor: grab;
	margin-right: 2px;
}

.monaco-tree-type-filter-grab.grabbing {
	cursor: grabbing;
}

.monaco-tree-type-filter-input {
	flex: 1;
}

.monaco-tree-type-filter-input .monaco-inputbox {
	height: 23px;
}

.monaco-tree-type-filter-input .monaco-inputbox > .ibwrapper > .input,
.monaco-tree-type-filter-input .monaco-inputbox > .ibwrapper > .mirror {
	padding: 2px 4px;
}

.monaco-tree-type-filter-input .monaco-findInput > .controls {
	top: 2px;
}

.monaco-tree-type-filter-actionbar {
	margin-left: 4px;
}

.monaco-tree-type-filter-actionbar .monaco-action-bar .action-label {
	padding: 2px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -- zone widget */
.monaco-editor .zone-widget .zone-widget-container.reference-zone-widget {
	border-top-width: 1px;
	border-bottom-width: 1px;
}

.monaco-editor .reference-zone-widget .inline {
	display: inline-block;
	vertical-align: top;
}

.monaco-editor .reference-zone-widget .messages {
	height: 100%;
	width: 100%;
	text-align: center;
	padding: 3em 0;
}

.monaco-editor .reference-zone-widget .ref-tree {
	line-height: 23px;
	background-color: var(--vscode-peekViewResult-background);
	color: var(--vscode-peekViewResult-lineForeground);
}

.monaco-editor .reference-zone-widget .ref-tree .reference {
	text-overflow: ellipsis;
	overflow: hidden;
}

.monaco-editor .reference-zone-widget .ref-tree .reference-file {
	display: inline-flex;
	width: 100%;
	height: 100%;
	color: var(--vscode-peekViewResult-fileForeground);
}

.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .selected .reference-file {
	color: inherit !important;
}

.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .monaco-list-rows > .monaco-list-row.selected:not(.highlighted) {
	background-color: var(--vscode-peekViewResult-selectionBackground);
	color: var(--vscode-peekViewResult-selectionForeground) !important;
}

.monaco-editor .reference-zone-widget .ref-tree .reference-file .count {
	margin-right: 12px;
	margin-left: auto;
}

.monaco-editor .reference-zone-widget .ref-tree .referenceMatch .highlight {
	background-color: var(--vscode-peekViewResult-matchHighlightBackground);
}

.monaco-editor .reference-zone-widget .preview .reference-decoration {
	background-color: var(--vscode-peekViewEditor-matchHighlightBackground);
	border: 2px solid var(--vscode-peekViewEditor-matchHighlightBorder);
	box-sizing: border-box;
}

.monaco-editor .reference-zone-widget .preview .monaco-editor .monaco-editor-background,
.monaco-editor .reference-zone-widget .preview .monaco-editor .inputarea.ime-input {
	background-color: var(--vscode-peekViewEditor-background);
}

.monaco-editor .reference-zone-widget .preview .monaco-editor .margin {
	background-color: var(--vscode-peekViewEditorGutter-background);
}

/* High Contrast Theming */

.monaco-editor.hc-black .reference-zone-widget .ref-tree .reference-file,
.monaco-editor.hc-light .reference-zone-widget .ref-tree .reference-file {
	font-weight: bold;
}

.monaco-editor.hc-black .reference-zone-widget .ref-tree .referenceMatch .highlight,
.monaco-editor.hc-light .reference-zone-widget .ref-tree .referenceMatch .highlight {
	border: 1px dotted var(--vscode-contrastActiveBorder, transparent);
	box-sizing: border-box;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-count-badge {
	padding: 3px 6px;
	border-radius: 11px;
	font-size: 11px;
	min-width: 18px;
	min-height: 18px;
	line-height: 11px;
	font-weight: normal;
	text-align: center;
	display: inline-block;
	box-sizing: border-box;
}

.monaco-count-badge.long {
	padding: 2px 3px;
	border-radius: 2px;
	min-height: auto;
	line-height: normal;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* ---------- Icon label ---------- */

.monaco-icon-label {
	display: flex; /* required for icons support :before rule */
	overflow: hidden;
	text-overflow: ellipsis;
}

.monaco-icon-label::before {

	/* svg icons rendered as background image */
	background-size: 16px;
	background-position: left center;
	background-repeat: no-repeat;
	padding-right: 6px;
	width: 16px;
	height: 22px;
	line-height: inherit !important;
	display: inline-block;

	/* fonts icons */
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	vertical-align: top;

	flex-shrink: 0; /* fix for https://github.com/microsoft/vscode/issues/13787 */
}

.monaco-icon-label > .monaco-icon-label-container {
	min-width: 0;
	overflow: hidden;
	text-overflow: ellipsis;
	flex: 1;
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-container > .label-name {
	color: inherit;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-container > .label-name > .label-separator {
	margin: 0 2px;
	opacity: 0.5;
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	opacity: .7;
	margin-left: 0.5em;
	font-size: 0.9em;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label.nowrap > .monaco-icon-label-container > .monaco-icon-description-container > .label-description{
	white-space: nowrap
}

.vs .monaco-icon-label > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	opacity: .95;
}

.monaco-icon-label.italic > .monaco-icon-label-container > .monaco-icon-name-container > .label-name,
.monaco-icon-label.italic > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	font-style: italic;
}

.monaco-icon-label.deprecated {
	text-decoration: line-through;
	opacity: 0.66;
}

/* make sure apply italic font style to decorations as well */
.monaco-icon-label.italic::after {
	font-style: italic;
}

.monaco-icon-label.strikethrough > .monaco-icon-label-container > .monaco-icon-name-container > .label-name,
.monaco-icon-label.strikethrough > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	text-decoration: line-through;
}

.monaco-icon-label::after {
	opacity: 0.75;
	font-size: 90%;
	font-weight: 600;
	margin: auto 16px 0 5px; /* https://github.com/microsoft/vscode/issues/113223 */
	text-align: center;
}

/* make sure selection color wins when a label is being selected */
.monaco-list:focus .selected .monaco-icon-label, /* list */
.monaco-list:focus .selected .monaco-icon-label::after
{
	color: inherit !important;
}

.monaco-list-row.focused.selected .label-description,
.monaco-list-row.selected .label-description {
	opacity: .8;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .monaco-editor-overlaymessage {
	padding-bottom: 8px;
	z-index: 10000;
}

.monaco-editor .monaco-editor-overlaymessage.below {
	padding-bottom: 0;
	padding-top: 8px;
	z-index: 10000;
}

@keyframes fadeIn {
	from { opacity: 0; }
	to { opacity: 1; }
}
.monaco-editor .monaco-editor-overlaymessage.fadeIn {
	animation: fadeIn 150ms ease-out;
}

@keyframes fadeOut {
	from { opacity: 1; }
	to { opacity: 0; }
}
.monaco-editor .monaco-editor-overlaymessage.fadeOut {
	animation: fadeOut 100ms ease-out;
}

.monaco-editor .monaco-editor-overlaymessage .message {
	padding: 1px 4px;
	color: var(--vscode-inputValidation-infoForeground);
	background-color: var(--vscode-inputValidation-infoBackground);
	border: 1px solid var(--vscode-inputValidation-infoBorder);
}

.monaco-editor.hc-black .monaco-editor-overlaymessage .message,
.monaco-editor.hc-light .monaco-editor-overlaymessage .message {
	border-width: 2px;
}

.monaco-editor .monaco-editor-overlaymessage .anchor {
	width: 0 !important;
	height: 0 !important;
	border-color: transparent;
	border-style: solid;
	z-index: 1000;
	border-width: 8px;
	position: absolute;
}

.monaco-editor .monaco-editor-overlaymessage .anchor.top {
	border-bottom-color: var(--vscode-inputValidation-infoBorder);
}

.monaco-editor .monaco-editor-overlaymessage .anchor.below {
	border-top-color: var(--vscode-inputValidation-infoBorder);
}

.monaco-editor .monaco-editor-overlaymessage:not(.below) .anchor.top,
.monaco-editor .monaco-editor-overlaymessage.below .anchor.below {
	display: none;
}

.monaco-editor .monaco-editor-overlaymessage.below .anchor.top {
	display: inherit;
	top: -8px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-hover {
	cursor: default;
	position: absolute;
	overflow: hidden;
	z-index: 50;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	box-sizing: initial;
	animation: fadein 100ms linear;
	line-height: 1.5em;
}

.monaco-hover.hidden {
	display: none;
}

.monaco-hover a:hover {
	cursor: pointer;
}

.monaco-hover .hover-contents:not(.html-hover-contents) {
	padding: 4px 8px;
}

.monaco-hover .markdown-hover > .hover-contents:not(.code-hover-contents) {
	max-width: 500px;
	word-wrap: break-word;
}

.monaco-hover .markdown-hover > .hover-contents:not(.code-hover-contents) hr {
	min-width: 100%;
}

.monaco-hover p,
.monaco-hover .code,
.monaco-hover ul {
	margin: 8px 0;
}

.monaco-hover code {
	font-family: var(--monaco-monospace-font);
}

.monaco-hover hr {
	box-sizing: border-box;
	border-left: 0px;
	border-right: 0px;
	margin-top: 4px;
	margin-bottom: -4px;
	margin-left: -8px;
	margin-right: -8px;
	height: 1px;
}

.monaco-hover p:first-child,
.monaco-hover .code:first-child,
.monaco-hover ul:first-child {
	margin-top: 0;
}

.monaco-hover p:last-child,
.monaco-hover .code:last-child,
.monaco-hover ul:last-child {
	margin-bottom: 0;
}

/* MarkupContent Layout */
.monaco-hover ul {
	padding-left: 20px;
}
.monaco-hover ol {
	padding-left: 20px;
}

.monaco-hover li > p {
	margin-bottom: 0;
}

.monaco-hover li > ul {
	margin-top: 0;
}

.monaco-hover code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-hover .monaco-tokenized-source {
	white-space: pre-wrap;
}

.monaco-hover .hover-row.status-bar {
	font-size: 12px;
	line-height: 22px;
}

.monaco-hover .hover-row.status-bar .actions {
	display: flex;
	padding: 0px 8px;
}

.monaco-hover .hover-row.status-bar .actions .action-container {
	margin-right: 16px;
	cursor: pointer;
}

.monaco-hover .hover-row.status-bar .actions .action-container .action .icon {
	padding-right: 4px;
}

.monaco-hover .markdown-hover .hover-contents .codicon {
	color: inherit;
	font-size: inherit;
	vertical-align: middle;
}

.monaco-hover .hover-contents a.code-link:hover,
.monaco-hover .hover-contents a.code-link {
	color: inherit;
}

.monaco-hover .hover-contents a.code-link:before {
	content: '(';
}

.monaco-hover .hover-contents a.code-link:after {
	content: ')';
}

.monaco-hover .hover-contents a.code-link > span {
	text-decoration: underline;
	/** Hack to force underline to show **/
	border-bottom: 1px solid transparent;
	text-underline-position: under;
}

/** Spans in markdown hovers need a margin-bottom to avoid looking cramped: https://github.com/microsoft/vscode/issues/101496 **/
.monaco-hover .markdown-hover .hover-contents:not(.code-hover-contents):not(.html-hover-contents) span {
	margin-bottom: 4px;
	display: inline-block;
}

.monaco-hover-content .action-container a {
	-webkit-user-select: none;
	user-select: none;
}

.monaco-hover-content .action-container.disabled {
	pointer-events: none;
	opacity: 0.4;
	cursor: default;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.codeActionMenuWidget {
	padding: 8px 0px 8px 0px;
	overflow: auto;
	font-size: 13px;
	border-radius: 5px;
	min-width: 160px;
	z-index: 40;
	display: block;
	/* flex-direction: column;
	flex: 0 1 auto; */
	width: 100%;
	border-width: 0px;
	border-color: none;
	background-color: var(--vscode-menu-background);
	color: var(--vscode-menu-foreground);
	box-shadow: rgb(0,0,0, 16%) 0px 2px 8px;
}

.codeActionMenuWidget .monaco-list:not(.element-focused):focus:before {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 5; /* make sure we are on top of the tree items */
	content: "";
	pointer-events: none; /* enable click through */
	outline: 0px solid !important; /* we still need to handle the empty tree or no focus item case */
	outline-width: 0px !important;
	outline-style: none !important;
	outline-offset: 0px !important;
}

.codeActionMenuWidget .monaco-list {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
	border: none !important;
	border-width: 0px !important;
}

/* .codeActionMenuWidget .monaco-list:not(.element-focus) {
	border: none !important;
	border-width: 0px !important;
} */

.codeActionMenuWidget .monaco-list .monaco-scrollable-element .monaco-list-rows {
	height: 100% !important;
}

.codeActionMenuWidget .monaco-list .monaco-scrollable-element {
	overflow: visible;
}
/** Styles for each row in the list element **/

.codeActionMenuWidget .monaco-list .monaco-list-row:not(.separator) {
	display: flex;
	-mox-box-sizing: border-box;
	box-sizing: border-box;
	padding: 0px 26px 0px 26px;
	background-repeat: no-repeat;
	background-position: 2px 2px;
	white-space: nowrap;
	cursor: pointer;
	touch-action: none;
	width: 100%;
}


.codeActionMenuWidget .monaco-list .monaco-list-row:hover:not(.option-disabled),
.codeActionMenuWidget .monaco-list .moncao-list-row.focused:not(.option-disabled) {
	color: var(--vscode-menu-selectionForeground) !important;
	background-color: var(--vscode-menu-selectionBackground) !important;
}

.codeActionMenuWidget .monaco-list .option-disabled,
.codeActionMenuWidget .monaco-list .option-disabled .focused {
	pointer-events: none;
	-webkit-touch-callout: none;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	color: var(--vscode-disabledForeground) !important;
}

.codeActionMenuWidget .monaco-list .separator {
	border-bottom: 1px solid var(--vscode-menu-separatorBackground);
	padding-top: 0px !important;
	/* padding: 30px; */
	width: 100%;
	height: 0px !important;
	opacity: 1;
	font-size: inherit;
	margin: 5px 0 !important;
	border-radius: 0;
	display: flex;
	-mox-box-sizing: border-box;
	box-sizing: border-box;
	background-repeat: no-repeat;
	background-position: 2px 2px;
	white-space: nowrap;
	cursor: pointer;
	touch-action: none;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .contentWidgets .codicon-light-bulb,
.monaco-editor .contentWidgets .codicon-lightbulb-autofix {
	display: flex;
	align-items: center;
	justify-content: center;
}

.monaco-editor .contentWidgets .codicon-light-bulb:hover,
.monaco-editor .contentWidgets .codicon-lightbulb-autofix:hover {
	cursor: pointer;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* marker zone */

.monaco-editor .peekview-widget .head .peekview-title .severity-icon {
	display: inline-block;
	vertical-align: text-top;
	margin-right: 4px;
}

.monaco-editor .marker-widget {
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .marker-widget > .stale {
	opacity: 0.6;
	font-style: italic;
}

.monaco-editor .marker-widget .title {
	display: inline-block;
	padding-right: 5px;
}

.monaco-editor .marker-widget .descriptioncontainer {
	position: absolute;
	white-space: pre;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	padding: 8px 12px 0 20px;
}

.monaco-editor .marker-widget .descriptioncontainer .message {
	display: flex;
	flex-direction: column;
}

.monaco-editor .marker-widget .descriptioncontainer .message .details {
	padding-left: 6px;
}

.monaco-editor .marker-widget .descriptioncontainer .message .source,
.monaco-editor .marker-widget .descriptioncontainer .message span.code {
	opacity: 0.6;
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link {
	opacity: 0.6;
	color: inherit;
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link:before {
	content: '(';
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link:after {
	content: ')';
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link > span {
	text-decoration: underline;
	/** Hack to force underline to show **/
	border-bottom: 1px solid transparent;
	text-underline-position: under;
	color: var(--vscode-textLink-foreground);
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link > span {
	color: var(--vscode-textLink-activeForeground);
}

.monaco-editor .marker-widget .descriptioncontainer .filename {
	cursor: pointer;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .detected-link,
.monaco-editor .detected-link-active {
	text-decoration: underline;
	text-underline-position: under;
}

.monaco-editor .detected-link-active {
	cursor: pointer;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .parameter-hints-widget {
	/* Must be higher than the sash's z-index and terminal canvases but lower than the suggest widget */
	z-index: 39;
	display: flex;
	flex-direction: column;
	line-height: 1.5em;
	cursor: default;
}

.monaco-editor .parameter-hints-widget > .phwrapper {
	max-width: 440px;
	display: flex;
	flex-direction: row;
}

.monaco-editor .parameter-hints-widget.multiple {
	min-height: 3.3em;
	padding: 0;
}

.monaco-editor .parameter-hints-widget.visible {
	transition: left .05s ease-in-out;
}

.monaco-editor .parameter-hints-widget p,
.monaco-editor .parameter-hints-widget ul {
	margin: 8px 0;
}

.monaco-editor .parameter-hints-widget .monaco-scrollable-element,
.monaco-editor .parameter-hints-widget .body {
	display: flex;
	flex: 1;
	flex-direction: column;
	min-height: 100%;
}

.monaco-editor .parameter-hints-widget .signature {
	padding: 4px 5px;
}

.monaco-editor .parameter-hints-widget .docs {
	padding: 0 10px 0 5px;
	white-space: pre-wrap;
}

.monaco-editor .parameter-hints-widget .docs.empty {
	display: none;
}

.monaco-editor .parameter-hints-widget .docs .markdown-docs {
	white-space: initial;
}

.monaco-editor .parameter-hints-widget .docs .markdown-docs a:hover {
	cursor: pointer;
}

.monaco-editor .parameter-hints-widget .docs .markdown-docs code {
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .parameter-hints-widget .docs  .monaco-tokenized-source,
.monaco-editor .parameter-hints-widget .docs .code {
	white-space: pre-wrap;
}

.monaco-editor .parameter-hints-widget .docs code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-editor .parameter-hints-widget .controls {
	display: none;
	flex-direction: column;
	align-items: center;
	min-width: 22px;
	justify-content: flex-end;
}

.monaco-editor .parameter-hints-widget.multiple .controls {
	display: flex;
	padding: 0 2px;
}

.monaco-editor .parameter-hints-widget.multiple .button {
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	cursor: pointer;
}

.monaco-editor .parameter-hints-widget .button.previous {
	bottom: 24px;
}

.monaco-editor .parameter-hints-widget .overloads {
	text-align: center;
	height: 12px;
	line-height: 12px;
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .parameter-hints-widget .signature .parameter.active {
	font-weight: bold;
}

.monaco-editor .parameter-hints-widget .documentation-parameter > .parameter {
	font-weight: bold;
	margin-right: 0.5em;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .snippet-placeholder {
	min-width: 2px;
	outline-style: solid;
	outline-width: 1px;
	background-color: var(--vscode-editor-snippetTabstopHighlightBackground, transparent);
	outline-color: var(--vscode-editor-snippetTabstopHighlightBorder, transparent);
}

.monaco-editor .finish-snippet-placeholder {
	outline-style: solid;
	outline-width: 1px;
	background-color: var(--vscode-editor-snippetFinalTabstopHighlightBackground, transparent);
	outline-color: var(--vscode-editor-snippetFinalTabstopHighlightBorder, transparent);
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

@font-face {
	font-family: "codicon";
	font-display: block;
	src: url(https://static.leetcode.cn/lc-monaco/b797181c93b3755f4fa1.ttf) format("truetype");
}

.codicon[class*='codicon-'] {
	font: normal normal normal 16px/1 codicon;
	display: inline-block;
	text-decoration: none;
	text-rendering: auto;
	text-align: center;
	text-transform: none;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

/* icon rules are dynamically created by the platform theme service (see iconsStyleSheet.ts) */
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.codicon-wrench-subaction {
	opacity: 0.5;
}

@keyframes codicon-spin {
	100% {
		transform:rotate(360deg);
	}
}

.codicon-sync.codicon-modifier-spin,
.codicon-loading.codicon-modifier-spin,
.codicon-gear.codicon-modifier-spin,
.codicon-notebook-state-executing.codicon-modifier-spin {
	/* Use steps to throttle FPS to reduce CPU usage */
	animation: codicon-spin 1.5s steps(30) infinite;
}

.codicon-modifier-disabled {
	opacity: 0.4;
}

/* custom speed & easing for loading icon */
.codicon-loading,
.codicon-tree-item-loading::before {
	animation-duration: 1s !important;
	animation-timing-function: cubic-bezier(0.53, 0.21, 0.29, 0.67) !important;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Suggest widget*/

.monaco-editor .suggest-widget {
	width: 430px;
	z-index: 40;
	display: flex;
	flex-direction: column;
}

.monaco-editor .suggest-widget.message {
	flex-direction: row;
	align-items: center;
}

.monaco-editor .suggest-widget,
.monaco-editor .suggest-details {
	flex: 0 1 auto;
	width: 100%;
	border-style: solid;
	border-width: 1px;
	border-color: var(--vscode-editorSuggestWidget-border);
	background-color: var(--vscode-editorSuggestWidget-background);
}

.monaco-editor.hc-black .suggest-widget,
.monaco-editor.hc-black .suggest-details,
.monaco-editor.hc-light .suggest-widget,
.monaco-editor.hc-light .suggest-details {
	border-width: 2px;
}

/* Styles for status bar part */


.monaco-editor .suggest-widget .suggest-status-bar {
	box-sizing: border-box;
	display: none;
	flex-flow: row nowrap;
	justify-content: space-between;
	width: 100%;
	font-size: 80%;
	padding: 0 4px 0 4px;
	border-top: 1px solid var(--vscode-editorSuggestWidget-border);
	overflow: hidden;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar {
	display: flex;
}

.monaco-editor .suggest-widget .suggest-status-bar .left {
	padding-right: 8px;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-label {
	color: var(--vscode-editorSuggestWidgetStatus-foreground);
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-item:not(:last-of-type) .action-label {
	margin-right: 0;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-item:not(:last-of-type) .action-label::after {
	content: ', ';
	margin-right: 0.3em;
}

.monaco-editor .suggest-widget.with-status-bar .monaco-list .monaco-list-row>.contents>.main>.right>.readMore,
.monaco-editor .suggest-widget.with-status-bar .monaco-list .monaco-list-row.focused.string-label>.contents>.main>.right>.readMore {
	display: none;
}

.monaco-editor .suggest-widget.with-status-bar:not(.docs-side) .monaco-list .monaco-list-row:hover>.contents>.main>.right.can-expand-details>.details-label {
	width: 100%;
}

/* Styles for Message element for when widget is loading or is empty */

.monaco-editor .suggest-widget>.message {
	padding-left: 22px;
}

/** Styles for the list element **/

.monaco-editor .suggest-widget>.tree {
	height: 100%;
	width: 100%;
}

.monaco-editor .suggest-widget .monaco-list {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

/** Styles for each row in the list element **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row {
	display: flex;
	-mox-box-sizing: border-box;
	box-sizing: border-box;
	padding-right: 10px;
	background-repeat: no-repeat;
	background-position: 2px 2px;
	white-space: nowrap;
	cursor: pointer;
	touch-action: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused {
	color: var(--vscode-editorSuggestWidget-selectedForeground);
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused .codicon {
	color: var(--vscode-editorSuggestWidget-selectedIconForeground);
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents {
	flex: 1;
	height: 100%;
	overflow: hidden;
	padding-left: 2px;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main {
	display: flex;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: pre;
	justify-content: space-between;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right {
	display: flex;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:not(.focused)>.contents>.main .monaco-icon-label {
	color: var(--vscode-editorSuggestWidget-foreground);
}

.monaco-editor .suggest-widget:not(.frozen) .monaco-highlighted-label .highlight {
	font-weight: bold;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main .monaco-highlighted-label .highlight {
	color: var(--vscode-editorSuggestWidget-highlightForeground);
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused>.contents>.main .monaco-highlighted-label .highlight {
	color: var(--vscode-editorSuggestWidget-focusHighlightForeground);
}

/** ReadMore Icon styles **/

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.codicon-close,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.readMore::before {
	color: inherit;
	opacity: 1;
	font-size: 14px;
	cursor: pointer;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.codicon-close {
	position: absolute;
	top: 6px;
	right: 2px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.codicon-close:hover,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.readMore:hover {
	opacity: 1;
}

/** signature, qualifier, type/details opacity **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label {
	opacity: 0.7;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left>.signature-label {
	overflow: hidden;
	text-overflow: ellipsis;
	opacity: 0.6;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left>.qualifier-label {
	margin-left: 12px;
	opacity: 0.4;
	font-size: 85%;
	line-height: initial;
	text-overflow: ellipsis;
	overflow: hidden;
	align-self: center;
}

/** Type Info and icon next to the label in the focused completion item **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label {
	font-size: 85%;
	margin-left: 1.1em;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label>.monaco-tokenized-source {
	display: inline;
}

/** Details: if using CompletionItem#details, show on focus **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label {
	display: none;
}

.monaco-editor .suggest-widget:not(.shows-details) .monaco-list .monaco-list-row.focused>.contents>.main>.right>.details-label {
	display: inline;
}

/** Details: if using CompletionItemLabel#details, always show **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:not(.string-label)>.contents>.main>.right>.details-label,
.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row.focused:not(.string-label)>.contents>.main>.right>.details-label {
	display: inline;
}

/** Ellipsis on hover **/

.monaco-editor .suggest-widget:not(.docs-side) .monaco-list .monaco-list-row.focused:hover>.contents>.main>.right.can-expand-details>.details-label {
	width: calc(100% - 26px);
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left {
	flex-shrink: 1;
	flex-grow: 1;
	overflow: hidden;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left>.monaco-icon-label {
	flex-shrink: 0;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:not(.string-label)>.contents>.main>.left>.monaco-icon-label {
	max-width: 100%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.string-label>.contents>.main>.left>.monaco-icon-label {
	flex-shrink: 1;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right {
	overflow: hidden;
	flex-shrink: 4;
	max-width: 70%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.readMore {
	display: inline-block;
	position: absolute;
	right: 10px;
	width: 18px;
	height: 18px;
	visibility: hidden;
}

/** Do NOT display ReadMore when docs is side/below **/

.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row>.contents>.main>.right>.readMore {
	display: none !important;
}

/** Do NOT display ReadMore when using plain CompletionItemLabel (details/documentation might not be resolved) **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.string-label>.contents>.main>.right>.readMore {
	display: none;
}

/** Focused item can show ReadMore, but can't when docs is side/below **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused.string-label>.contents>.main>.right>.readMore {
	display: inline-block;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused:hover>.contents>.main>.right>.readMore {
	visibility: visible;
}

/** Styles for each row in the list **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label.deprecated {
	opacity: 0.66;
	text-decoration: unset;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label.deprecated>.monaco-icon-label-container>.monaco-icon-name-container {
	text-decoration: line-through;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label::before {
	height: 100%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon {
	display: block;
	height: 16px;
	width: 16px;
	margin-left: 2px;
	background-repeat: no-repeat;
	background-size: 80%;
	background-position: center;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.hide {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .suggest-icon {
	display: flex;
	align-items: center;
	margin-right: 4px;
}

.monaco-editor .suggest-widget.no-icons .monaco-list .monaco-list-row .icon,
.monaco-editor .suggest-widget.no-icons .monaco-list .monaco-list-row .suggest-icon::before {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.customcolor .colorspan {
	margin: 0 0 0 0.3em;
	border: 0.1em solid #000;
	width: 0.7em;
	height: 0.7em;
	display: inline-block;
}

/** Styles for the docs of the completion item in focus **/

.monaco-editor .suggest-details-container {
	z-index: 41;
}

.monaco-editor .suggest-details {
	display: flex;
	flex-direction: column;
	cursor: default;
	color: var(--vscode-editorSuggestWidget-foreground);
}

.monaco-editor .suggest-details.focused {
	border-color: var(--vscode-focusBorder);
}

.monaco-editor .suggest-details a {
	color: var(--vscode-textLink-foreground);
}

.monaco-editor .suggest-details a:hover {
	color: var(--vscode-textLink-activeForeground);
}

.monaco-editor .suggest-details code {
	background-color: var(--vscode-textCodeBlock-background);
}

.monaco-editor .suggest-details.no-docs {
	display: none;
}

.monaco-editor .suggest-details>.monaco-scrollable-element {
	flex: 1;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body {
	box-sizing: border-box;
	height: 100%;
	width: 100%;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.type {
	flex: 2;
	overflow: hidden;
	text-overflow: ellipsis;
	opacity: 0.7;
	white-space: pre;
	margin: 0 24px 0 0;
	padding: 4px 0 12px 5px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.type.auto-wrap {
	white-space: normal;
	word-break: break-all;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs {
	margin: 0;
	padding: 4px 5px;
	white-space: pre-wrap;
}

.monaco-editor .suggest-details.no-type>.monaco-scrollable-element>.body>.docs {
	margin-right: 24px;
	overflow: hidden;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs {
	padding: 0;
	white-space: initial;
	min-height: calc(1rem + 8px);
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>div,
.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>span:not(:empty) {
	padding: 4px 5px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>div>p:first-child {
	margin-top: 0;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>div>p:last-child {
	margin-bottom: 0;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs .monaco-tokenized-source {
	white-space: pre;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs .code {
	white-space: pre-wrap;
	word-wrap: break-word;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs .codicon {
	vertical-align: sub;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>p:empty {
	display: none;
}

.monaco-editor .suggest-details code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-editor .suggest-details ul {
	padding-left: 20px;
}

.monaco-editor .suggest-details ol {
	padding-left: 20px;
}

.monaco-editor .suggest-details p code {
	font-family: var(--monaco-monospace-font);
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .accessibilityHelpWidget {
	padding: 10px;
	vertical-align: middle;
	overflow: scroll;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .tokens-inspect-widget {
	z-index: 50;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	padding: 10px;
}

.tokens-inspect-separator {
	height: 1px;
	border: 0;
}

.monaco-editor .tokens-inspect-widget .tm-token {
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .tokens-inspect-widget .tm-token-length {
	font-weight: normal;
	font-size: 60%;
	float: right;
}

.monaco-editor .tokens-inspect-widget .tm-metadata-table {
	width: 100%;
}

.monaco-editor .tokens-inspect-widget .tm-metadata-value {
	font-family: var(--monaco-monospace-font);
	text-align: right;
}

.monaco-editor .tokens-inspect-widget .tm-token-type {
	font-family: var(--monaco-monospace-font);
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/


/* Default standalone editor fonts */
.monaco-editor {
	font-family: -apple-system, BlinkMacSystemFont, "Segoe WPC", "Segoe UI", "HelveticaNeue-Light", system-ui, "Ubuntu", "Droid Sans", sans-serif;
	--monaco-monospace-font: "SF Mono", Monaco, Menlo, Consolas, "Ubuntu Mono", "Liberation Mono", "DejaVu Sans Mono", "Courier New", monospace;
}

.monaco-menu .monaco-action-bar.vertical .action-item .action-menu-item:focus .action-label {
	stroke-width: 1.2px;
}

.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
.monaco-editor.hc-black .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
.monaco-editor.hc-light .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label {
	stroke-width: 1.2px;
}

.monaco-hover p {
	margin: 0;
}

/* See https://github.com/microsoft/monaco-editor/issues/2168#issuecomment-780078600 */
.monaco-aria-container {
	position: absolute !important;
	top: 0; /* avoid being placed underneath a sibling element */
	height: 1px;
	width: 1px;
	margin: -1px;
	overflow: hidden;
	padding: 0;
	clip: rect(1px, 1px, 1px, 1px);
	clip-path: inset(50%);
}

/* The hc-black theme is already high contrast optimized */
.monaco-editor.hc-black,
.monaco-editor.hc-light {
	-ms-high-contrast-adjust: none;
}
/* In case the browser goes into high contrast mode and the editor is not configured with the hc-black theme */
@media screen and (-ms-high-contrast:active) {

	/* current line highlight */
	.monaco-editor.vs .view-overlays .current-line,
	.monaco-editor.vs-dark .view-overlays .current-line {
		border-color: windowtext !important;
		border-left: 0;
		border-right: 0;
	}

	/* view cursors */
	.monaco-editor.vs .cursor,
	.monaco-editor.vs-dark .cursor {
		background-color: windowtext !important;
	}
	/* dnd target */
	.monaco-editor.vs .dnd-target,
	.monaco-editor.vs-dark .dnd-target {
		border-color: windowtext !important;
	}

	/* selected text background */
	.monaco-editor.vs .selected-text,
	.monaco-editor.vs-dark .selected-text {
		background-color: highlight !important;
	}

	/* allow the text to have a transparent background. */
	.monaco-editor.vs .view-line,
	.monaco-editor.vs-dark .view-line {
		-ms-high-contrast-adjust: none;
	}

	/* text color */
	.monaco-editor.vs .view-line span,
	.monaco-editor.vs-dark .view-line span {
		color: windowtext !important;
	}
	/* selected text color */
	.monaco-editor.vs .view-line span.inline-selected-text,
	.monaco-editor.vs-dark .view-line span.inline-selected-text {
		color: highlighttext !important;
	}

	/* allow decorations */
	.monaco-editor.vs .view-overlays,
	.monaco-editor.vs-dark .view-overlays {
		-ms-high-contrast-adjust: none;
	}

	/* various decorations */
	.monaco-editor.vs .selectionHighlight,
	.monaco-editor.vs-dark .selectionHighlight,
	.monaco-editor.vs .wordHighlight,
	.monaco-editor.vs-dark .wordHighlight,
	.monaco-editor.vs .wordHighlightStrong,
	.monaco-editor.vs-dark .wordHighlightStrong,
	.monaco-editor.vs .reference-decoration,
	.monaco-editor.vs-dark .reference-decoration {
		border: 2px dotted highlight !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .rangeHighlight,
	.monaco-editor.vs-dark .rangeHighlight {
		background: transparent !important;
		border: 1px dotted activeborder !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .bracket-match,
	.monaco-editor.vs-dark .bracket-match {
		border-color: windowtext !important;
		background: transparent !important;
	}

	/* find widget */
	.monaco-editor.vs .findMatch,
	.monaco-editor.vs-dark .findMatch,
	.monaco-editor.vs .currentFindMatch,
	.monaco-editor.vs-dark .currentFindMatch {
		border: 2px dotted activeborder !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .find-widget,
	.monaco-editor.vs-dark .find-widget {
		border: 1px solid windowtext;
	}

	/* list - used by suggest widget */
	.monaco-editor.vs .monaco-list .monaco-list-row,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row {
		-ms-high-contrast-adjust: none;
		color: windowtext !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row.focused,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row.focused {
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row:hover,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row:hover {
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* scrollbars */
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar {
		-ms-high-contrast-adjust: none;
		background: background !important;
		border: 1px solid windowtext;
		box-sizing: border-box;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider {
		background: windowtext !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider:hover,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider:hover {
		background: highlight !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider.active,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider.active {
		background: highlight !important;
	}

	/* overview ruler */
	.monaco-editor.vs .decorationsOverviewRuler,
	.monaco-editor.vs-dark .decorationsOverviewRuler {
		opacity: 0;
	}

	/* minimap */
	.monaco-editor.vs .minimap,
	.monaco-editor.vs-dark .minimap {
		display: none;
	}

	/* squiggles */
	.monaco-editor.vs .squiggly-d-error,
	.monaco-editor.vs-dark .squiggly-d-error {
		background: transparent !important;
		border-bottom: 4px double #E47777;
	}
	.monaco-editor.vs .squiggly-c-warning,
	.monaco-editor.vs-dark .squiggly-c-warning {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-b-info,
	.monaco-editor.vs-dark .squiggly-b-info {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-a-hint,
	.monaco-editor.vs-dark .squiggly-a-hint {
		border-bottom: 4px double #6c6c6c;
	}

	/* contextmenu */
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label {
		-ms-high-contrast-adjust: none;
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-menu-item:hover .action-label,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:hover .action-label {
		-ms-high-contrast-adjust: none;
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* diff editor */
	.monaco-diff-editor.vs .diffOverviewRuler,
	.monaco-diff-editor.vs-dark .diffOverviewRuler {
		display: none;
	}
	.monaco-editor.vs .line-insert,
	.monaco-editor.vs-dark .line-insert,
	.monaco-editor.vs .line-delete,
	.monaco-editor.vs-dark .line-delete {
		background: transparent !important;
		border: 1px solid highlight !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .char-insert,
	.monaco-editor.vs-dark .char-insert,
	.monaco-editor.vs .char-delete,
	.monaco-editor.vs-dark .char-delete {
		background: transparent !important;
	}
}

/*.monaco-editor.vs [tabindex="0"]:focus {
	outline: 1px solid rgba(0, 122, 204, 0.4);
	outline-offset: -1px;
	opacity: 1 !important;
}

.monaco-editor.vs-dark [tabindex="0"]:focus {
	outline: 1px solid rgba(14, 99, 156, 0.6);
	outline-offset: -1px;
	opacity: 1 !important;
}*/
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- DiffEditor ---------- */

.monaco-diff-editor .diffOverview {
	z-index: 9;
}

.monaco-diff-editor .diffOverview .diffViewport {
	z-index: 10;
}

/* colors not externalized: using transparancy on background */
.monaco-diff-editor.vs			.diffOverview { background: rgba(0, 0, 0, 0.03); }
.monaco-diff-editor.vs-dark		.diffOverview { background: rgba(255, 255, 255, 0.01); }

.monaco-scrollable-element.modified-in-monaco-diff-editor.vs		.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.vs-dark	.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.hc-black	.scrollbar { background: none; }
.monaco-scrollable-element.modified-in-monaco-diff-editor.hc-light	.scrollbar { background: none; }

.monaco-scrollable-element.modified-in-monaco-diff-editor .slider {
	z-index: 10;
}
.modified-in-monaco-diff-editor				.slider.active { background: rgba(171, 171, 171, .4); }
.modified-in-monaco-diff-editor.hc-black	.slider.active { background: none; }
.modified-in-monaco-diff-editor.hc-light	.slider.active { background: none; }

/* ---------- Diff ---------- */

.monaco-editor .insert-sign,
.monaco-diff-editor .insert-sign,
.monaco-editor .delete-sign,
.monaco-diff-editor .delete-sign {
	font-size: 11px !important;
	opacity: 0.7 !important;
	display: flex !important;
	align-items: center;
}
.monaco-editor.hc-black .insert-sign,
.monaco-diff-editor.hc-black .insert-sign,
.monaco-editor.hc-black .delete-sign,
.monaco-diff-editor.hc-black .delete-sign,
.monaco-editor.hc-light .insert-sign,
.monaco-diff-editor.hc-light .insert-sign,
.monaco-editor.hc-light .delete-sign,
.monaco-diff-editor.hc-light .delete-sign {
	opacity: 1;
}

.monaco-editor .inline-deleted-margin-view-zone {
	text-align: right;
}
.monaco-editor .inline-added-margin-view-zone {
	text-align: right;
}

.monaco-editor .arrow-revert-change {
	z-index: 10;
	position: absolute;
}

.monaco-editor .arrow-revert-change:hover {
	cursor: pointer;
}

/* ---------- Inline Diff ---------- */

.monaco-editor .view-zones .view-lines .view-line span {
	display: inline-block;
}

.monaco-editor .margin-view-zones .lightbulb-glyph:hover {
	cursor: pointer;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-diff-editor .diff-review-line-number {
	text-align: right;
	display: inline-block;
}

.monaco-diff-editor .diff-review {
	position: absolute;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-diff-editor .diff-review-summary {
	padding-left: 10px;
}

.monaco-diff-editor .diff-review-shadow {
	position: absolute;
}

.monaco-diff-editor .diff-review-row {
	white-space: pre;
}

.monaco-diff-editor .diff-review-table {
	display: table;
	min-width: 100%;
}

.monaco-diff-editor .diff-review-row {
	display: table-row;
	width: 100%;
}

.monaco-diff-editor .diff-review-spacer {
	display: inline-block;
	width: 10px;
	vertical-align: middle;
}

.monaco-diff-editor .diff-review-spacer > .codicon {
	font-size: 9px !important;
}

.monaco-diff-editor .diff-review-actions {
	display: inline-block;
	position: absolute;
	right: 10px;
	top: 2px;
}

.monaco-diff-editor .diff-review-actions .action-label {
	width: 16px;
	height: 16px;
	margin: 2px 0;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view {
	position: absolute;
}

.context-view.fixed {
	all: initial;
	font-family: inherit;
	font-size: 13px;
	position: fixed;
	color: inherit;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.quick-input-widget {
	font-size: 13px;
}

.quick-input-widget .monaco-highlighted-label .highlight,
.quick-input-widget .monaco-highlighted-label .highlight {
	color: #0066BF;
}

.vs .quick-input-widget .monaco-list-row.focused .monaco-highlighted-label .highlight,
.vs .quick-input-widget .monaco-list-row.focused .monaco-highlighted-label .highlight {
	color: #9DDDFF;
}

.vs-dark .quick-input-widget .monaco-highlighted-label .highlight,
.vs-dark .quick-input-widget .monaco-highlighted-label .highlight {
	color: #0097fb;
}

.hc-black .quick-input-widget .monaco-highlighted-label .highlight,
.hc-black .quick-input-widget .monaco-highlighted-label .highlight {
	color: #F38518;
}

.hc-light .quick-input-widget .monaco-highlighted-label .highlight,
.hc-light .quick-input-widget .monaco-highlighted-label .highlight {
	color: #0F4A85;
}

.monaco-keybinding > .monaco-keybinding-key {
	background-color: rgba(221, 221, 221, 0.4);
	border: solid 1px rgba(204, 204, 204, 0.4);
	border-bottom-color: rgba(187, 187, 187, 0.4);
	box-shadow: inset 0 -1px 0 rgba(187, 187, 187, 0.4);
	color: #555;
}

.hc-black .monaco-keybinding > .monaco-keybinding-key {
	background-color: transparent;
	border: solid 1px rgb(111, 195, 223);
	box-shadow: none;
	color: #fff;
}

.hc-light .monaco-keybinding > .monaco-keybinding-key {
	background-color: transparent;
	border: solid 1px #0F4A85;
	box-shadow: none;
	color: #292929;
}

.vs-dark .monaco-keybinding > .monaco-keybinding-key {
	background-color: rgba(128, 128, 128, 0.17);
	border: solid 1px rgba(51, 51, 51, 0.6);
	border-bottom-color: rgba(68, 68, 68, 0.6);
	box-shadow: inset 0 -1px 0 rgba(68, 68, 68, 0.6);
	color: #ccc;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-text-button {
	box-sizing: border-box;
	display: flex;
	width: 100%;
	padding: 4px;
	text-align: center;
	cursor: pointer;
	justify-content: center;
	align-items: center;
}

.monaco-text-button:focus {
	outline-offset: 2px !important;
}

.monaco-text-button:hover {
	text-decoration: none !important;
}

.monaco-button.disabled:focus,
.monaco-button.disabled {
	opacity: 0.4 !important;
	cursor: default;
}

.monaco-text-button > .codicon {
	margin: 0 0.2em;
	color: inherit !important;
}

.monaco-button-dropdown {
	display: flex;
	cursor: pointer;
}

.monaco-button-dropdown.disabled {
	cursor: default;
}

.monaco-button-dropdown > .monaco-button:focus {
	outline-offset: -1px !important;
}

.monaco-button-dropdown.disabled > .monaco-button.disabled,
.monaco-button-dropdown.disabled > .monaco-button.disabled:focus,
.monaco-button-dropdown.disabled > .monaco-button-dropdown-separator {
	opacity: 0.4 !important;
}

.monaco-button-dropdown > .monaco-button.monaco-text-button {
	border-right-width: 0 !important;
}

.monaco-button-dropdown .monaco-button-dropdown-separator {
	padding: 4px 0;
	cursor: default;
}

.monaco-button-dropdown .monaco-button-dropdown-separator > div {
	height: 100%;
	width: 1px;
}

.monaco-button-dropdown > .monaco-button.monaco-dropdown-button {
	border-left-width: 0 !important;
}

.monaco-description-button {
	flex-direction: column;
}

.monaco-description-button .monaco-button-label {
	font-weight: 500;
}

.monaco-description-button .monaco-button-description {
	font-style: italic;
}

.monaco-description-button .monaco-button-label,
.monaco-description-button .monaco-button-description
{
	display: flex;
	justify-content: center;
	align-items: center;
}

.monaco-description-button .monaco-button-label > .codicon,
.monaco-description-button .monaco-button-description > .codicon
{
	margin: 0 0.2em;
	color: inherit !important;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-progress-container {
	width: 100%;
	height: 5px;
	overflow: hidden; /* keep progress bit in bounds */
}

.monaco-progress-container .progress-bit {
	width: 2%;
	height: 5px;
	position: absolute;
	left: 0;
	display: none;
}

.monaco-progress-container.active .progress-bit {
	display: inherit;
}

.monaco-progress-container.discrete .progress-bit {
	left: 0;
	transition: width 100ms linear;
}

.monaco-progress-container.discrete.done .progress-bit {
	width: 100%;
}

.monaco-progress-container.infinite .progress-bit {
	animation-name: progress;
	animation-duration: 4s;
	animation-iteration-count: infinite;
	transform: translate3d(0px, 0px, 0px);
	animation-timing-function: linear;
}

.monaco-progress-container.infinite.infinite-long-running .progress-bit {
	/*
		The more smooth `linear` timing function can cause
		higher GPU consumption as indicated in
		https://github.com/microsoft/vscode/issues/97900 &
		https://github.com/microsoft/vscode/issues/138396
	*/
	animation-timing-function: steps(100);
}

/**
 * The progress bit has a width: 2% (1/50) of the parent container. The animation moves it from 0% to 100% of
 * that container. Since translateX is relative to the progress bit size, we have to multiple it with
 * its relative size to the parent container:
 * parent width: 5000%
 *    bit width: 100%
 * translateX should be as follow:
 *  50%: 5000% * 50% - 50% (set to center) = 2450%
 * 100%: 5000% * 100% - 100% (do not overflow) = 4900%
 */
@keyframes progress { from { transform: translateX(0%) scaleX(1) } 50% { transform: translateX(2500%) scaleX(3) } to { transform: translateX(4900%) scaleX(1) } }
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.quick-input-widget {
	position: absolute;
	width: 600px;
	z-index: 2550;
	left: 50%;
	margin-left: -300px;
	-webkit-app-region: no-drag;
}

.quick-input-titlebar {
	display: flex;
	align-items: center;
}

.quick-input-left-action-bar {
	display: flex;
	margin-left: 4px;
	flex: 1;
}

.quick-input-title {
	padding: 3px 0px;
	text-align: center;
	text-overflow: ellipsis;
	overflow: hidden;
}

.quick-input-right-action-bar {
	display: flex;
	margin-right: 4px;
	flex: 1;
}

.quick-input-right-action-bar > .actions-container {
	justify-content: flex-end;
}

.quick-input-titlebar .monaco-action-bar .action-label.codicon {
	background-position: center;
	background-repeat: no-repeat;
	padding: 2px;
}

.quick-input-description {
	margin: 6px;
}

.quick-input-header .quick-input-description {
	margin: 4px 2px;
}

.quick-input-header {
	display: flex;
	padding: 6px 6px 0px 6px;
	margin-bottom: -2px;
}

.quick-input-widget.hidden-input .quick-input-header {
	/* reduce margins and paddings when input box hidden */
	padding: 0;
	margin-bottom: 0;
}

.quick-input-and-message {
	display: flex;
	flex-direction: column;
	flex-grow: 1;
	min-width: 0;
	position: relative;
}

.quick-input-check-all {
	align-self: center;
	margin: 0;
}

.quick-input-filter {
	flex-grow: 1;
	display: flex;
	position: relative;
}

.quick-input-box {
	flex-grow: 1;
}

.quick-input-widget.show-checkboxes .quick-input-box,
.quick-input-widget.show-checkboxes .quick-input-message {
	margin-left: 5px;
}

.quick-input-visible-count {
	position: absolute;
	left: -10000px;
}

.quick-input-count {
	align-self: center;
	position: absolute;
	right: 4px;
	display: flex;
	align-items: center;
}

.quick-input-count .monaco-count-badge {
	vertical-align: middle;
	padding: 2px 4px;
	border-radius: 2px;
	min-height: auto;
	line-height: normal;
}

.quick-input-action {
	margin-left: 6px;
}

.quick-input-action .monaco-text-button {
	font-size: 11px;
	padding: 0 6px;
	display: flex;
	height: 27.5px;
	align-items: center;
}

.quick-input-message {
	margin-top: -1px;
	padding: 5px;
	overflow-wrap: break-word;
}

.quick-input-message > .codicon {
	margin: 0 0.2em;
	vertical-align: text-bottom;
}

.quick-input-progress.monaco-progress-container {
	position: relative;
}

.quick-input-progress.monaco-progress-container,
.quick-input-progress.monaco-progress-container .progress-bit {
	height: 2px;
}

.quick-input-list {
	line-height: 22px;
	margin-top: 6px;
	padding: 0px 1px 1px 1px;
}

.quick-input-widget.hidden-input .quick-input-list {
	margin-top: 0; /* reduce margins when input box hidden */
}

.quick-input-list .monaco-list {
	overflow: hidden;
	max-height: calc(20 * 22px);
}

.quick-input-list .quick-input-list-entry {
	box-sizing: border-box;
	overflow: hidden;
	display: flex;
	height: 100%;
	padding: 0 6px;
}

.quick-input-list .quick-input-list-entry.quick-input-list-separator-border {
	border-top-width: 1px;
	border-top-style: solid;
}

.quick-input-list .monaco-list-row[data-index="0"] .quick-input-list-entry.quick-input-list-separator-border {
	border-top-style: none;
}

.quick-input-list .quick-input-list-label {
	overflow: hidden;
	display: flex;
	height: 100%;
	flex: 1;
}

.quick-input-list .quick-input-list-checkbox {
	align-self: center;
	margin: 0;
}

.quick-input-list .quick-input-list-rows {
	overflow: hidden;
	text-overflow: ellipsis;
	display: flex;
	flex-direction: column;
	height: 100%;
	flex: 1;
	margin-left: 5px;
}

.quick-input-widget.show-checkboxes .quick-input-list .quick-input-list-rows {
	margin-left: 10px;
}

.quick-input-widget .quick-input-list .quick-input-list-checkbox {
	display: none;
}
.quick-input-widget.show-checkboxes .quick-input-list .quick-input-list-checkbox {
	display: inline;
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row {
	display: flex;
	align-items: center;
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row .monaco-icon-label,
.quick-input-list .quick-input-list-rows > .quick-input-list-row .monaco-icon-label .monaco-icon-label-container > .monaco-icon-name-container {
	flex: 1; /* make sure the icon label grows within the row */
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row .codicon[class*='codicon-'] {
	vertical-align: text-bottom;
}

.quick-input-list .quick-input-list-rows .monaco-highlighted-label span {
	opacity: 1;
}

.quick-input-list .quick-input-list-entry .quick-input-list-entry-keybinding {
	margin-right: 8px; /* separate from the separator label or scrollbar if any */
}

.quick-input-list .quick-input-list-label-meta {
	opacity: 0.7;
	line-height: normal;
	text-overflow: ellipsis;
	overflow: hidden;
}

.quick-input-list .monaco-highlighted-label .highlight {
	font-weight: bold;
}

.quick-input-list .quick-input-list-entry .quick-input-list-separator {
	margin-right: 8px; /* separate from keybindings or actions */
}

.quick-input-list .quick-input-list-entry-action-bar {
	display: flex;
	flex: 0;
	overflow: visible;
}

.quick-input-list .quick-input-list-entry-action-bar .action-label {
	/*
	 * By default, actions in the quick input action bar are hidden
	 * until hovered over them or selected.
	 */
	display: none;
}

.quick-input-list .quick-input-list-entry-action-bar .action-label.codicon {
	margin-right: 4px;
	padding: 0px 2px 2px 2px;
}

.quick-input-list .quick-input-list-entry-action-bar {
	margin-top: 1px;
}

.quick-input-list .quick-input-list-entry-action-bar {
	margin-right: 4px; /* separate from scrollbar */
}

.quick-input-list .quick-input-list-entry .quick-input-list-entry-action-bar .action-label.always-visible,
.quick-input-list .quick-input-list-entry:hover .quick-input-list-entry-action-bar .action-label,
.quick-input-list .monaco-list-row.focused .quick-input-list-entry-action-bar .action-label {
	display: flex;
}

/* focused items in quick pick */
.quick-input-list .monaco-list-row.focused .monaco-keybinding-key,
.quick-input-list .monaco-list-row.focused .quick-input-list-entry .quick-input-list-separator {
	color: inherit
}
.quick-input-list .monaco-list-row.focused .monaco-keybinding-key {
	background: none;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-keybinding {
	display: flex;
	align-items: center;
	line-height: 10px;
}

.monaco-keybinding > .monaco-keybinding-key {
	display: inline-block;
	border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	vertical-align: middle;
	font-size: 11px;
	padding: 3px 5px;
	margin: 0 2px;
}

.monaco-keybinding > .monaco-keybinding-key:first-child {
	margin-left: 0;
}

.monaco-keybinding > .monaco-keybinding-key:last-child {
	margin-right: 0;
}

.monaco-keybinding > .monaco-keybinding-key-separator {
	display: inline-block;
}

.monaco-keybinding > .monaco-keybinding-key-chord-separator {
	width: 6px;
}
</style><style id="__monaco_theme_color__">
.mtk1 { color: #d4d4d4; }
.mtk2 { color: #282828; }
.mtk3 { color: #6a9955; }
.mtk4 { color: #569cd6; }
.mtk5 { color: #d16969; }
.mtk6 { color: #d7ba7d; }
.mtk7 { color: #b5cea8; }
.mtk8 { color: #ce9178; }
.mtk9 { color: #646695; }
.mtk10 { color: #4ec9b0; }
.mtk11 { color: #dcdcaa; }
.mtk12 { color: #c8c8c8; }
.mtk13 { color: #c586c0; }
.mtk14 { color: #9cdcfe; }
.mtk15 { color: #000080; }
.mtk16 { color: #f44747; }
.mtk17 { color: #6796e6; }
.mtk18 { color: #808080; }
.mtk19 { color: #4fc1ff; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.monaco-editor, .monaco-editor-background { background-color: #282828; }
.monaco-editor .inputarea.ime-input { background-color: #282828; }
.monaco-editor, .monaco-editor .inputarea.ime-input { color: #d4d4d4; }
.monaco-editor .margin { background-color: #282828; }
.monaco-editor .rangeHighlight { background-color: rgba(255, 255, 255, 0.04); }
.monaco-editor .symbolHighlight { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .mtkw { color: rgba(227, 228, 226, 0.16) !important; }
.monaco-editor .mtkz { color: rgba(227, 228, 226, 0.16) !important; }
.monaco-editor .line-numbers { color: #858585; }
.monaco-editor .line-numbers.active-line-number { color: #c6c6c6; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }

			.monaco-scrollable-element > .shadow.top {
				box-shadow: #000000 0 6px 6px -6px inset;
			}

			.monaco-scrollable-element > .shadow.left {
				box-shadow: #000000 6px 0 6px -6px inset;
			}

			.monaco-scrollable-element > .shadow.top.left {
				box-shadow: #000000 6px 6px 6px -6px inset;
			}
		

			.monaco-scrollable-element > .scrollbar > .slider {
				background: rgba(121, 121, 121, 0.4);
			}
		

			.monaco-scrollable-element > .scrollbar > .slider:hover {
				background: rgba(100, 100, 100, 0.7);
			}
		

			.monaco-scrollable-element > .scrollbar > .slider.active {
				background: rgba(191, 191, 191, 0.4);
			}
		
.monaco-editor .lines-content .core-guide-indent { box-shadow: 1px 0 0 0 #404040 inset; }
.monaco-editor .lines-content .core-guide-indent-active { box-shadow: 1px 0 0 0 #707070 inset; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .minimap-slider .minimap-slider-horizontal { background: rgba(121, 121, 121, 0.2); }
.monaco-editor .minimap-slider:hover .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.35); }
.monaco-editor .minimap-slider.active .minimap-slider-horizontal { background: rgba(191, 191, 191, 0.2); }
.monaco-editor .minimap-shadow-visible { box-shadow: #000000 -6px 0 6px -6px inset; }
.monaco-editor .view-ruler { box-shadow: 1px 0 0 0 #5a5a5a inset; }
.monaco-editor .scroll-decoration { box-shadow: #000000 0 6px 6px -6px inset; }
.monaco-editor .focused .selected-text { background-color: #264f78; }
.monaco-editor .selected-text { background-color: #3a3d41; }
.monaco-editor .inputarea.ime-input { caret-color: #aeafad; }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor.showDeprecated .squiggly-inline-deprecated { text-decoration: line-through; text-decoration-color: #d4d4d4}
.monaco-editor .bracket-match { background-color: rgba(0, 100, 0, 0.1); }
.monaco-editor .bracket-match { border: 1px solid #888888; }
.monaco-editor .findOptionsWidget { background-color: #252526; }
.monaco-editor .findOptionsWidget { color: #cccccc; }
.monaco-editor .findOptionsWidget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .folded-background { background-color: rgba(38, 79, 120, 0.3); }

		.monaco-editor .cldr.codicon.codicon-folding-expanded,
		.monaco-editor .cldr.codicon.codicon-folding-collapsed,
		.monaco-editor .cldr.codicon.codicon-folding-manual-expanded,
		.monaco-editor .cldr.codicon.codicon-folding-manual-collapsed {
			color: #c5c5c5 !important;
		}
		
.monaco-editor .goto-definition-link { color: #4e94ce !important; }

		.monaco-editor .contentWidgets .codicon.codicon-light-bulb {
			color: #ffcc00;
			background-color: rgba(40, 40, 40, 0.7);
		}

		.monaco-editor .contentWidgets .codicon.codicon-lightbulb-autofix {
			color: #75beff;
			background-color: rgba(40, 40, 40, 0.7);
		}

			.monaco-editor .zone-widget .codicon.codicon-error,
			.markers-panel .marker-icon.codicon.codicon-error,
			.text-search-provider-messages .providerMessage .codicon.codicon-error,
			.extensions-viewlet > .extensions .codicon.codicon-error {
				color: #f14c4c;
			}
		

			.monaco-editor .zone-widget .codicon.codicon-warning,
			.markers-panel .marker-icon.codicon.codicon-warning,
			.extensions-viewlet > .extensions .codicon.codicon-warning,
			.extension-editor .codicon.codicon-warning,
			.text-search-provider-messages .providerMessage .codicon.codicon-warning,
			.preferences-editor .codicon.codicon-warning {
				color: #cca700;
			}
		

			.monaco-editor .zone-widget .codicon.codicon-info,
			.markers-panel .marker-icon.codicon.codicon-info,
			.extensions-viewlet > .extensions .codicon.codicon-info,
			.text-search-provider-messages .providerMessage .codicon.codicon-info,
			.extension-editor .codicon.codicon-info {
				color: #3794ff;
			}
		
.monaco-hover .hover-contents a.code-link span { color: #3794ff; }
.monaco-hover .hover-contents a.code-link span:hover { color: #3794ff; }
.monaco-editor .hoverHighlight { background-color: rgba(38, 79, 120, 0.25); }
.monaco-editor .monaco-hover { background-color: #252526; }
.monaco-editor .monaco-hover { border: 1px solid #454545; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover a { color: #3794ff; }
.monaco-editor .monaco-hover a:hover { color: #3794ff; }
.monaco-editor .monaco-hover { color: #cccccc; }
.monaco-editor .monaco-hover .hover-row .actions { background-color: #2c2c2d; }
.monaco-editor .monaco-hover code { background-color: rgba(10, 10, 10, 0.4); }
.monaco-editor.vs .valueSetReplacement { outline: solid 2px #888888; }
.monaco-editor .detected-link-active { color: #4e94ce !important; }
.monaco-editor .parameter-hints-widget { border: 1px solid #454545; }
.monaco-editor .parameter-hints-widget.multiple .body { border-left: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .parameter-hints-widget .signature.has-docs { border-bottom: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .parameter-hints-widget { background-color: #252526; }
.monaco-editor .parameter-hints-widget a { color: #3794ff; }
.monaco-editor .parameter-hints-widget a:hover { color: #3794ff; }
.monaco-editor .parameter-hints-widget { color: #cccccc; }
.monaco-editor .parameter-hints-widget code { background-color: rgba(10, 10, 10, 0.4); }
.monaco-editor .parameter-hints-widget .parameter.active { color: #2aaaff}
.codicon.codicon-symbol-array { color: #cccccc; }
.codicon.codicon-symbol-boolean { color: #cccccc; }
.codicon.codicon-symbol-class { color: #ee9d28; }
.codicon.codicon-symbol-method { color: #b180d7; }
.codicon.codicon-symbol-color { color: #cccccc; }
.codicon.codicon-symbol-constant { color: #cccccc; }
.codicon.codicon-symbol-constructor { color: #b180d7; }

			.codicon.codicon-symbol-value,.codicon.codicon-symbol-enum { color: #ee9d28; }
.codicon.codicon-symbol-enum-member { color: #75beff; }
.codicon.codicon-symbol-event { color: #ee9d28; }
.codicon.codicon-symbol-field { color: #75beff; }
.codicon.codicon-symbol-file { color: #cccccc; }
.codicon.codicon-symbol-folder { color: #cccccc; }
.codicon.codicon-symbol-function { color: #b180d7; }
.codicon.codicon-symbol-interface { color: #75beff; }
.codicon.codicon-symbol-key { color: #cccccc; }
.codicon.codicon-symbol-keyword { color: #cccccc; }
.codicon.codicon-symbol-module { color: #cccccc; }
.codicon.codicon-symbol-namespace { color: #cccccc; }
.codicon.codicon-symbol-null { color: #cccccc; }
.codicon.codicon-symbol-number { color: #cccccc; }
.codicon.codicon-symbol-object { color: #cccccc; }
.codicon.codicon-symbol-operator { color: #cccccc; }
.codicon.codicon-symbol-package { color: #cccccc; }
.codicon.codicon-symbol-property { color: #cccccc; }
.codicon.codicon-symbol-reference { color: #cccccc; }
.codicon.codicon-symbol-snippet { color: #cccccc; }
.codicon.codicon-symbol-string { color: #cccccc; }
.codicon.codicon-symbol-struct { color: #cccccc; }
.codicon.codicon-symbol-text { color: #cccccc; }
.codicon.codicon-symbol-type-parameter { color: #cccccc; }
.codicon.codicon-symbol-unit { color: #cccccc; }
.codicon.codicon-symbol-variable { color: #75beff; }
.monaco-editor .focused .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }
.monaco-editor .wordHighlight { background-color: rgba(87, 87, 87, 0.72); }
.monaco-editor .wordHighlightStrong { background-color: rgba(0, 73, 114, 0.72); }
.monaco-editor .accessibilityHelpWidget { background-color: #252526; }
.monaco-editor .accessibilityHelpWidget { color: #cccccc; }
.monaco-editor .accessibilityHelpWidget { box-shadow: 0 2px 8px rgba(0, 0, 0, 0.36); }
.monaco-editor .tokens-inspect-widget { border: 1px solid #454545; }
.monaco-editor .tokens-inspect-widget .tokens-inspect-separator { background-color: #454545; }
.monaco-editor .tokens-inspect-widget { background-color: #252526; }
.monaco-editor .tokens-inspect-widget { color: #cccccc; }
.monaco-diff-editor .diff-review-line-number { color: #858585; }
.monaco-diff-editor .diff-review-shadow { box-shadow: #000000 0 -6px 6px -6px inset; }
.monaco-editor .char-insert, .monaco-diff-editor .char-insert { background-color: rgba(156, 204, 44, 0.2); }
.monaco-editor .line-insert, .monaco-diff-editor .line-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .inline-added-margin-view-zone { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .gutter-insert, .monaco-diff-editor .gutter-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .char-delete, .monaco-diff-editor .char-delete { background-color: rgba(255, 0, 0, 0.4); }
.monaco-editor .line-delete, .monaco-diff-editor .line-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-editor .inline-deleted-margin-view-zone { background-color: rgba(255, 0, 0, 0.2); }
.monaco-editor .gutter-delete, .monaco-diff-editor .gutter-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor.side-by-side .editor.modified { box-shadow: -6px 0 5px -5px #000000; }

			.monaco-diff-editor .diffViewport {
				background: rgba(121, 121, 121, 0.4);
			}
		

			.monaco-diff-editor .diffViewport:hover {
				background: rgba(100, 100, 100, 0.7);
			}
		

			.monaco-diff-editor .diffViewport:active {
				background: rgba(191, 191, 191, 0.4);
			}
		

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: rgba(0, 122, 204, 0);
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: #a6a6a6;
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #282828;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #282828;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: rgba(255, 255, 255, 0.8);
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.6);
--vscode-editorInlayHint-typeForeground: rgba(255, 255, 255, 0.8);
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.6);
--vscode-editorInlayHint-parameterForeground: rgba(255, 255, 255, 0.8);
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.6);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: rgba(156, 204, 44, 0.2);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.4);
--vscode-diffEditor-insertedLineBackground: rgba(155, 185, 85, 0.2);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.2);
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #383b3d;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #cccccc;
--vscode-menu-background: #252526;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #282828;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #282828;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5;
--vscode-peekViewTitle-background: rgba(55, 148, 255, 0.1);
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #282828;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8); }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #282828; }
.mtk3 { color: #6a9955; }
.mtk4 { color: #569cd6; }
.mtk5 { color: #d16969; }
.mtk6 { color: #d7ba7d; }
.mtk7 { color: #b5cea8; }
.mtk8 { color: #ce9178; }
.mtk9 { color: #646695; }
.mtk10 { color: #4ec9b0; }
.mtk11 { color: #dcdcaa; }
.mtk12 { color: #c8c8c8; }
.mtk13 { color: #c586c0; }
.mtk14 { color: #9cdcfe; }
.mtk15 { color: #000080; }
.mtk16 { color: #f44747; }
.mtk17 { color: #6796e6; }
.mtk18 { color: #808080; }
.mtk19 { color: #4fc1ff; }
.mtk20 { color: #cc6666; }
.mtk21 { color: #608b4e; }
.mtk22 { color: #dcdcdc; }
.mtk23 { color: #a79873; }
.mtk24 { color: #dd6a6f; }
.mtk25 { color: #5bb498; }
.mtk26 { color: #909090; }
.mtk27 { color: #778899; }
.mtk28 { color: #ff00ff; }
.mtk29 { color: #b46695; }
.mtk30 { color: #ff0000; }
.mtk31 { color: #4f76ac; }
.mtk32 { color: #3dc9b0; }
.mtk33 { color: #74b0df; }
.mtk34 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/2461-e958d665c2ab5afd.js.download"><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/6419-bf2b0e67c50692b3.js.download"><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/5891-983742785a4dde23.js.download"><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/719-46205b2a2c9cd287.js.download"><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/9521-fe99975ff5fe1038.js.download"><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/7107-beb8d57336790611.js.download"><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/1179-3a467ec6b88ae472.js.download"><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/8307-39cff2dd6db4307e.js.download"><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/4764-73021b0c137199cf.js.download"><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/2265-9cd1a8e9fb0f4124.js.download"><link as="script" rel="prefetch" href="./Running Sum of 1d Array - LeetCode_files/[[...slug]]-336526233f10d9dd.js.download"><style id="52999">.fI1u6 a{--tw-text-opacity:1;color:rgb(0 122 255/var(--tw-text-opacity))}:is(.Y2Upg .fI1u6 a){--tw-text-opacity:1;color:rgb(0 122 255/var(--tw-text-opacity))}
/*# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL21vZHVsZXMvcHJvYmxlbXMvZWRpdG9yL3Rvb2xiYXIvdG9vbGJhci5pc28uY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUNFLFNBQUEsbUJBQWtDLENBQWxDLDJDQUFrQyxDQUFsQyxxQkFBQSxtQkFBa0MsQ0FBbEMsMkNBQWtDIiwic291cmNlc0NvbnRlbnQiOlsiLmxhbmdJbmZvIGEgeyBcbiAgQGFwcGx5IHRleHQtYmx1ZS1zIGRhcms6dGV4dC1ibHVlLXNcbn0iXSwic291cmNlUm9vdCI6IiJ9 */</style></head><body><div id="__next"><script>!function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('lc-theme');if('system'===e||(!e&&true)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}if(e==='light'||e==='dark')d.style.colorScheme=e}catch(e){}}()</script><div class="hidden"><div class="hidden"><div class="swiper-autoheight"></div><div class="swiper-autoheight"></div><div class="gap-8"></div><div class="gap-8"></div><div class="gap-6"></div><div class="gap-6"></div><div class="pt-3"></div><div class="pt-3"></div><div class="space-y-1.5"></div><div class="space-y-1.5"></div><div role="rowgroup"></div><div role="rowgroup"></div><div role="table"></div><div role="table"></div></div></div><div class="flex h-[100vh] min-w-[360px] flex-col  text-label-1 dark:text-dark-label-1 overflow-x-auto"><div class="h-[100vh] bg-gray-2 dark:bg-dark-layer-bg min-w-[1000px]"><div class="flex h-full w-full flex-col bg-layer-bg-gray dark:bg-layer-bg-gray"><div class="z-base-2 fixed left-0 right-0 top-0  md:relative bg-layer-1 dark:bg-dark-layer-1 z-nav-9" id="navbar-container"></div><div class="md:!h-0" style="height: 0px;"></div><div class="relative"><nav class="z-nav-1 relative flex h-[48px] w-full shrink-0 items-center px-5 pr-2.5"><div class="flex w-full justify-between"><div class="flex w-full items-center justify-between"><div class="flex items-center"><ul class="relative mr-2 flex h-10 items-center"><a href="https://leetcode.com/" class="mr-2 self-center"><div class="mb-0.5 pl-1"><div class="hidden h-5 dark:flex"><img src="./Running Sum of 1d Array - LeetCode_files/logo-dark-c96c407d175e36c81e236fcfdd682a0b.png" class="h-full" alt="LeetCode Logo"></div><div class="flex h-5 dark:hidden"><img src="./Running Sum of 1d Array - LeetCode_files/logo-ff2b712834cf26bf50a5de58ee27bcef.png" class="h-full" alt="LeetCode Logo"></div></div></a><li class="h-[16px] w-[1px] bg-lc-fill-01 dark:bg-dark-lc-fill-01"></li></ul><div class="lc-md:flex group flex items-center overflow-hidden rounded hover:bg-fill-tertiary dark:hover:bg-fill-tertiary"><div class="group/nav-back cursor-pointer gap-2 hover:text-lc-icon-primary dark:hover:text-dark-lc-icon-primary flex items-center h-[32px] transition-none hover:bg-fill-quaternary dark:hover:bg-fill-quaternary text-gray-60 dark:text-gray-60 px-2" data-state="closed"><div class="relative text-[16px] leading-[normal] p-0.5 before:block before:h-4 before:w-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="indent" class="svg-inline--fa fa-indent absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M0 64C0 77.3 10.7 88 24 88H424c13.3 0 24-10.7 24-24s-10.7-24-24-24H24C10.7 40 0 50.7 0 64zM192 192c0 13.3 10.7 24 24 24H424c13.3 0 24-10.7 24-24s-10.7-24-24-24H216c-13.3 0-24 10.7-24 24zm24 104c-13.3 0-24 10.7-24 24s10.7 24 24 24H424c13.3 0 24-10.7 24-24s-10.7-24-24-24H216zM0 448c0 13.3 10.7 24 24 24H424c13.3 0 24-10.7 24-24s-10.7-24-24-24H24c-13.3 0-24 10.7-24 24zM121 268.4c7.8-6.4 7.8-18.3 0-24.7L26.2 165.6C15.7 157 0 164.4 0 177.9V334.1c0 13.5 15.7 20.9 26.2 12.4L121 268.4z"></path></svg></div><div class="relative flex items-center gap-2"><div class="max-w-[170px] truncate font-medium group-hover/nav-back:invisible group-hover:text-lc-text-primary dark:group-hover:text-dark-lc-text-primary text-text-primary dark:text-text-primary hover:text-text-primary dark:hover:text-text-primary">Problem List</div><div class="invisible absolute left-0 top-0 flex w-full max-w-[170px] gap-1 overflow-hidden group-hover/nav-back:visible"><div class="flex-1 truncate font-medium group-hover:text-lc-text-primary dark:group-hover:text-dark-lc-text-primary text-text-primary dark:text-text-primary hover:text-text-primary dark:hover:text-text-primary">Problem List</div><div class="flex flex-none" data-state="closed"><a target="_blank" rel="noopener noreferrer" class="no-underline truncate rounded p-1 bg-fill-tertiary dark:bg-fill-tertiary text-text-tertiary dark:text-text-tertiary hover:bg-fill-secondary dark:hover:bg-fill-secondary hover:text-text-primary dark:hover:text-text-primary" href="https://leetcode.com/problemset/"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-3 w-3"><path fill-rule="evenodd" d="M14.167 6a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0V7.414l-6.46 6.46a1 1 0 01-1.414-1.414L16.753 6h-2.586zM18 14.533a1 1 0 112 0v3.6A2.867 2.867 0 0117.133 21H5.867A2.867 2.867 0 013 18.133V6.867A2.867 2.867 0 015.867 4h3.6a1 1 0 110 2h-3.6A.867.867 0 005 6.867v11.266c0 .479.388.867.867.867h11.266a.867.867 0 00.867-.867v-3.6z" clip-rule="evenodd"></path></svg></a></div></div></div></div><div class="h-[28px] w-[1px] bg-layer-bg-gray dark:bg-layer-bg-gray"></div><a class="group cursor-pointer group-hover:text-lc-icon-primary dark:group-hover:text-dark-lc-icon-primary flex items-center h-[32px] transition-none hover:bg-fill-quaternary dark:hover:bg-fill-quaternary text-gray-60 dark:text-gray-60 w-[32px]" href="https://leetcode.com/problems/sales-by-day-of-the-week" data-state="closed"><div class="relative text-[16px] leading-[normal] before:block before:h-4 before:w-4 m-auto items-center"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="chevron-left" class="svg-inline--fa fa-chevron-left absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path fill="currentColor" d="M15 239c-9.4 9.4-9.4 24.6 0 33.9L207 465c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9L65.9 256 241 81c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0L15 239z"></path></svg></div></a><div class="h-[28px] w-[1px] bg-layer-bg-gray dark:bg-layer-bg-gray"></div><a class="group cursor-pointer group-hover:text-lc-icon-primary dark:group-hover:text-dark-lc-icon-primary flex items-center h-[32px] transition-none hover:bg-fill-quaternary dark:hover:bg-fill-quaternary text-gray-60 dark:text-gray-60 w-[32px]" href="https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals" data-state="closed"><div class="relative text-[16px] leading-[normal] before:block before:h-4 before:w-4 m-auto items-center"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="chevron-right" class="svg-inline--fa fa-chevron-right absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path fill="currentColor" d="M305 239c9.4 9.4 9.4 24.6 0 33.9L113 465c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l175-175L79 81c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0L305 239z"></path></svg></div></a><div class="h-[28px] w-[1px] bg-layer-bg-gray dark:bg-layer-bg-gray"></div><a href="https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other" target="" rel="" class="cursor-pointer justify-center hover:text-lc-icon-primary dark:hover:text-dark-lc-icon-primary flex items-center h-[32px] transition-none hover:bg-fill-quaternary dark:hover:bg-fill-quaternary text-gray-60 dark:text-gray-60 w-[32px]" data-state="closed"><div class="relative text-[16px] leading-[normal] before:block before:h-4 before:w-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="shuffle" class="svg-inline--fa fa-shuffle absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M425 31l80 80c9.4 9.4 9.4 24.6 0 33.9l-80 80c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l39-39H352c-12.6 0-24.4 5.9-32 16l-46 61.3-30-40 37.6-50.1C298.2 117 324.3 104 352 104h78.1L391 65c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0zM204 322.7l-37.6 50.1C149.8 395 123.7 408 96 408H24c-13.3 0-24-10.7-24-24s10.7-24 24-24H96c12.6 0 24.4-5.9 32-16l46-61.3 30 40zM391 287c9.4-9.4 24.6-9.4 33.9 0l80 80c9.4 9.4 9.4 24.6 0 33.9l-80 80c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l39-39H352c-27.7 0-53.8-13-70.4-35.2L128 168c-7.6-10.1-19.4-16-32-16H24c-13.3 0-24-10.7-24-24s10.7-24 24-24H96c27.7 0 53.8 13 70.4 35.2L320 344c7.6 10.1 19.4 16 32 16h78.1l-39-39c-9.4-9.4-9.4-24.6 0-33.9z"></path></svg></div></a></div></div><div class="relative ml-4 flex items-center gap-2"><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:r0:"><div><div id="qd-layout-manager-btn" class="flex cursor-pointer rounded-lg p-2 text-sd-muted-foreground hover:text-sd-foreground hover:bg-fill-tertiary dark:hover:bg-fill-tertiary" data-state="closed"><div class="relative text-[16px] leading-[normal] before:block before:h-4 before:w-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="objects-column" class="svg-inline--fa fa-objects-column absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M48 80V240h96V80H48zM0 80C0 53.5 21.5 32 48 32h96c26.5 0 48 21.5 48 48V240c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V80zM304 272V432h96V272H304zm-48 0c0-26.5 21.5-48 48-48h96c26.5 0 48 21.5 48 48V432c0 26.5-21.5 48-48 48H304c-26.5 0-48-21.5-48-48V272zM144 368H48v64h96V368zM48 320h96c26.5 0 48 21.5 48 48v64c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V368c0-26.5 21.5-48 48-48zM304 80v64h96V80H304zm-48 0c0-26.5 21.5-48 48-48h96c26.5 0 48 21.5 48 48v64c0 26.5-21.5 48-48 48H304c-26.5 0-48-21.5-48-48V80z"></path></svg></div></div></div></div></div></div><div class="pointer-events-none absolute inset-0" type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r3:" data-state="closed"></div><div class="flex cursor-pointer rounded-lg p-2 text-sd-muted-foreground hover:text-sd-foreground hover:bg-fill-tertiary dark:hover:bg-fill-tertiary" id="nav-setting-btn" data-state="closed"><div class="relative text-[16px] leading-[normal] before:block before:h-4 before:w-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="gear" class="svg-inline--fa fa-gear absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M256 0c17 0 33.6 1.7 49.8 4.8c7.9 1.5 21.8 6.1 29.4 20.1c2 3.7 3.6 7.6 4.6 11.8l9.3 38.5C350.5 81 360.3 86.7 366 85l38-11.2c4-1.2 8.1-1.8 12.2-1.9c16.1-.5 27 9.4 32.3 15.4c22.1 25.1 39.1 54.6 49.9 86.3c2.6 7.6 5.6 21.8-2.7 35.4c-2.2 3.6-4.9 7-8 10L459 246.3c-4.2 4-4.2 15.5 0 19.5l28.7 27.3c3.1 3 5.8 6.4 8 10c8.2 13.6 5.2 27.8 2.7 35.4c-10.8 31.7-27.8 61.1-49.9 86.3c-5.3 6-16.3 15.9-32.3 15.4c-4.1-.1-8.2-.8-12.2-1.9L366 427c-5.7-1.7-15.5 4-16.9 9.8l-9.3 38.5c-1 4.2-2.6 8.2-4.6 11.8c-7.7 14-21.6 18.5-29.4 20.1C289.6 510.3 273 512 256 512s-33.6-1.7-49.8-4.8c-7.9-1.5-21.8-6.1-29.4-20.1c-2-3.7-3.6-7.6-4.6-11.8l-9.3-38.5c-1.4-5.8-11.2-11.5-16.9-9.8l-38 11.2c-4 1.2-8.1 1.8-12.2 1.9c-16.1 .5-27-9.4-32.3-15.4c-22-25.1-39.1-54.6-49.9-86.3c-2.6-7.6-5.6-21.8 2.7-35.4c2.2-3.6 4.9-7 8-10L53 265.7c4.2-4 4.2-15.5 0-19.5L24.2 218.9c-3.1-3-5.8-6.4-8-10C8 195.3 11 181.1 13.6 173.6c10.8-31.7 27.8-61.1 49.9-86.3c5.3-6 16.3-15.9 32.3-15.4c4.1 .1 8.2 .8 12.2 1.9L146 85c5.7 1.7 15.5-4 16.9-9.8l9.3-38.5c1-4.2 2.6-8.2 4.6-11.8c7.7-14 21.6-18.5 29.4-20.1C222.4 1.7 239 0 256 0zM218.1 51.4l-8.5 35.1c-7.8 32.3-45.3 53.9-77.2 44.6L97.9 120.9c-16.5 19.3-29.5 41.7-38 65.7l26.2 24.9c24 22.8 24 66.2 0 89L59.9 325.4c8.5 24 21.5 46.4 38 65.7l34.6-10.2c31.8-9.4 69.4 12.3 77.2 44.6l8.5 35.1c24.6 4.5 51.3 4.5 75.9 0l8.5-35.1c7.8-32.3 45.3-53.9 77.2-44.6l34.6 10.2c16.5-19.3 29.5-41.7 38-65.7l-26.2-24.9c-24-22.8-24-66.2 0-89l26.2-24.9c-8.5-24-21.5-46.4-38-65.7l-34.6 10.2c-31.8 9.4-69.4-12.3-77.2-44.6l-8.5-35.1c-24.6-4.5-51.3-4.5-75.9 0zM208 256a48 48 0 1 0 96 0 48 48 0 1 0 -96 0zm48 96a96 96 0 1 1 0-192 96 96 0 1 1 0 192z"></path></svg></div></div><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:r5:"><a class="group relative flex h-8 items-center justify-center rounded p-1 hover:bg-fill-3 dark:hover:bg-dark-fill-3" href="https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/?envType=daily-question&amp;envId=2024-11-14"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18" width="1em" height="1em" fill="currentColor" class="h-[20px] w-[20px] hover:text-text-primary dark:hover:text-text-primary text-text-secondary dark:text-text-secondary h-4 w-4"><path fill-rule="evenodd" d="M7.19 1.564a.75.75 0 01.729.069c2.137 1.475 3.373 3.558 3.981 5.002l.641-.663a.75.75 0 011.17.115c1.633 2.536 1.659 5.537.391 7.725-1.322 2.282-3.915 2.688-5.119 2.688-1.177 0-3.679-.203-5.12-2.688-.623-1.076-.951-2.29-.842-3.528.109-1.245.656-2.463 1.697-3.54.646-.67 1.129-1.592 1.468-2.492.337-.895.51-1.709.564-2.105a.75.75 0 01.44-.583zm.784 2.023c-.1.368-.226.773-.385 1.193-.375.997-.947 2.13-1.792 3.005-.821.851-1.205 1.754-1.282 2.63-.078.884.153 1.792.647 2.645C6.176 14.81 7.925 15 8.983 15c1.03 0 2.909-.366 3.822-1.94.839-1.449.97-3.446.11-5.315l-.785.812a.75.75 0 01-1.268-.345c-.192-.794-1.04-2.948-2.888-4.625z" clip-rule="evenodd"></path></svg><span class="mx-1 text-sm font-medium hover:text-text-primary dark:hover:text-text-primary text-text-secondary dark:text-text-secondary">0</span></a></div></div></div><div style="position: fixed; top: 1px; left: 1px; width: 1px; height: 0px; padding: 0px; margin: -1px; overflow: hidden; clip: rect(0px, 0px, 0px, 0px); white-space: nowrap; border-width: 0px; display: none;"></div><div><div class="relative"><button class="flex items-center focus:outline-none" id="headlessui-menu-button-:r7:" type="button" aria-haspopup="menu" aria-expanded="false" data-headlessui-state=""><span id="navbar_user_avatar" class="relative ml-1 h-6 w-6 mr-2"><img src="./Running Sum of 1d Array - LeetCode_files/default_avatar.jpg" alt="avatar" class="h-full w-full rounded-full object-cover"></span></button></div></div><div class="ml-0"><a href="https://leetcode.com/subscribe/?ref=lp_pl&amp;source=qd"><span class="display-none h-8 w-[84px] cursor-pointer  rounded-[8px] bg-[#ffa1161f] text-center leading-8 transition-colors hover:bg-[#ffa11633] lg:inline-block font-typo"><span class="text-brand-orange">Premium</span></span></a></div></div></div></div></nav><div class="z-nav-5 absolute left-1/2 top-0 h-full -translate-x-1/2 py-2"><div class="relative flex" id="ide-top-btns"><div><div class="relative flex overflow-hidden rounded bg-fill-tertiary dark:bg-fill-tertiary mr-[6px]"><div class="relative overflow-hidden transition-[width] ease-[cubic-bezier(0,1.5,.5,1)]" style="width: auto; transition-duration: 0.6s;"><div class="transition-[opacity] pointer-events-none absolute left-0 top-0 flex opacity-0"><div class="group flex flex-none items-center justify-center min-w-[150px] gap-2 px-4 py-[6px] hover:bg-transparent dark:hover:bg-transparent"><img src="./Running Sum of 1d Array - LeetCode_files/dark-judging-723b3c3e728a574bc2a2d4b89a10d4d7.gif" alt="Judging..." class="h-5 w-5 hidden"><img src="./Running Sum of 1d Array - LeetCode_files/dark-pending-f313d6fe32951fb6b4d48ad3ee4f3821.gif" alt="Pending..." class="h-5 w-5 hidden"></div></div><div class="transition-[opacity]"><div class="relative overflow-hidden transition-[width] ease-[cubic-bezier(0,1.5,.5,1)]" style="width: auto; transition-duration: 0.6s;"><div class="transition-[opacity] pointer-events-none absolute left-0 top-0 flex opacity-0"><div class="flex flex-none"><div class="group flex flex-none items-center justify-center hover:bg-fill-quaternary dark:hover:bg-fill-quaternary"><div class="cursor-pointer p-[9px] text-red-60 dark:text-red-60" data-state="closed"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-3.5 w-3.5"><path d="M5.998 1.4a4.6 4.6 0 00-4.6 4.6v12a4.6 4.6 0 004.6 4.6h12a4.6 4.6 0 004.6-4.6V6a4.6 4.6 0 00-4.6-4.6h-12z"></path></svg></div></div><div class="w-[1px] flex-none bg-layer-bg-gray dark:bg-layer-bg-gray"></div><div class="relative overflow-hidden transition-[width] ease-[cubic-bezier(0,1.5,.5,1)]" style="width: auto; transition-duration: 0.6s;"><div class="transition-[opacity]"><div class="group flex flex-none items-center justify-center min-w-[140px] gap-2 px-4 py-[6px] hover:bg-transparent dark:hover:bg-transparent"><div class="h-5 w-5 flex-none"><img src="./Running Sum of 1d Array - LeetCode_files/premium-lightning-judging-4387bb93db459811b028131cb5ea75d4.gif" alt="Debugging..." class="h-full w-full"></div><div class="flex-none text-xs leading-[20px] text-brand-orange dark:text-brand-orange">Debugging...</div></div></div><div class="transition-[opacity] pointer-events-none absolute left-0 top-0 flex opacity-0"><div class="flex"><button disabled="" data-state="closed" class="font-medium items-center whitespace-nowrap focus:outline-none cursor-not-allowed opacity-50 flex flex-none rounded-none p-[9px] bg-transparent dark:bg-transparent text-gray-60 dark:text-gray-60"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-3.5 w-3.5"><path d="M6.708 1.96C5.507.76 3.453 1.61 3.453 3.308v17.383c0 1.7 2.054 2.55 3.255 1.349l8.692-8.692a1.907 1.907 0 000-2.696L6.708 1.96zM20.543 3.308a1 1 0 10-2 0v17.383a1 1 0 102 0V3.308z"></path></svg></button><button disabled="" data-state="closed" class="font-medium items-center whitespace-nowrap focus:outline-none cursor-not-allowed opacity-50 flex flex-none rounded-none p-[9px] bg-transparent dark:bg-transparent text-gray-60 dark:text-gray-60"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-3.5 w-3.5"><path d="M19.496 6.828v3.586L13.96 4.88a3 3 0 00-4.243 0l-7.424 7.424a1 1 0 101.414 1.414l7.425-7.424a1 1 0 011.414 0l5.535 5.535h-3.585a1 1 0 100 2h5.5a1.5 1.5 0 001.5-1.5v-5.5a1 1 0 00-2 0zM11.5 17.172a1.5 1.5 0 100 3 1.5 1.5 0 000-3z"></path></svg></button><button disabled="" data-state="closed" class="font-medium items-center whitespace-nowrap focus:outline-none cursor-not-allowed opacity-50 flex flex-none rounded-none p-[9px] bg-transparent dark:bg-transparent text-gray-60 dark:text-gray-60"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-3.5 w-3.5"><path fill-rule="evenodd" d="M13 3a1 1 0 10-2 0v11.485L8.464 11.95a1 1 0 10-1.414 1.414l3.89 3.889a1.5 1.5 0 002.12 0l3.89-3.89a1 1 0 10-1.414-1.413L13 14.485V3zm-1 16a1.5 1.5 0 100 3 1.5 1.5 0 000-3z" clip-rule="evenodd"></path></svg></button><button disabled="" data-state="closed" class="font-medium items-center whitespace-nowrap focus:outline-none cursor-not-allowed opacity-50 flex flex-none rounded-none p-[9px] bg-transparent dark:bg-transparent text-gray-60 dark:text-gray-60"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-3.5 w-3.5"><path fill-rule="evenodd" d="M12 5a1.5 1.5 0 110-3 1.5 1.5 0 010 3zm.003 17a1 1 0 001-1V9.515l2.535 2.535a1 1 0 001.414-1.414l-3.889-3.889a1.5 1.5 0 00-2.121 0l-3.89 3.89a1 1 0 001.415 1.413l2.536-2.535V21a1 1 0 001 1z" clip-rule="evenodd"></path></svg></button><button disabled="" data-state="closed" class="font-medium items-center whitespace-nowrap focus:outline-none cursor-not-allowed opacity-50 flex flex-none rounded-none p-[9px] bg-transparent dark:bg-transparent text-gray-60 dark:text-gray-60"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-3.5 w-3.5"><path fill-rule="evenodd" d="M5.725 9.255h2.843a1 1 0 110 2H3.2a1 1 0 01-1-1V4.887a1 1 0 012 0v3.056l2.445-2.297a9.053 9.053 0 11-2.142 9.415 1 1 0 011.886-.665 7.053 7.053 0 1010.064-8.515 7.063 7.063 0 00-8.417 1.202L5.725 9.255z" clip-rule="evenodd"></path></svg></button></div></div></div></div></div><div class="transition-[opacity]"><div class="flex flex-none"><div class="group flex flex-none items-center justify-center hover:bg-fill-quaternary dark:hover:bg-fill-quaternary"><button data-state="closed" class="font-medium items-center whitespace-nowrap focus:outline-none inline-flex opacity-50 cursor-pointer rounded-none p-2 hover:bg-transparent dark:hover:bg-transparent !opacity-100"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14 14" width="1em" height="1em" fill="none" class="text-text-secondary dark:text-text-secondary w-4 h-4"><path fill-rule="evenodd" clip-rule="evenodd" d="M5.83373 3.48097C5.83828 3.48095 5.84284 3.48094 5.84739 3.48094H8.15673C8.16127 3.48094 8.1658 3.48095 8.17033 3.48097C8.16323 2.8418 7.64288 2.32585 7.00203 2.32585C6.36117 2.32585 5.84083 2.8418 5.83373 3.48097ZM9.32578 3.72484C9.33325 3.64887 9.33707 3.57194 9.33707 3.49422C9.33707 2.20461 8.29164 1.15918 7.00203 1.15918C5.71242 1.15918 4.66699 2.20461 4.66699 3.49422C4.66699 3.57189 4.6708 3.64879 4.67826 3.72471C4.22848 3.92173 3.83796 4.22895 3.54086 4.61221C3.53598 4.61016 3.53087 4.60799 3.52553 4.60569C3.46337 4.57893 3.37269 4.53607 3.268 4.47498C3.05532 4.35088 2.80417 4.16288 2.60939 3.89984C2.49885 3.75056 2.42174 3.52306 2.37646 3.29097C2.35519 3.18193 2.34348 3.08539 2.33719 3.01701C2.33406 2.98309 2.33234 2.95681 2.33143 2.94023L2.3306 2.9231L2.33051 2.92073C2.32175 2.59947 2.05467 2.34567 1.73317 2.35352C1.4111 2.36138 1.15638 2.62884 1.16424 2.95091L1.7474 2.93668C1.16424 2.95091 1.16424 2.95077 1.16424 2.95091L1.16427 2.95208L1.16431 2.95356L1.16442 2.9574L1.16482 2.9686C1.16517 2.97759 1.16571 2.9896 1.16652 3.00435C1.16814 3.03382 1.17087 3.07444 1.17543 3.12395C1.1845 3.22244 1.20105 3.35889 1.23138 3.51437C1.28932 3.81133 1.40881 4.23898 1.6718 4.59413C1.98923 5.0228 2.37942 5.30724 2.68001 5.48264C2.81254 5.55997 2.93137 5.61828 3.0248 5.66C2.96341 5.89559 2.93073 6.14278 2.93073 6.39761V7.00608H1.74746C1.42529 7.00608 1.16412 7.26725 1.16412 7.58941C1.16412 7.91158 1.42529 8.17275 1.74746 8.17275H2.93073V8.77192C2.93073 9.01289 2.95167 9.24894 2.99182 9.47837C2.90725 9.51778 2.80645 9.56896 2.69617 9.63331C2.39557 9.80871 2.00538 10.0931 1.68795 10.5218C1.42496 10.877 1.30547 11.3046 1.24754 11.6016C1.2172 11.7571 1.20065 11.8935 1.19158 11.992C1.18703 12.0415 1.1843 12.0821 1.18268 12.1116C1.18186 12.1263 1.18133 12.1384 1.18097 12.1473L1.18058 12.1585L1.18046 12.1624L1.18042 12.1639L1.18041 12.1645C1.1804 12.1646 1.18039 12.165 1.76355 12.1793L1.18041 12.1645C1.17255 12.4866 1.42725 12.7546 1.74932 12.7624C2.07082 12.7703 2.3379 12.5165 2.34667 12.1952C2.34668 12.1947 2.34669 12.1942 2.34671 12.1937L2.34675 12.1928L2.34758 12.1757C2.34849 12.1591 2.35022 12.1329 2.35334 12.0989C2.35963 12.0306 2.37134 11.934 2.39261 11.825C2.43789 11.5929 2.515 11.3654 2.62554 11.2161C2.82032 10.9531 3.07147 10.7651 3.28415 10.641C3.31111 10.6252 3.33714 10.6107 3.362 10.5974C3.7181 11.306 4.27486 11.8961 4.95693 12.293C5.08155 12.3655 5.21041 12.4316 5.34306 12.4909C5.63722 12.6223 5.98219 12.4903 6.11358 12.1962C6.24498 11.902 6.11303 11.557 5.81888 11.4256C5.72442 11.3834 5.63259 11.3363 5.54371 11.2846C4.67753 10.7806 4.0974 9.84367 4.0974 8.77192V6.39761C4.0974 5.43111 4.8809 4.64761 5.84739 4.64761H6.41598L6.41634 6.12506C6.41642 6.44723 6.67766 6.70833 6.99982 6.70825C7.32199 6.70817 7.58309 6.44694 7.58301 6.12478L7.58265 4.64761H8.15673C8.47942 4.64761 8.78007 4.73441 9.03852 4.88556C9.31661 5.04821 9.6739 4.95462 9.83655 4.67652C9.99919 4.39842 9.9056 4.04113 9.62751 3.87849C9.53037 3.82168 9.42964 3.77032 9.32578 3.72484ZM3.6237 10.4776L3.62467 10.4772C3.62491 10.4771 3.62506 10.4771 3.62467 10.4772M12.2707 2.35353C12.5927 2.36139 12.8475 2.62885 12.8396 2.95092L12.2564 2.93669C12.8396 2.95092 12.8396 2.95078 12.8396 2.95092L12.8395 2.95357L12.8394 2.95742L12.839 2.96862C12.8387 2.9776 12.8381 2.98961 12.8373 3.00436C12.8357 3.03383 12.833 3.07445 12.8284 3.12396C12.8193 3.22245 12.8028 3.3589 12.7725 3.51438C12.7145 3.81134 12.595 4.239 12.332 4.59414C12.2543 4.69916 12.1723 4.79531 12.0887 4.88308C11.8664 5.11632 11.4972 5.12523 11.2639 4.90299C11.0307 4.68075 11.0218 4.31151 11.244 4.07827C11.2968 4.02285 11.3474 3.96343 11.3945 3.89986C11.505 3.75058 11.5821 3.52308 11.6274 3.29099C11.6487 3.18194 11.6604 3.0854 11.6667 3.01702C11.6698 2.9831 11.6715 2.95682 11.6724 2.94024L11.6732 2.92311L11.6733 2.92222C11.6733 2.92173 11.6733 2.92124 11.6733 2.92075C11.6821 2.59949 11.9492 2.34569 12.2707 2.35353Z" fill="#FFA116"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M10.2164 5.71748C9.74147 5.70692 9.34051 5.81961 9.01184 6.03027C8.68565 6.23935 8.45171 6.5313 8.28573 6.84829C7.9588 7.47271 7.875 8.23293 7.875 8.81114V8.84782C7.48968 8.99728 7.21875 9.37613 7.21875 9.81114V12.4153C7.21875 12.9779 7.6719 13.4466 8.23958 13.4466H12.1771C12.7448 13.4466 13.1979 12.9779 13.1979 12.4153V9.81114C13.1979 9.37613 12.927 8.99728 12.5417 8.84782V8.81114C12.5417 8.23216 12.4577 7.48931 12.1298 6.87341C11.7881 6.2317 11.1836 5.73897 10.2164 5.71748ZM11.8124 8.77989H8.60426C8.60738 8.25706 8.68927 7.64956 8.93171 7.18652C9.05285 6.95515 9.20856 6.77027 9.40532 6.64416C9.59959 6.51964 9.85489 6.43879 10.2002 6.44646C10.8737 6.46143 11.2536 6.77932 11.4861 7.21609C11.7276 7.66959 11.8093 8.25853 11.8124 8.77989Z" fill="currentColor"></path></svg></button></div><div class="w-[1px] flex-none bg-layer-bg-gray dark:bg-layer-bg-gray"></div><div class="flex"><div class="group flex flex-none items-center justify-center hover:bg-fill-quaternary dark:hover:bg-fill-quaternary"><div data-state="closed"><button data-e2e-locator="console-run-button" class="font-medium items-center whitespace-nowrap focus:outline-none inline-flex rounded-none py-1.5 px-3 bg-transparent dark:bg-transparent text-text-primary dark:text-text-primary"><div class="relative text-[16px] leading-[normal] p-0.5 before:block before:h-4 before:w-4 mr-2 text-text-secondary dark:text-text-secondary"><svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="play" class="svg-inline--fa fa-play absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M73 39c-14.8-9.1-33.4-9.4-48.5-.9S0 62.6 0 80V432c0 17.4 9.4 33.4 24.5 41.9s33.7 8.1 48.5-.9L361 297c14.3-8.7 23-24.2 23-41s-8.7-32.2-23-41L73 39z"></path></svg></div><span class="text-sm font-medium">Run</span></button></div></div><div class="w-[1px] flex-none bg-layer-bg-gray dark:bg-layer-bg-gray"></div><div class="group flex flex-none items-center justify-center hover:bg-fill-quaternary dark:hover:bg-fill-quaternary"><div data-state="closed"><button data-e2e-locator="console-submit-button" class="font-medium items-center whitespace-nowrap focus:outline-none inline-flex relative select-none rounded-none px-3 py-1.5 bg-transparent dark:bg-transparent text-green-60 dark:text-green-60"><div class="relative text-[16px] leading-[normal] p-0.5 before:block before:h-4 before:w-4 mr-2"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="cloud-arrow-up" class="svg-inline--fa fa-cloud-arrow-up absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path fill="currentColor" d="M354.9 121.7c13.8 16 36.5 21.1 55.9 12.5c8.9-3.9 18.7-6.2 29.2-6.2c39.8 0 72 32.2 72 72c0 4-.3 7.9-.9 11.7c-3.5 21.6 8.1 42.9 28.1 51.7C570.4 276.9 592 308 592 344c0 46.8-36.6 85.2-82.8 87.8c-.6 0-1.3 .1-1.9 .2H504 144c-53 0-96-43-96-96c0-41.7 26.6-77.3 64-90.5c19.2-6.8 32-24.9 32-45.3l0-.2v0 0c0-66.3 53.7-120 120-120c36.3 0 68.8 16.1 90.9 41.7zM512 480v-.2c71.4-4.1 128-63.3 128-135.8c0-55.7-33.5-103.7-81.5-124.7c1-6.3 1.5-12.8 1.5-19.3c0-66.3-53.7-120-120-120c-17.4 0-33.8 3.7-48.7 10.3C360.4 54.6 314.9 32 264 32C171.2 32 96 107.2 96 200l0 .2C40.1 220 0 273.3 0 336c0 79.5 64.5 144 144 144H464h40 8zM223 255c-9.4 9.4-9.4 24.6 0 33.9s24.6 9.4 33.9 0l39-39V384c0 13.3 10.7 24 24 24s24-10.7 24-24V249.9l39 39c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9l-80-80c-9.4-9.4-24.6-9.4-33.9 0l-80 80z"></path></svg></div><span class="text-sm font-medium">Submit</span></button></div></div></div></div></div></div></div></div></div></div><div class="relative flex"><div class="relative flex overflow-hidden rounded bg-fill-tertiary dark:bg-fill-tertiary mr-[6px]"><div class="relative overflow-hidden transition-[width] ease-[cubic-bezier(0,1.5,.5,1)]" style="width: auto; transition-duration: 0.6s;"><div class="transition-[opacity] pointer-events-none absolute left-0 top-0 flex opacity-0"><div class="flex flex-none cursor-pointer items-center"><div class="flex flex-none"><div class="flex flex-none p-0.5 py-2 text-gray-60 dark:text-gray-60 hover:bg-fill-quaternary dark:hover:bg-fill-quaternary"><div class="relative text-[16px] leading-[normal] before:block before:h-4 before:w-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="angle-left" class="svg-inline--fa fa-angle-left absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path fill="currentColor" d="M47 239c-9.4 9.4-9.4 24.6 0 33.9L207 433c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9L97.9 256 241 113c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0L47 239z"></path></svg></div></div><div class="h-8 w-[1px] flex-none bg-layer-bg-gray dark:bg-layer-bg-gray"></div></div><div class="flex items-center hover:bg-fill-quaternary dark:hover:bg-fill-quaternary"><div class="flex flex-none py-2 pl-2 pr-1 text-gray-60 dark:text-gray-60"><div class="relative text-[16px] leading-[normal] before:block before:h-4 before:w-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="circle-play" class="svg-inline--fa fa-circle-play absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M464 256A208 208 0 1 0 48 256a208 208 0 1 0 416 0zM0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256zM188.3 147.1c7.6-4.2 16.8-4.1 24.3 .5l144 88c7.1 4.4 11.5 12.1 11.5 20.5s-4.4 16.1-11.5 20.5l-144 88c-7.4 4.5-16.7 4.7-24.3 .5s-12.3-12.2-12.3-20.9V168c0-8.7 4.7-16.7 12.3-20.9z"></path></svg></div></div><div class="select-none pr-2 text-sm text-text-secondary dark:text-text-secondary">00:00:00</div></div><div class="h-8 w-[1px] flex-none bg-layer-bg-gray dark:bg-layer-bg-gray"></div><div class="rounded-[3px] p-2 hover:bg-fill-quaternary dark:hover:bg-fill-quaternary text-gray-60 dark:text-gray-60" data-state="closed"><div class="relative text-[16px] leading-[normal] before:block before:h-4 before:w-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="arrows-rotate" class="svg-inline--fa fa-arrows-rotate absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M496 200c0 13.3-10.7 24-24 24h0H360 328c-13.3 0-24-10.7-24-24s10.7-24 24-24h32 54.1l-52.1-52.1C333.8 95.8 295.7 80 256 80c-72.7 0-135.2 44.1-162 107.1c-5.2 12.2-19.3 17.9-31.5 12.7s-17.9-19.3-12.7-31.5C83.9 88.2 163.4 32 256 32c52.5 0 102.8 20.8 139.9 57.9L448 142.1V88l0-.4V56c0-13.3 10.7-24 24-24s24 10.7 24 24V200zM40 288H152c13.3 0 24 10.7 24 24s-10.7 24-24 24H97.9l52.1 52.1C178.2 416.2 216.3 432 256 432c72.6 0 135-43.9 161.9-106.8c5.2-12.2 19.3-17.8 31.5-12.6s17.8 19.3 12.6 31.5C427.8 424 348.5 480 256 480c-52.5 0-102.8-20.8-139.9-57.9L64 369.9V424c0 13.3-10.7 24-24 24s-24-10.7-24-24V312c0-13.3 10.7-24 24-24z"></path></svg></div></div></div></div><div class="transition-[opacity]"><div class="flex flex-none cursor-pointer p-2 text-gray-60 dark:text-gray-60" data-state="closed"><div class="relative text-[16px] leading-[normal] before:block before:h-4 before:w-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="alarm-clock" class="svg-inline--fa fa-alarm-clock absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M160 25.4C143 9.6 120.2 0 95.2 0C42.6 0 0 42.6 0 95.2c0 18.8 5.5 36.3 14.9 51.1L160 25.4zM256 112a176 176 0 1 1 0 352 176 176 0 1 1 0-352zm0 400c53.2 0 102.1-18.6 140.5-49.5L439 505c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9l-42.5-42.5c31-38.4 49.5-87.3 49.5-140.5C480 164.3 379.7 64 256 64S32 164.3 32 288c0 53.2 18.6 102.1 49.5 140.5L39 471c-9.4 9.4-9.4 24.6 0 33.9s24.6 9.4 33.9 0l42.5-42.5c38.4 31 87.3 49.5 140.5 49.5zM497.1 146.4C506.5 131.6 512 114 512 95.2C512 42.6 469.4 0 416.8 0C391.8 0 369 9.6 352 25.4L497.1 146.4zM280 184c0-13.3-10.7-24-24-24s-24 10.7-24 24V288c0 6.4 2.5 12.5 7 17l48 48c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9l-41-41V184z"></path></svg></div></div></div></div></div><div class="relative flex overflow-hidden rounded bg-fill-tertiary dark:bg-fill-tertiary"><div class="group flex flex-none items-center justify-center hover:bg-fill-quaternary dark:hover:bg-fill-quaternary"><div class="flex cursor-pointer p-2 text-gray-60 dark:text-gray-60" data-state="closed"><div class="relative text-[16px] leading-[normal] before:block before:h-4 before:w-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="note-sticky" class="svg-inline--fa fa-note-sticky absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M64 80c-8.8 0-16 7.2-16 16V416c0 8.8 7.2 16 16 16H288V352c0-17.7 14.3-32 32-32h80V96c0-8.8-7.2-16-16-16H64zM288 480H64c-35.3 0-64-28.7-64-64V96C0 60.7 28.7 32 64 32H384c35.3 0 64 28.7 64 64V320v5.5c0 17-6.7 33.3-18.7 45.3l-90.5 90.5c-12 12-28.3 18.7-45.3 18.7H288z"></path></svg></div></div></div></div></div></div></div></div><div class="flex w-full flex-grow overflow-y-hidden p-[10px] pt-0"><div id="qd-content" class="relative flex h-full w-full"><div class="flexlayout__layout"><div id="fe5ce108-b325-4cb7-2f72-9b7be392da25" dir="ltr1" data-layout-path="/ts0" class="flexlayout__tabset" style="left: 0px; top: 0px; width: 754px; height: 671.594px; position: absolute;"><div class="flexlayout__tabset_tabbar_outer flexlayout__tabset_tabbar_outer_top flexlayout__tabset_tabbar_hover_show_toolbar" data-layout-path="/ts0/tabstrip" id="description_tabbar_outer" style="height: 36px;"><div class="flexlayout__tabset_tabbar_inner flexlayout__tabset_tabbar_inner_top"><div class="flexlayout__tabset_tabbar_inner_tab_container flexlayout__tabset_tabbar_inner_tab_container_top" style="left: 0px;"><div data-layout-path="/ts0/tb0" class="flexlayout__tab_button flexlayout__tab_button_top flexlayout__tab_button--selected"><div class="flexlayout__tab_button_content"><div class="relative flex items-center gap-1 overflow-hidden text-sm capitalize" id="description_tab" style="max-width: 150px;"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-blue-500"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="memo" class="svg-inline--fa fa-memo absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M64 48c-8.8 0-16 7.2-16 16V448c0 8.8 7.2 16 16 16H320c8.8 0 16-7.2 16-16V64c0-8.8-7.2-16-16-16H64zM0 64C0 28.7 28.7 0 64 0H320c35.3 0 64 28.7 64 64V448c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V64zm120 64H264c13.3 0 24 10.7 24 24s-10.7 24-24 24H120c-13.3 0-24-10.7-24-24s10.7-24 24-24zm0 96H264c13.3 0 24 10.7 24 24s-10.7 24-24 24H120c-13.3 0-24-10.7-24-24s10.7-24 24-24zm0 96h48c13.3 0 24 10.7 24 24s-10.7 24-24 24H120c-13.3 0-24-10.7-24-24s10.7-24 24-24z"></path></svg></div><div class="relative"><div class="medium whitespace-nowrap font-medium">Description</div><div class="normal absolute left-0 top-0 whitespace-nowrap font-normal">Description</div></div></div></div></div><div class="flexlayout__tabset_tab_divider"></div><div data-layout-path="/ts0/tb1" class="flexlayout__tab_button flexlayout__tab_button_top flexlayout__tab_button--unselected"><div class="flexlayout__tab_button_content"><div class="relative flex items-center gap-1 overflow-hidden text-sm capitalize" id="editorial_tab" style="max-width: 150px;"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-yellow-500"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="book-open" class="svg-inline--fa fa-book-open absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path fill="currentColor" d="M156 32C100.6 32 48.8 46.6 27.1 53.6C10.3 59 0 74.5 0 91.1V403.5c0 26.1 24 44.2 48 40.2c19.8-3.3 54.8-7.7 100-7.7c54 0 97.5 25.5 112.5 35.6c7.5 5 16.8 8.4 27 8.4c11.5 0 21.6-4.2 29.3-9.9C330.2 460.3 369.1 436 428 436c47.7 0 80.5 4 99 7.2c23.9 4.1 49-13.8 49-40.6V91.1c0-16.5-10.3-32.1-27.1-37.5C527.2 46.6 475.4 32 420 32c-36.8 0-71.8 6.4-97.4 12.7c-12.8 3.2-23.5 6.3-30.9 8.7c-1.3 .4-2.6 .8-3.7 1.2c-1.1-.4-2.4-.8-3.7-1.2c-7.5-2.4-18.1-5.5-30.9-8.7C227.8 38.4 192.8 32 156 32zM264 97.3V417.9C238 404.2 196.8 388 148 388c-42.9 0-77.4 3.7-100 7.1V97.3C70.3 90.6 112.4 80 156 80c31.6 0 62.6 5.6 85.9 11.3c8.6 2.1 16.1 4.2 22.1 6zm48 319.2V97.3c6-1.8 13.5-3.9 22.1-6C357.4 85.6 388.4 80 420 80c43.6 0 85.7 10.6 108 17.3V394.7c-21.7-3.3-54.9-6.7-100-6.7c-51.4 0-90.8 15-116 28.6z"></path></svg></div><div class="relative"><div class="medium whitespace-nowrap font-medium">Editorial</div><div class="normal absolute left-0 top-0 whitespace-nowrap font-normal">Editorial</div></div></div></div></div><div class="flexlayout__tabset_tab_divider"></div><div data-layout-path="/ts0/tb2" class="flexlayout__tab_button flexlayout__tab_button_top flexlayout__tab_button--unselected"><div class="flexlayout__tab_button_content"><div class="relative flex items-center gap-1 overflow-hidden text-sm capitalize" id="solutions_tab" style="max-width: 150px;"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-blue-500"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="flask" class="svg-inline--fa fa-flask absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M176 196.8c0 20.7-5.8 41-16.6 58.7L119.7 320H328.3l-39.7-64.5c-10.9-17.7-16.6-38-16.6-58.7V48H176V196.8zM320 48V196.8c0 11.8 3.3 23.5 9.5 33.5L437.7 406.2c6.7 10.9 10.3 23.5 10.3 36.4c0 38.3-31.1 69.4-69.4 69.4H69.4C31.1 512 0 480.9 0 442.6c0-12.8 3.6-25.4 10.3-36.4L118.5 230.4c6.2-10.1 9.5-21.7 9.5-33.5V48h-8c-13.3 0-24-10.7-24-24s10.7-24 24-24h40H288h40c13.3 0 24 10.7 24 24s-10.7 24-24 24h-8z"></path></svg></div><div class="relative"><div class="medium whitespace-nowrap font-medium">Solutions</div><div class="normal absolute left-0 top-0 whitespace-nowrap font-normal">Solutions</div></div></div></div></div><div class="flexlayout__tabset_tab_divider"></div><div data-layout-path="/ts0/tb3" class="flexlayout__tab_button flexlayout__tab_button_top flexlayout__tab_button--unselected"><div class="flexlayout__tab_button_content"><div class="relative flex items-center gap-1 overflow-hidden text-sm capitalize" id="submissions_tab" style="max-width: 150px;"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-blue-500"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="clock-rotate-left" class="svg-inline--fa fa-clock-rotate-left absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M48 106.7V56c0-13.3-10.7-24-24-24S0 42.7 0 56V168c0 13.3 10.7 24 24 24H136c13.3 0 24-10.7 24-24s-10.7-24-24-24H80.7c37-57.8 101.7-96 175.3-96c114.9 0 208 93.1 208 208s-93.1 208-208 208c-42.5 0-81.9-12.7-114.7-34.5c-11-7.3-25.9-4.3-33.3 6.7s-4.3 25.9 6.7 33.3C155.2 496.4 203.8 512 256 512c141.4 0 256-114.6 256-256S397.4 0 256 0C170.3 0 94.4 42.1 48 106.7zM256 128c-13.3 0-24 10.7-24 24V256c0 6.4 2.5 12.5 7 17l72 72c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9l-65-65V152c0-13.3-10.7-24-24-24z"></path></svg></div><div class="relative"><div class="medium whitespace-nowrap font-medium">Submissions</div><div class="normal absolute left-0 top-0 whitespace-nowrap font-normal">Submissions</div></div></div></div></div></div></div><div class="flexlayout__tab_toolbar"><div class="panel-right-btn flex space-x-1"><div data-state="closed"><button class="relative text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-sd-ring disabled:pointer-events-none disabled:opacity-50 text-sd-foreground hover:text-sd-accent-foreground rounded-sd-md hover:bg-fill-secondary dark:hover:bg-fill-secondary flex h-6 w-6 cursor-pointer items-center justify-center !rounded p-[5px] maximize"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 h-[14px] w-[14px] text-text-secondary dark:text-text-secondary"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="expand" class="svg-inline--fa fa-expand absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M136 32c13.3 0 24 10.7 24 24s-10.7 24-24 24H48v88c0 13.3-10.7 24-24 24s-24-10.7-24-24V56C0 42.7 10.7 32 24 32H136zM0 344c0-13.3 10.7-24 24-24s24 10.7 24 24v88h88c13.3 0 24 10.7 24 24s-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V344zM424 32c13.3 0 24 10.7 24 24V168c0 13.3-10.7 24-24 24s-24-10.7-24-24V80H312c-13.3 0-24-10.7-24-24s10.7-24 24-24H424zM400 344c0-13.3 10.7-24 24-24s24 10.7 24 24V456c0 13.3-10.7 24-24 24H312c-13.3 0-24-10.7-24-24s10.7-24 24-24h88V344z"></path></svg></div></button></div><div data-state="closed"><button class="relative text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-sd-ring disabled:pointer-events-none disabled:opacity-50 text-sd-foreground hover:text-sd-accent-foreground rounded-sd-md hover:bg-fill-secondary dark:hover:bg-fill-secondary flex h-6 w-6 cursor-pointer items-center justify-center !rounded p-[5px] fold"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 h-[14px] w-[14px] text-text-secondary dark:text-text-secondary"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="chevron-left" class="svg-inline--fa fa-chevron-left absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path fill="currentColor" d="M15 239c-9.4 9.4-9.4 24.6 0 33.9L207 465c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9L65.9 256 241 81c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0L15 239z"></path></svg></div></button></div></div><button data-layout-path="/ts0/button/max" title="Maximize tabset" class="flexlayout__tab_toolbar_button flexlayout__tab_toolbar_button-min"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="var(--color-icon)" style="width: 1em; height: 1em; display: flex; align-items: center;"><path d="M0 0h24v24H0z" fill="none"></path><path stroke="var(--color-icon)" d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"></path></svg></button></div></div><div class="flexlayout__tabset_content"></div></div><div id="fc3d2442-534b-3854-b4a6-986c17fd1086" dir="ltr1" data-layout-path="/c1/ts0" class="flexlayout__tabset flexlayout__tabset-active" style="left: 762px; top: 0px; width: 754px; height: 313px; position: absolute;"><div class="flexlayout__tabset_tabbar_outer flexlayout__tabset_tabbar_outer_top flexlayout__tabset-selected flexlayout__tabset_tabbar_hover_show_toolbar" data-layout-path="/c1/ts0/tabstrip" id="code_tabbar_outer" style="height: 36px;"><div class="flexlayout__tabset_tabbar_inner flexlayout__tabset_tabbar_inner_top"><div class="flexlayout__tabset_tabbar_inner_tab_container flexlayout__tabset_tabbar_inner_tab_container_top" style="left: 0px;"><div data-layout-path="/c1/ts0/tb0" class="flexlayout__tab_button flexlayout__tab_button_top flexlayout__tab_button--selected"><div class="flexlayout__tab_button_content"><div class="relative flex items-center gap-1 overflow-hidden text-sm capitalize" id="code_tab" style="max-width: 150px;"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-green-500"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="code" class="svg-inline--fa fa-code absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path fill="currentColor" d="M399.1 1.1c-12.7-3.9-26.1 3.1-30 15.8l-144 464c-3.9 12.7 3.1 26.1 15.8 30s26.1-3.1 30-15.8l144-464c3.9-12.7-3.1-26.1-15.8-30zm71.4 118.5c-9.1 9.7-8.6 24.9 1.1 33.9L580.9 256 471.6 358.5c-9.7 9.1-10.2 24.3-1.1 33.9s24.3 10.2 33.9 1.1l128-120c4.8-4.5 7.6-10.9 7.6-17.5s-2.7-13-7.6-17.5l-128-120c-9.7-9.1-24.9-8.6-33.9 1.1zm-301 0c-9.1-9.7-24.3-10.2-33.9-1.1l-128 120C2.7 243 0 249.4 0 256s2.7 13 7.6 17.5l128 120c9.7 9.1 24.9 8.6 33.9-1.1s8.6-24.9-1.1-33.9L59.1 256 168.4 153.5c9.7-9.1 10.2-24.3 1.1-33.9z"></path></svg></div><div class="relative"><div class="medium whitespace-nowrap font-medium">Code</div><div class="normal absolute left-0 top-0 whitespace-nowrap font-normal">Code</div></div></div></div></div></div></div><div class="flexlayout__tab_toolbar"><div class="panel-right-btn flex space-x-1"><div data-state="closed"><button class="relative text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-sd-ring disabled:pointer-events-none disabled:opacity-50 text-sd-foreground hover:text-sd-accent-foreground rounded-sd-md hover:bg-fill-secondary dark:hover:bg-fill-secondary flex h-6 w-6 cursor-pointer items-center justify-center !rounded p-[5px] maximize"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 h-[14px] w-[14px] text-text-secondary dark:text-text-secondary"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="expand" class="svg-inline--fa fa-expand absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M136 32c13.3 0 24 10.7 24 24s-10.7 24-24 24H48v88c0 13.3-10.7 24-24 24s-24-10.7-24-24V56C0 42.7 10.7 32 24 32H136zM0 344c0-13.3 10.7-24 24-24s24 10.7 24 24v88h88c13.3 0 24 10.7 24 24s-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V344zM424 32c13.3 0 24 10.7 24 24V168c0 13.3-10.7 24-24 24s-24-10.7-24-24V80H312c-13.3 0-24-10.7-24-24s10.7-24 24-24H424zM400 344c0-13.3 10.7-24 24-24s24 10.7 24 24V456c0 13.3-10.7 24-24 24H312c-13.3 0-24-10.7-24-24s10.7-24 24-24h88V344z"></path></svg></div></button></div><div data-state="closed"><button class="relative text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-sd-ring disabled:pointer-events-none disabled:opacity-50 text-sd-foreground hover:text-sd-accent-foreground rounded-sd-md hover:bg-fill-secondary dark:hover:bg-fill-secondary flex h-6 w-6 cursor-pointer items-center justify-center !rounded p-[5px] fold"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 h-[14px] w-[14px] text-text-secondary dark:text-text-secondary"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="chevron-up" class="svg-inline--fa fa-chevron-up absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M239 111c9.4-9.4 24.6-9.4 33.9 0L465 303c9.4 9.4 9.4 24.6 0 33.9s-24.6 9.4-33.9 0l-175-175L81 337c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9L239 111z"></path></svg></div></button></div></div><button data-layout-path="/c1/ts0/button/max" title="Maximize tabset" class="flexlayout__tab_toolbar_button flexlayout__tab_toolbar_button-min"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="var(--color-icon)" style="width: 1em; height: 1em; display: flex; align-items: center;"><path d="M0 0h24v24H0z" fill="none"></path><path stroke="var(--color-icon)" d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"></path></svg></button></div></div><div class="flexlayout__tabset_content"></div></div><div id="53f37308-30fe-1210-83ad-08211c8e2340" dir="ltr1" data-layout-path="/c1/ts1" class="flexlayout__tabset" style="left: 762px; top: 321px; width: 754px; height: 350px; position: absolute;"><div class="flexlayout__tabset_tabbar_outer flexlayout__tabset_tabbar_outer_top flexlayout__tabset_tabbar_hover_show_toolbar" data-layout-path="/c1/ts1/tabstrip" id="result_tabbar_outer" style="height: 36px;"><div class="flexlayout__tabset_tabbar_inner flexlayout__tabset_tabbar_inner_top"><div class="flexlayout__tabset_tabbar_inner_tab_container flexlayout__tabset_tabbar_inner_tab_container_top" style="left: 0px;"><div data-layout-path="/c1/ts1/tb0" class="flexlayout__tab_button flexlayout__tab_button_top flexlayout__tab_button--unselected"><div class="flexlayout__tab_button_content"><div class="relative flex items-center gap-1 overflow-hidden text-sm capitalize" id="testcase_tab" style="max-width: 150px;"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-green-500"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="square-check" class="svg-inline--fa fa-square-check absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M64 80c-8.8 0-16 7.2-16 16V416c0 8.8 7.2 16 16 16H384c8.8 0 16-7.2 16-16V96c0-8.8-7.2-16-16-16H64zM0 96C0 60.7 28.7 32 64 32H384c35.3 0 64 28.7 64 64V416c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V96zM337 209L209 337c-9.4 9.4-24.6 9.4-33.9 0l-64-64c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0l47 47L303 175c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9z"></path></svg></div><div class="relative"><div class="medium whitespace-nowrap font-medium">Testcase</div><div class="normal absolute left-0 top-0 whitespace-nowrap font-normal">Testcase</div></div></div></div></div><div class="flexlayout__tabset_tab_divider"></div><div data-layout-path="/c1/ts1/tb1" class="flexlayout__tab_button flexlayout__tab_button_top flexlayout__tab_button--selected"><div class="flexlayout__tab_button_content"><div class="relative flex items-center gap-1 overflow-hidden text-sm capitalize" id="result_tab" style="max-width: 150px;"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-green-500"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="terminal" class="svg-inline--fa fa-terminal absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path fill="currentColor" d="M6.3 72.2c-9-9.8-8.3-24.9 1.4-33.9s24.9-8.3 33.9 1.4l184 200c8.5 9.2 8.5 23.3 0 32.5l-184 200c-9 9.8-24.2 10.4-33.9 1.4s-10.4-24.2-1.4-33.9L175.4 256 6.3 72.2zM248 432H552c13.3 0 24 10.7 24 24s-10.7 24-24 24H248c-13.3 0-24-10.7-24-24s10.7-24 24-24z"></path></svg></div><div class="relative"><div class="medium whitespace-nowrap font-medium">Test Result</div><div class="normal absolute left-0 top-0 whitespace-nowrap font-normal">Test Result</div></div></div></div></div></div></div><div class="flexlayout__tab_toolbar"><div class="panel-right-btn flex space-x-1"><div data-state="closed"><button class="relative text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-sd-ring disabled:pointer-events-none disabled:opacity-50 text-sd-foreground hover:text-sd-accent-foreground rounded-sd-md hover:bg-fill-secondary dark:hover:bg-fill-secondary flex h-6 w-6 cursor-pointer items-center justify-center !rounded p-[5px] maximize"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 h-[14px] w-[14px] text-text-secondary dark:text-text-secondary"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="expand" class="svg-inline--fa fa-expand absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M136 32c13.3 0 24 10.7 24 24s-10.7 24-24 24H48v88c0 13.3-10.7 24-24 24s-24-10.7-24-24V56C0 42.7 10.7 32 24 32H136zM0 344c0-13.3 10.7-24 24-24s24 10.7 24 24v88h88c13.3 0 24 10.7 24 24s-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V344zM424 32c13.3 0 24 10.7 24 24V168c0 13.3-10.7 24-24 24s-24-10.7-24-24V80H312c-13.3 0-24-10.7-24-24s10.7-24 24-24H424zM400 344c0-13.3 10.7-24 24-24s24 10.7 24 24V456c0 13.3-10.7 24-24 24H312c-13.3 0-24-10.7-24-24s10.7-24 24-24h88V344z"></path></svg></div></button></div><div data-state="closed"><button class="relative text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-sd-ring disabled:pointer-events-none disabled:opacity-50 text-sd-foreground hover:text-sd-accent-foreground rounded-sd-md hover:bg-fill-secondary dark:hover:bg-fill-secondary flex h-6 w-6 cursor-pointer items-center justify-center !rounded p-[5px] fold"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 h-[14px] w-[14px] text-text-secondary dark:text-text-secondary"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="chevron-up" class="svg-inline--fa fa-chevron-up absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M239 111c9.4-9.4 24.6-9.4 33.9 0L465 303c9.4 9.4 9.4 24.6 0 33.9s-24.6 9.4-33.9 0l-175-175L81 337c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9L239 111z"></path></svg></div></button></div></div><button data-layout-path="/c1/ts1/button/max" title="Maximize tabset" class="flexlayout__tab_toolbar_button flexlayout__tab_toolbar_button-min"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="var(--color-icon)" style="width: 1em; height: 1em; display: flex; align-items: center;"><path d="M0 0h24v24H0z" fill="none"></path><path stroke="var(--color-icon)" d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"></path></svg></button></div></div><div class="flexlayout__tabset_content"></div></div><div class="flexlayout__tab" data-layout-path="/ts0/t0" id="b3538c3e-3332-a38a-4a06-a1db6315cf81" style="left: 0px; top: 36px; position: absolute; --width: 754px; --height: 635.59375px;"><div class="flex h-full w-full flex-col"><div class="flex w-full flex-1 flex-col gap-4 overflow-y-auto px-4 py-5"><div class="flex items-start justify-between gap-4"><div class="flex items-start gap-2"><div class="text-title-large font-semibold text-text-primary dark:text-text-primary"><a class="no-underline hover:text-blue-s dark:hover:text-dark-blue-s truncate cursor-text whitespace-normal hover:!text-[inherit]" href="https://leetcode.com/problems/running-sum-of-1d-array/">1480. Running Sum of 1d Array</a><div class="text-body ml-2 inline-flex items-center gap-2 py-1"><div class="inline-flex items-center space-x-2"></div></div></div></div><div class="text-body flex flex-none items-center gap-1 py-1.5 text-text-secondary dark:text-text-secondary">Solved<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14 14" width="1em" height="1em" fill="currentColor" class="fill-none stroke-current text-message-success dark:text-message-success"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.2" d="M12.598 7a5.6 5.6 0 11-3.15-5.037m2.1 1.537l-4.9 4.9-1.4-1.4"></path></svg></div></div><div class="flex gap-1"><div class="relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-difficulty-easy dark:text-difficulty-easy">Easy</div><div class="relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary cursor-pointer transition-colors hover:bg-fill-primary hover:text-text-primary text-sd-secondary-foreground hover:opacity-80"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 h-3.5 w-3.5 fill-none stroke-current"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="tag" class="svg-inline--fa fa-tag absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M197.5 32c17 0 33.3 6.7 45.3 18.7l176 176c25 25 25 65.5 0 90.5L285.3 450.7c-25 25-65.5 25-90.5 0l-176-176C6.7 262.7 0 246.5 0 229.5V80C0 53.5 21.5 32 48 32H197.5zM48 229.5c0 4.2 1.7 8.3 4.7 11.3l176 176c6.2 6.2 16.4 6.2 22.6 0L384.8 283.3c6.2-6.2 6.2-16.4 0-22.6l-176-176c-3-3-7.1-4.7-11.3-4.7H48V229.5zM112 112a32 32 0 1 1 0 64 32 32 0 1 1 0-64z"></path></svg></div>Topics</div><div class="relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary cursor-pointer transition-colors hover:bg-fill-primary hover:text-text-primary text-sd-secondary-foreground hover:opacity-80"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-3.5 w-3.5"><path fill-rule="evenodd" d="M7 8v2H6a3 3 0 00-3 3v6a3 3 0 003 3h12a3 3 0 003-3v-6a3 3 0 00-3-3h-1V8A5 5 0 007 8zm8 0v2H9V8a3 3 0 116 0zm-3 6a2 2 0 100 4 2 2 0 000-4z" clip-rule="evenodd"></path></svg>Companies</div><div class="relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary cursor-pointer transition-colors hover:bg-fill-primary hover:text-text-primary text-sd-secondary-foreground hover:opacity-80"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 h-3.5 w-3.5 fill-none stroke-current"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="lightbulb" class="svg-inline--fa fa-lightbulb absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M297.2 248.9C311.6 228.3 320 203.2 320 176c0-70.7-57.3-128-128-128S64 105.3 64 176c0 27.2 8.4 52.3 22.8 72.9c3.7 5.3 8.1 11.3 12.8 17.7l0 0c12.9 17.7 28.3 38.9 39.8 59.8c10.4 19 15.7 38.8 18.3 57.5H109c-2.2-12-5.9-23.7-11.8-34.5c-9.9-18-22.2-34.9-34.5-51.8l0 0 0 0c-5.2-7.1-10.4-14.2-15.4-21.4C27.6 247.9 16 213.3 16 176C16 78.8 94.8 0 192 0s176 78.8 176 176c0 37.3-11.6 71.9-31.4 100.3c-5 7.2-10.2 14.3-15.4 21.4l0 0 0 0c-12.3 16.8-24.6 33.7-34.5 51.8c-5.9 10.8-9.6 22.5-11.8 34.5H226.4c2.6-18.7 7.9-38.6 18.3-57.5c11.5-20.9 26.9-42.1 39.8-59.8l0 0 0 0 0 0c4.7-6.4 9-12.4 12.7-17.7zM192 128c-26.5 0-48 21.5-48 48c0 8.8-7.2 16-16 16s-16-7.2-16-16c0-44.2 35.8-80 80-80c8.8 0 16 7.2 16 16s-7.2 16-16 16zm0 384c-44.2 0-80-35.8-80-80V416H272v16c0 44.2-35.8 80-80 80z"></path></svg></div>Hint</div></div><div><div class="elfjS" data-track-load="description_content"><p>Given an array <code>nums</code>. We define a running sum of an array as&nbsp;<code>runningSum[i] = sum(nums[0]…nums[i])</code>.</p>

<p>Return the running sum of <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [1,3,6,10]
<strong>Explanation:</strong> Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,1,1,1]
<strong>Output:</strong> [1,2,3,4,5]
<strong>Explanation:</strong> Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,2,10,1]
<strong>Output:</strong> [3,4,6,16,17]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10^6&nbsp;&lt;= nums[i] &lt;=&nbsp;10^6</code></li>
</ul>
</div></div><div class="mt-6 flex flex-col gap-3"><div class="group/ads flex w-full items-start justify-start"><div class="group-hover/ads:bg-sd-muted relative overflow-hidden transition-colors group-hover/ads:before:text-sd-muted-foreground/50 before:absolute before:left-1/2 before:top-1/2 before:-translate-x-1/2 before:-translate-y-1/2 before:text-transparent before:transition-colors before:content-[&#39;Advertisement&#39;]"><div style="width: 468px; height: 60px;"></div></div><div class="bg-sd-muted text-sd-muted-foreground h-6 w-6 flex-none cursor-pointer p-1 opacity-0 transition-opacity group-hover/ads:opacity-100" type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1p:" data-state="closed"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5"><svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="xmark" class="svg-inline--fa fa-xmark absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"></path></svg></div></div></div><hr class="border-divider-3 dark:border-dark-divider-3"><div><div class="mb-2 flex items-center space-x-4"><div class="text-label-2 dark:text-dark-label-2 text-md">Seen this question in a real interview before?</div><div class="text-label-3 dark:text-dark-label-3 text-md font-medium">1/5</div></div><div class="flex"><div class="py-1 px-2 cursor-pointer text-xs mr-3 rounded-[12px] text-label-2 dark:text-dark-label-2 bg-fill-3 dark:bg-dark-fill-3 hover:bg-fill-2 dark:hover:bg-dark-fill-2" data-has-seen="true">Yes</div><div class="py-1 px-2 cursor-pointer text-xs mr-3 rounded-[12px] text-label-2 dark:text-dark-label-2 bg-fill-3 dark:bg-dark-fill-3 hover:bg-fill-2 dark:hover:bg-dark-fill-2">No</div></div></div><div class="flex flex-wrap items-center"><div class="mr-4 flex items-center space-x-2.5"><div class="text-label-2 dark:text-dark-label-2 text-xs">Accepted</div><div class="text-label-1 dark:text-dark-label-1 text-sm font-medium">1.9M</div></div><div class="bg-divider-2 dark:bg-dark-divider-2 h-full w-px border-divider-1 dark:border-dark-divider-1 mr-4 max-h-[14px]"></div><div class="mr-4 flex items-center space-x-2.5"><div class="text-label-2 dark:text-dark-label-2 text-xs">Submissions</div><div class="text-label-1 dark:text-dark-label-1 text-sm font-medium">2.2M</div></div><div class="bg-divider-2 dark:bg-dark-divider-2 h-full w-px border-divider-1 dark:border-dark-divider-1 mr-4 max-h-[14px]"></div><div class="mr-4 flex items-center space-x-2.5"><div class="text-label-2 dark:text-dark-label-2 text-xs">Acceptance Rate</div><div class="text-label-1 dark:text-dark-label-1 text-sm font-medium"><span class="text-md font-medium">86.9%</span></div></div></div><hr class="border-divider-3 dark:border-dark-divider-3"><div><div class="flex flex-col"><div class="group flex cursor-pointer items-center transition-colors text-label-2 dark:text-dark-label-2 hover:text-label-1 dark:hover:text-dark-label-1"><div class="flex-1 text-sm leading-[22px]"><div class="text-sd-foreground flex items-center gap-2"><div class="relative text-[16px] leading-[normal] p-0.5 before:block before:h-4 before:w-4 text-sd-foreground fill-none stroke-current"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="tag" class="svg-inline--fa fa-tag absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M197.5 32c17 0 33.3 6.7 45.3 18.7l176 176c25 25 25 65.5 0 90.5L285.3 450.7c-25 25-65.5 25-90.5 0l-176-176C6.7 262.7 0 246.5 0 229.5V80C0 53.5 21.5 32 48 32H197.5zM48 229.5c0 4.2 1.7 8.3 4.7 11.3l176 176c6.2 6.2 16.4 6.2 22.6 0L384.8 283.3c6.2-6.2 6.2-16.4 0-22.6l-176-176c-3-3-7.1-4.7-11.3-4.7H48V229.5zM112 112a32 32 0 1 1 0 64 32 32 0 1 1 0-64z"></path></svg></div><div class="text-body text-text-primary dark:text-text-primary">Topics</div></div></div><div class="text-[24px] transition-colors text-gray-4 dark:text-dark-gray-4 group-hover:text-gray-5 dark:group-hover:text-dark-gray-5"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="origin-center transition-transform"><path fill-rule="evenodd" d="M16.293 9.293a1 1 0 111.414 1.414l-5 5a1 1 0 01-1.414 0l-5-5a1 1 0 011.414-1.414L12 13.586l4.293-4.293z" clip-rule="evenodd"></path></svg></div></div><div class="overflow-hidden transition-all" style="height: 0px; transition-duration: 0.25s;"><div class="mt-2 flex flex-wrap gap-1 pl-7"><a target="_blank" rel="noopener noreferrer" class="no-underline hover:text-current relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-text-secondary" href="https://leetcode.com/tag/array/">Array</a><a target="_blank" rel="noopener noreferrer" class="no-underline hover:text-current relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-text-secondary" href="https://leetcode.com/tag/prefix-sum/">Prefix Sum</a></div></div></div></div><hr class="border-divider-3 dark:border-dark-divider-3"><div><div class="flex flex-col"><div class="group flex cursor-pointer items-center transition-colors text-label-2 dark:text-dark-label-2 hover:text-label-1 dark:hover:text-dark-label-1"><div class="flex-1 text-sm leading-[22px]"><div class="ext-sd-foreground text-sd-foreground flex items-center gap-2"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-4 w-4"><path fill-rule="evenodd" d="M7 8v2H6a3 3 0 00-3 3v6a3 3 0 003 3h12a3 3 0 003-3v-6a3 3 0 00-3-3h-1V8A5 5 0 007 8zm8 0v2H9V8a3 3 0 116 0zm-3 6a2 2 0 100 4 2 2 0 000-4z" clip-rule="evenodd"></path></svg><div class="text-body">Companies</div></div></div><div class="text-[24px] transition-colors text-gray-4 dark:text-dark-gray-4 group-hover:text-gray-5 dark:group-hover:text-dark-gray-5"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="origin-center transition-transform"><path fill-rule="evenodd" d="M16.293 9.293a1 1 0 111.414 1.414l-5 5a1 1 0 01-1.414 0l-5-5a1 1 0 011.414-1.414L12 13.586l4.293-4.293z" clip-rule="evenodd"></path></svg></div></div><div class="overflow-hidden transition-all" style="height: 0px; transition-duration: 0.25s;"><div class="mt-2 flex flex-col gap-3 pl-7"></div></div></div></div><hr class="border-divider-3 dark:border-dark-divider-3"><div><div class="flex flex-col"><div class="group flex cursor-pointer items-center transition-colors text-label-2 dark:text-dark-label-2 hover:text-label-1 dark:hover:text-dark-label-1"><div class="flex-1 text-sm leading-[22px]"><div class="text-sd-foreground flex items-center gap-2"><div class="relative text-[16px] leading-[normal] p-0.5 before:block before:h-4 before:w-4 fill-none stroke-current"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="lightbulb" class="svg-inline--fa fa-lightbulb absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M297.2 248.9C311.6 228.3 320 203.2 320 176c0-70.7-57.3-128-128-128S64 105.3 64 176c0 27.2 8.4 52.3 22.8 72.9c3.7 5.3 8.1 11.3 12.8 17.7l0 0c12.9 17.7 28.3 38.9 39.8 59.8c10.4 19 15.7 38.8 18.3 57.5H109c-2.2-12-5.9-23.7-11.8-34.5c-9.9-18-22.2-34.9-34.5-51.8l0 0 0 0c-5.2-7.1-10.4-14.2-15.4-21.4C27.6 247.9 16 213.3 16 176C16 78.8 94.8 0 192 0s176 78.8 176 176c0 37.3-11.6 71.9-31.4 100.3c-5 7.2-10.2 14.3-15.4 21.4l0 0 0 0c-12.3 16.8-24.6 33.7-34.5 51.8c-5.9 10.8-9.6 22.5-11.8 34.5H226.4c2.6-18.7 7.9-38.6 18.3-57.5c11.5-20.9 26.9-42.1 39.8-59.8l0 0 0 0 0 0c4.7-6.4 9-12.4 12.7-17.7zM192 128c-26.5 0-48 21.5-48 48c0 8.8-7.2 16-16 16s-16-7.2-16-16c0-44.2 35.8-80 80-80c8.8 0 16 7.2 16 16s-7.2 16-16 16zm0 384c-44.2 0-80-35.8-80-80V416H272v16c0 44.2-35.8 80-80 80z"></path></svg></div><div class="text-body">Hint 1</div></div></div><div class="text-[24px] transition-colors text-gray-4 dark:text-dark-gray-4 group-hover:text-gray-5 dark:group-hover:text-dark-gray-5"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="origin-center transition-transform"><path fill-rule="evenodd" d="M16.293 9.293a1 1 0 111.414 1.414l-5 5a1 1 0 01-1.414 0l-5-5a1 1 0 011.414-1.414L12 13.586l4.293-4.293z" clip-rule="evenodd"></path></svg></div></div><div class="overflow-hidden transition-all" style="height: 0px; transition-duration: 0.25s;"><div class="text-body text-sd-foreground mt-2 pl-7 elfjS">Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.</div></div></div></div><hr class="border-divider-3 dark:border-dark-divider-3"><div><div class="flex flex-col"><div class="group flex cursor-pointer items-center transition-colors text-label-2 dark:text-dark-label-2 hover:text-label-1 dark:hover:text-dark-label-1"><div class="flex-1 text-sm leading-[22px]"><div class="text-sd-foreground flex items-center gap-2"><div class="relative text-[16px] leading-[normal] p-0.5 before:block before:h-4 before:w-4 fill-none stroke-current"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="comment" class="svg-inline--fa fa-comment absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M123.6 391.3c12.9-9.4 29.6-11.8 44.6-6.4c26.5 9.6 56.2 15.1 87.8 15.1c124.7 0 208-80.5 208-160s-83.3-160-208-160S48 160.5 48 240c0 32 12.4 62.8 35.7 89.2c8.6 9.7 12.8 22.5 11.8 35.5c-1.4 18.1-5.7 34.7-11.3 49.4c17-7.9 31.1-16.7 39.4-22.7zM21.2 431.9c1.8-2.7 3.5-5.4 5.1-8.1c10-16.6 19.5-38.4 21.4-62.9C17.7 326.8 0 285.1 0 240C0 125.1 114.6 32 256 32s256 93.1 256 208s-114.6 208-256 208c-37.1 0-72.3-6.4-104.1-17.9c-11.9 8.7-31.3 20.6-54.3 30.6c-15.1 6.6-32.3 12.6-50.1 16.1c-.8 .2-1.6 .3-2.4 .5c-4.4 .8-8.7 1.5-13.2 1.9c-.2 0-.5 .1-.7 .1c-5.1 .5-10.2 .8-15.3 .8c-6.5 0-12.3-3.9-14.8-9.9c-2.5-6-1.1-12.8 3.4-17.4c4.1-4.2 7.8-8.7 11.3-13.5c1.7-2.3 3.3-4.6 4.8-6.9c.1-.2 .2-.3 .3-.5z"></path></svg></div><div class="text-body">Discussion (132)</div></div></div><div class="text-[24px] transition-colors text-gray-4 dark:text-dark-gray-4 group-hover:text-gray-5 dark:group-hover:text-dark-gray-5"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="origin-center transition-transform"><path fill-rule="evenodd" d="M16.293 9.293a1 1 0 111.414 1.414l-5 5a1 1 0 01-1.414 0l-5-5a1 1 0 011.414-1.414L12 13.586l4.293-4.293z" clip-rule="evenodd"></path></svg></div></div><div class="overflow-hidden transition-all" style="height: 0px; transition-duration: 0.25s;"><div class="mt-2 flex flex-col"><div class="flex h-full flex-col px-1"><div class="mt-3"><div><div class="relative"><div class="flex w-full flex-col rounded-[13px] bg-layer-2 dark:bg-dark-layer-2 shadow-level1 dark:shadow-dark-level1"><textarea data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false" placeholder="Type comment here... (Markdown supported)" class="w-full resize-none bg-transparent p-4 text-md outline-0 outline-none dark:bg-transparent min-h-[80px] placeholder:text-label-4 dark:placeholder:text-dark-label-4 inherit" rows="1" style="overflow: hidden; overflow-wrap: break-word; height: 80px;"></textarea><div class="relative box-content flex h-8 items-end p-4"><div class="flex flex-1 flex-col"><div class="absolute top-0"><div class="relative flex items-center space-x-2"><div class="relative" data-headlessui-state=""><button class="flex items-center rounded text-left cursor-pointer focus:outline-none whitespace-nowrap leading-5 bg-transparent dark:bg-dark-transparent active:bg-transparent dark:active:bg-dark-transparent hover:bg-transparent dark:hover:bg-dark-transparent text-blue-s dark:text-dark-blue-s p-0" id="headlessui-menu-button-:r1q:" type="button" aria-haspopup="true" aria-expanded="false" data-headlessui-state=""><div class="text-blue-s dark:text-dark-blue-s text-xs font-medium">Choose a type</div><div class="flex items-center pointer-events-none transition duration-300 text-label-3 dark:text-dark-label-3 w-4 h-4 ml-0.5" aria-hidden="true"><div class="text-blue-s dark:text-dark-blue-s text-xs font-medium"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor"><path fill-rule="evenodd" d="M16.293 9.293a1 1 0 111.414 1.414l-5 5a1 1 0 01-1.414 0l-5-5a1 1 0 011.414-1.414L12 13.586l4.293-4.293z" clip-rule="evenodd"></path></svg></div></div></button></div></div></div><div class="flex h-8 items-end gap-2 inherit"><div class="flex cursor-pointer items-center rounded-[5px] p-1 text-base text-gray-7 dark:text-dark-gray-7 hover:bg-fill-4 dark:hover:bg-dark-fill-4"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor"><path fill-rule="evenodd" d="M13.27 5.02c.456.1.764.562.727 1.06l-.015.116-2.181 12c-.099.541-.578.893-1.07.784-.457-.1-.765-.562-.728-1.06l.015-.116 2.181-12c.099-.541.578-.893 1.07-.784zm4.65.37l.07.096 3.857 6c.178.277.2.614.067.906l-.067.123-3.857 6c-.304.473-.962.627-1.47.342-.47-.264-.646-.812-.425-1.268l.058-.104L19.678 12l-3.525-5.485c-.283-.44-.161-1.001.264-1.307l.103-.065a1.123 1.123 0 011.4.246zm-11.84 0c.3-.365.83-.49 1.28-.305l.12.058.103.065a.96.96 0 01.326 1.194l-.062.113L4.322 12l3.525 5.485.058.104c.221.456.046 1.005-.425 1.268a1.123 1.123 0 01-1.4-.246l-.07-.097-3.857-6-.067-.122a.939.939 0 010-.784l.067-.123 3.857-6 .07-.096z" clip-rule="evenodd"></path></svg></div><div class="flex cursor-pointer items-center rounded-[5px] p-1 text-base text-gray-7 dark:text-dark-gray-7 hover:bg-fill-4 dark:hover:bg-dark-fill-4"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor"><path fill-rule="evenodd" d="M13 7a1 1 0 011-1h2a6 6 0 010 12h-2a1 1 0 110-2h2a4 4 0 000-8h-2a1 1 0 01-1-1zm-3 10a1 1 0 01-1 1H8A6 6 0 018 6h1a1 1 0 010 2H8a4 4 0 100 8h1a1 1 0 011 1zm-1-6h6a1 1 0 110 2H9a1 1 0 110-2z" clip-rule="evenodd"></path></svg></div><div class="flex cursor-pointer items-center rounded-[5px] p-1 text-base text-gray-7 dark:text-dark-gray-7 hover:bg-fill-4 dark:hover:bg-dark-fill-4"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18" width="1em" height="1em" fill="currentColor"><path d="M11.27 6.799l.146-.438c.075-.259.178-.437.308-.534.14-.108.345-.06.615.145.065.054.124.114.178.179a.45.45 0 01.114.226.976.976 0 01.032.373 2.21 2.21 0 01-.13.535l-1.182 3.434c-.054.151-.043.28.032.389a.399.399 0 00.308.146c.087 0 .232-.081.438-.243.205-.173.41-.405.615-.697.216-.292.405-.637.567-1.037a3.63 3.63 0 00.243-1.344c0-.519-.108-1-.324-1.442a3.458 3.458 0 00-.907-1.15 4.033 4.033 0 00-1.345-.778 4.76 4.76 0 00-1.684-.292 4.55 4.55 0 00-1.766.373 5.343 5.343 0 00-2.77 2.738c-.292.659-.438 1.393-.438 2.203 0 .691.13 1.296.389 1.814.26.519.616.95 1.07 1.296.453.335.982.589 1.587.762a7.555 7.555 0 001.96.243 9.97 9.97 0 001.328-.081c.4-.054.783-.151 1.15-.292a5.269 5.269 0 001.07-.6c.345-.258.707-.582 1.085-.971.076-.108.162-.162.26-.162.107-.011.21.01.307.065a.567.567 0 01.243.21.5.5 0 01.13.276.857.857 0 01-.081.55c-.076.162-.26.378-.551.648-.292.27-.61.524-.956.762a6.538 6.538 0 01-1.118.632c-.4.172-.837.307-1.312.405a7.016 7.016 0 01-1.555.162 8.817 8.817 0 01-2.527-.324 6.147 6.147 0 01-2.122-1.021 5.098 5.098 0 01-1.442-1.814c-.357-.735-.535-1.61-.535-2.625 0-1.09.19-2.057.567-2.9.389-.853.891-1.566 1.507-2.138a6.371 6.371 0 012.09-1.328A6.646 6.646 0 019.26 2.7c.875 0 1.674.13 2.398.389.734.259 1.36.62 1.879 1.085.518.465.918 1.02 1.199 1.669.291.648.437 1.36.437 2.138 0 .627-.119 1.237-.356 1.83a5.638 5.638 0 01-.94 1.556c-.389.454-.826.82-1.312 1.102-.486.27-.977.405-1.474.405-.378 0-.675-.087-.891-.26-.216-.172-.378-.437-.486-.793-.346.28-.637.496-.875.648-.238.15-.545.221-.923.21-.443-.01-.8-.102-1.07-.275a1.905 1.905 0 01-.631-.648 2.547 2.547 0 01-.308-.859 5.625 5.625 0 01-.081-.923c0-.465.092-.967.275-1.507.195-.55.46-1.053.794-1.506a4.519 4.519 0 011.247-1.15 2.928 2.928 0 011.62-.47c.227 0 .422.037.584.113.172.076.313.184.42.324.12.13.217.286.292.47.076.173.146.356.211.55zm-2.657 4.374c.324 0 .637-.12.94-.357.313-.248.578-.723.794-1.425.14-.432.243-.746.307-.94.065-.205.103-.373.114-.502.01-.205-.07-.389-.243-.551-.173-.173-.357-.26-.551-.26-.346 0-.659.087-.94.26-.27.173-.502.394-.696.664a3.53 3.53 0 00-.438.907 3.563 3.563 0 00-.178.972c0 .476.092.8.276.972.183.173.388.26.615.26z"></path></svg></div></div></div><div class="flex items-center gap-4"><button disabled="" class="font-medium items-center whitespace-nowrap focus:outline-none opacity-50 inline-flex transition-colors py-[5px] px-3 rounded-lg text-label-3 dark:text-dark-label-3 cursor-not-allowed bg-transparent hover:!bg-transparent dark:bg-transparent">Preview</button><button disabled="" class="font-medium items-center whitespace-nowrap focus:outline-none opacity-50 inline-flex transition-colors cursor-pointer py-[5px] px-3 rounded-lg bg-green-s dark:bg-dark-green-s hover:bg-green-3 dark:hover:bg-dark-green-3 text-white dark:text-dark-white opacty-100">Comment</button></div></div></div><div class="z-base-1 absolute box-content rounded-lg hidden"></div></div></div></div><div class="mt-3"><div class="w-full rounded-[13px] border p-4 bg-fill-4 dark:bg-dark-fill-4 border-divider-4 dark:border-dark-divider-4 mb-3"><div class="flex w-full flex-col items-start gap-3"><div class="flex w-full items-center justify-between"><div class="font-medium text-label-1 dark:text-dark-label-1">💡 Discussion Rules</div><div class="cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-4 w-4 text-gray-6 dark:text-dark-gray-6 hover:text-gray-7 dark:hover:text-dark-gray-7"><path fill-rule="evenodd" d="M13.414 12L19 17.586A1 1 0 0117.586 19L12 13.414 6.414 19A1 1 0 015 17.586L10.586 12 5 6.414A1 1 0 116.414 5L12 10.586 17.586 5A1 1 0 1119 6.414L13.414 12z" clip-rule="evenodd"></path></svg></div></div><div class="flex w-full flex-col items-start gap-4 text-xs text-label-2 dark:text-dark-label-2"><p>1. Please don't post <b>any solutions</b> in this discussion.</p><p>2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.</p><p>3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.</p></div></div></div><div class="pt-3"><div class="flex items-center space-x-2"><div class="relative" data-headlessui-state=""><button class="flex items-center rounded text-left cursor-pointer focus:outline-none whitespace-nowrap leading-5 p-0 bg-transparent dark:bg-transparent hover:bg-transparent dark:hover:bg-transparent active:bg-transparent dark:active:bg-transparent text-label-2 dark:text-dark-label-2" id="headlessui-menu-button-:r1r:" type="button" aria-haspopup="true" aria-expanded="false" data-headlessui-state=""><div class="text-xs text-label-2 dark:text-dark-label-2"><span class="mr-2">Sort by:</span><span class="text-label-1 dark:text-dark-label-1 font-medium">Best</span></div><div class="w-4.5 h-4.5 flex items-center ml-3 pointer-events-none transition duration-300 text-label-3 dark:text-dark-label-3" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor"><path fill-rule="evenodd" d="M16.293 9.293a1 1 0 111.414 1.414l-5 5a1 1 0 01-1.414 0l-5-5a1 1 0 011.414-1.414L12 13.586l4.293-4.293z" clip-rule="evenodd"></path></svg></div></button></div></div></div></div><div class="mt-4 flex-1"><div class="w-full p-5 text-center text-label-4 dark:text-dark-label-4">No comments yet.</div></div><div class="mb-4 mt-7 flex justify-center pb-4"><nav role="navigation" class="flex flex-nowrap items-center space-x-2"><button class="flex items-center justify-center h-8 rounded select-none focus:outline-none bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2 disabled:opacity-40 disabled:pointer-events-none text-sm px-2" aria-label="prev" disabled=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="text-label-2 dark:text-dark-label-2 w-4 h-4"><path fill-rule="evenodd" d="M16.091 4.929l-7.057 7.078 7.057 7.064a1 1 0 01-1.414 1.414l-7.764-7.77a1 1 0 010-1.415l7.764-7.785a1 1 0 111.415 1.414z" clip-rule="evenodd"></path></svg></button><button class="flex items-center justify-center px-3 h-8 rounded select-none focus:outline-none pointer-events-none bg-paper dark:bg-dark-gray-5 text-label-1 dark:text-dark-label-1 shadow-level1 dark:shadow-dark-level1 text-sm">1</button><button class="flex items-center justify-center px-3 h-8 rounded select-none focus:outline-none bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-sm">2</button><button class="flex items-center justify-center px-3 h-8 rounded select-none focus:outline-none bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-sm">3</button><button class="flex items-center justify-center px-3 h-8 rounded select-none focus:outline-none bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-sm">4</button><button class="flex items-center justify-center px-3 h-8 rounded select-none focus:outline-none bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-sm">5</button><button class="flex items-center justify-center px-3 h-8 rounded select-none focus:outline-none bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-sm">6</button><button class="flex items-center justify-center px-3 h-8 rounded select-none focus:outline-none bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2 disabled:opacity-40 disabled:pointer-events-none text-sm" aria-label="gap" disabled=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="text-label-2 dark:text-dark-label-2"><path fill-rule="evenodd" d="M4.4 14a2 2 0 100-4 2 2 0 000 4zm9.6-2a2 2 0 11-4 0 2 2 0 014 0zm7.6 0a2 2 0 11-4 0 2 2 0 014 0z" clip-rule="evenodd"></path></svg></button><button class="flex items-center justify-center px-3 h-8 rounded select-none focus:outline-none bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-sm">14</button><button class="flex items-center justify-center h-8 rounded select-none focus:outline-none bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-sm px-2" aria-label="next"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="text-label-2 dark:text-dark-label-2 w-4 h-4"><path fill-rule="evenodd" d="M7.913 19.071l7.057-7.078-7.057-7.064a1 1 0 011.414-1.414l7.764 7.77a1 1 0 010 1.415l-7.764 7.785a1 1 0 01-1.414-1.414z" clip-rule="evenodd"></path></svg></button></nav></div></div></div></div></div></div></div><div class="mt-8"><div class="text-label-2 dark:text-dark-label-2 text-xs">Copyright ©️ 2024 LeetCode All rights reserved</div></div></div><div class="flex-none"><div class="flex w-full items-center justify-between gap-2 p-1 bg-layer-01 dark:bg-layer-01"><div class="flex items-center gap-2"><div class="flex"><div class="mr-1 flex overflow-hidden rounded-lg bg-fill-secondary dark:bg-fill-secondary"><button class="relative inline-flex gap-2 items-center justify-center font-medium cursor-pointer focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 transition-colors bg-transparent enabled:hover:bg-fill-secondary enabled:active:bg-fill-primary text-body rounded-none px-2 py-1 text-text-secondary dark:text-text-secondary hover:text-text-secondary dark:hover:text-text-secondary"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="thumbs-up" class="svg-inline--fa fa-thumbs-up absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M323.8 34.8c-38.2-10.9-78.1 11.2-89 49.4l-5.7 20c-3.7 13-10.4 25-19.5 35l-51.3 56.4c-8.9 9.8-8.2 25 1.6 33.9s25 8.2 33.9-1.6l51.3-56.4c14.1-15.5 24.4-34 30.1-54.1l5.7-20c3.6-12.7 16.9-20.1 29.7-16.5s20.1 16.9 16.5 29.7l-5.7 20c-5.7 19.9-14.7 38.7-26.6 55.5c-5.2 7.3-5.8 16.9-1.7 24.9s12.3 13 21.3 13L448 224c8.8 0 16 7.2 16 16c0 6.8-4.3 12.7-10.4 15c-7.4 2.8-13 9-14.9 16.7s.1 15.8 5.3 21.7c2.5 2.8 4 6.5 4 10.6c0 7.8-5.6 14.3-13 15.7c-8.2 1.6-15.1 7.3-18 15.1s-1.6 16.7 3.6 23.3c2.1 2.7 3.4 6.1 3.4 9.9c0 6.7-4.2 12.6-10.2 14.9c-11.5 4.5-17.7 16.9-14.4 28.8c.4 1.3 .6 2.8 .6 4.3c0 8.8-7.2 16-16 16H286.5c-12.6 0-25-3.7-35.5-10.7l-61.7-41.1c-11-7.4-25.9-4.4-33.3 6.7s-4.4 25.9 6.7 33.3l61.7 41.1c18.4 12.3 40 18.8 62.1 18.8H384c34.7 0 62.9-27.6 64-62c14.6-11.7 24-29.7 24-50c0-4.5-.5-8.8-1.3-13c15.4-11.7 25.3-30.2 25.3-51c0-6.5-1-12.8-2.8-18.7C504.8 273.7 512 257.7 512 240c0-35.3-28.6-64-64-64l-92.3 0c4.7-10.4 8.7-21.2 11.8-32.2l5.7-20c10.9-38.2-11.2-78.1-49.4-89zM32 192c-17.7 0-32 14.3-32 32V448c0 17.7 14.3 32 32 32H96c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32H32z"></path></svg></div><div class="">8K</div></button><div class="h-full w-[1px] bg-layer-01 dark:bg-layer-01"></div><button class="relative inline-flex gap-2 items-center justify-center font-medium cursor-pointer focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 transition-colors bg-transparent enabled:hover:bg-fill-secondary enabled:active:bg-fill-primary text-body rounded-none p-1.5 text-text-secondary dark:text-text-secondary hover:text-text-secondary dark:hover:text-text-secondary"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="thumbs-down" class="svg-inline--fa fa-thumbs-down absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M323.8 477.2c-38.2 10.9-78.1-11.2-89-49.4l-5.7-20c-3.7-13-10.4-25-19.5-35l-51.3-56.4c-8.9-9.8-8.2-25 1.6-33.9s25-8.2 33.9 1.6l51.3 56.4c14.1 15.5 24.4 34 30.1 54.1l5.7 20c3.6 12.7 16.9 20.1 29.7 16.5s20.1-16.9 16.5-29.7l-5.7-20c-5.7-19.9-14.7-38.7-26.6-55.5c-5.2-7.3-5.8-16.9-1.7-24.9s12.3-13 21.3-13L448 288c8.8 0 16-7.2 16-16c0-6.8-4.3-12.7-10.4-15c-7.4-2.8-13-9-14.9-16.7s.1-15.8 5.3-21.7c2.5-2.8 4-6.5 4-10.6c0-7.8-5.6-14.3-13-15.7c-8.2-1.6-15.1-7.3-18-15.2s-1.6-16.7 3.6-23.3c2.1-2.7 3.4-6.1 3.4-9.9c0-6.7-4.2-12.6-10.2-14.9c-11.5-4.5-17.7-16.9-14.4-28.8c.4-1.3 .6-2.8 .6-4.3c0-8.8-7.2-16-16-16H286.5c-12.6 0-25 3.7-35.5 10.7l-61.7 41.1c-11 7.4-25.9 4.4-33.3-6.7s-4.4-25.9 6.7-33.3l61.7-41.1c18.4-12.3 40-18.8 62.1-18.8H384c34.7 0 62.9 27.6 64 62c14.6 11.7 24 29.7 24 50c0 4.5-.5 8.8-1.3 13c15.4 11.7 25.3 30.2 25.3 51c0 6.5-1 12.8-2.8 18.7C504.8 238.3 512 254.3 512 272c0 35.3-28.6 64-64 64l-92.3 0c4.7 10.4 8.7 21.2 11.8 32.2l5.7 20c10.9 38.2-11.2 78.1-49.4 89zM32 384c-17.7 0-32-14.3-32-32V128c0-17.7 14.3-32 32-32H96c17.7 0 32 14.3 32 32V352c0 17.7-14.3 32-32 32H32z"></path></svg></div></button></div><button class="relative inline-flex gap-2 items-center justify-center font-medium cursor-pointer focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 transition-colors bg-transparent enabled:hover:bg-fill-secondary enabled:active:bg-fill-primary text-body rounded-lg px-2 py-1 text-text-secondary dark:text-text-secondary hover:text-text-secondary dark:hover:text-text-secondary"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="comment" class="svg-inline--fa fa-comment absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M123.6 391.3c12.9-9.4 29.6-11.8 44.6-6.4c26.5 9.6 56.2 15.1 87.8 15.1c124.7 0 208-80.5 208-160s-83.3-160-208-160S48 160.5 48 240c0 32 12.4 62.8 35.7 89.2c8.6 9.7 12.8 22.5 11.8 35.5c-1.4 18.1-5.7 34.7-11.3 49.4c17-7.9 31.1-16.7 39.4-22.7zM21.2 431.9c1.8-2.7 3.5-5.4 5.1-8.1c10-16.6 19.5-38.4 21.4-62.9C17.7 326.8 0 285.1 0 240C0 125.1 114.6 32 256 32s256 93.1 256 208s-114.6 208-256 208c-37.1 0-72.3-6.4-104.1-17.9c-11.9 8.7-31.3 20.6-54.3 30.6c-15.1 6.6-32.3 12.6-50.1 16.1c-.8 .2-1.6 .3-2.4 .5c-4.4 .8-8.7 1.5-13.2 1.9c-.2 0-.5 .1-.7 .1c-5.1 .5-10.2 .8-15.3 .8c-6.5 0-12.3-3.9-14.8-9.9c-2.5-6-1.1-12.8 3.4-17.4c4.1-4.2 7.8-8.7 11.3-13.5c1.7-2.3 3.3-4.6 4.8-6.9c.1-.2 .2-.3 .3-.5z"></path></svg></div><div class="">132</div></button></div><div class="h-4 w-[1px] bg-border-tertiary dark:bg-border-tertiary"></div><div class="flex gap-2"><div type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:rt:" data-state="closed"><button class="relative inline-flex gap-2 items-center justify-center font-medium cursor-pointer focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 transition-colors bg-transparent enabled:hover:bg-fill-secondary enabled:active:bg-fill-primary text-body rounded p-1.5 text-text-secondary dark:text-text-secondary hover:text-text-secondary dark:hover:text-text-secondary" data-state="closed"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="star" class="svg-inline--fa fa-star absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path fill="currentColor" d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.6 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z"></path></svg></div></button></div><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:ru:"><div><button class="relative inline-flex gap-2 items-center justify-center font-medium cursor-pointer focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 transition-colors bg-transparent enabled:hover:bg-fill-secondary enabled:active:bg-fill-primary text-body rounded p-1.5 text-text-secondary dark:text-text-secondary hover:text-text-secondary dark:hover:text-text-secondary"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="arrow-up-right-from-square" class="svg-inline--fa fa-arrow-up-right-from-square absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M304 24c0 13.3 10.7 24 24 24H430.1L207 271c-9.4 9.4-9.4 24.6 0 33.9s24.6 9.4 33.9 0l223-223V184c0 13.3 10.7 24 24 24s24-10.7 24-24V24c0-13.3-10.7-24-24-24H328c-13.3 0-24 10.7-24 24zM72 32C32.2 32 0 64.2 0 104V440c0 39.8 32.2 72 72 72H408c39.8 0 72-32.2 72-72V312c0-13.3-10.7-24-24-24s-24 10.7-24 24V440c0 13.3-10.7 24-24 24H72c-13.3 0-24-10.7-24-24V104c0-13.3 10.7-24 24-24H200c13.3 0 24-10.7 24-24s-10.7-24-24-24H72z"></path></svg></div></button></div></div><div style="position: fixed; z-index: 40; inset: 0px auto auto 0px; transform: translate(232px, 678px);"></div></div></div><button class="relative inline-flex gap-2 items-center justify-center font-medium cursor-pointer focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 transition-colors bg-transparent enabled:hover:bg-fill-secondary enabled:active:bg-fill-primary text-body rounded p-1.5 text-text-secondary dark:text-text-secondary hover:text-text-secondary dark:hover:text-text-secondary" data-state="closed"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="circle-question" class="svg-inline--fa fa-circle-question absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M464 256A208 208 0 1 0 48 256a208 208 0 1 0 416 0zM0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256zm169.8-90.7c7.9-22.3 29.1-37.3 52.8-37.3h58.3c34.9 0 63.1 28.3 63.1 63.1c0 22.6-12.1 43.5-31.7 54.8L280 264.4c-.2 13-10.9 23.6-24 23.6c-13.3 0-24-10.7-24-24V250.5c0-8.6 4.6-16.5 12.1-20.8l44.3-25.4c4.7-2.7 7.6-7.7 7.6-13.1c0-8.4-6.8-15.1-15.1-15.1H222.6c-3.4 0-6.4 2.1-7.5 5.3l-.4 1.2c-4.4 12.5-18.2 19-30.6 14.6s-19-18.2-14.6-30.6l.4-1.2zM224 352a32 32 0 1 1 64 0 32 32 0 1 1 -64 0z"></path></svg></div></button></div></div><div class="text-text-secondary text-caption mr-2 flex items-center gap-1 font-medium" data-state="closed"><div class="bg-sd-green-500 h-1.5 w-1.5 rounded-full"></div><div>45 Online</div></div></div></div></div></div><div class="flexlayout__tab" data-layout-path="/ts0/t1" id="02eb902b-5572-c1e6-bfa1-ef0de8797a70" style="left: 0px; top: 36px; position: absolute; display: none; --width: 754px; --height: 635.59375px;"></div><div class="flexlayout__tab" data-layout-path="/ts0/t2" id="aff280e0-082c-2710-ce16-0d51d61852fd" style="left: 0px; top: 36px; position: absolute; display: none; --width: 754px; --height: 635.59375px;"></div><div class="flexlayout__tab" data-layout-path="/ts0/t3" id="d0dfa9a0-a311-4881-085e-9aa749409268" style="left: 0px; top: 36px; position: absolute; --width: 754px; --height: 635.59375px; display: none;"><div class="flex h-full w-full flex-col" style="min-width: 594px;"><div class="z-base-1 sticky top-0 ml-[1px] w-[calc(100%_-_2px)]"><div class="flex h-8 items-center border-b text-sm border-border-quaternary dark:border-border-quaternary mx-0 px-3"><div class="relative shrink-0" data-headlessui-state="" style="width: 170px;"><div><button class="group flex w-full flex-nowrap items-center outline-0 transition-colors duration-300 focus:bg-transparent text-label-3 dark:text-dark-label-3 hover:text-label-1 dark:hover:text-dark-label-1 rounded-lg" id="headlessui-menu-button-:r92:" type="button" aria-haspopup="true" aria-expanded="false" data-headlessui-state=""><div class="truncate">Status</div><div class="w-4.5 h-4.5 pointer-events-none transition duration-300 text-label-3 dark:text-dark-label-3 flex items-center mx-1 group-hover:text-label-1 dark:group-hover:text-dark-label-1"><div class="relative text-[12px] leading-[normal] p-0.5 before:block before:h-3 before:w-3"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="chevron-down" class="svg-inline--fa fa-chevron-down absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M239 401c9.4 9.4 24.6 9.4 33.9 0L465 209c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0l-175 175L81 175c-9.4-9.4-24.6-9.4-33.9 0s-9.4 24.6 0 33.9L239 401z"></path></svg></div></div></button></div></div><div class="relative shrink-0" data-headlessui-state="" style="width: 92px;"><div><button class="group flex w-full flex-nowrap items-center outline-0 transition-colors duration-300 focus:bg-transparent text-label-3 dark:text-dark-label-3 hover:text-label-1 dark:hover:text-dark-label-1 rounded-lg" id="headlessui-menu-button-:r93:" type="button" aria-haspopup="true" aria-expanded="false" data-headlessui-state=""><div class="truncate">Language</div><div class="w-4.5 h-4.5 pointer-events-none transition duration-300 text-label-3 dark:text-dark-label-3 flex items-center mx-1 group-hover:text-label-1 dark:group-hover:text-dark-label-1"><div class="relative text-[12px] leading-[normal] p-0.5 before:block before:h-3 before:w-3"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="chevron-down" class="svg-inline--fa fa-chevron-down absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M239 401c9.4 9.4 24.6 9.4 33.9 0L465 209c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0l-175 175L81 175c-9.4-9.4-24.6-9.4-33.9 0s-9.4 24.6 0 33.9L239 401z"></path></svg></div></div></button></div></div><div class="shrink-0 text-label-3 dark:text-dark-label-3" style="width: 100px;">Runtime</div><div class="shrink-0 text-label-3 dark:text-dark-label-3" style="width: 100px;">Memory</div><div class="flex flex-1 items-center justify-between" style="min-width: 110px;"><div class="text-label-3 dark:text-dark-label-3">Notes</div><div class="relative flex flex-1 justify-end" data-headlessui-state=""><div><button class="group flex w-full items-center outline-0 transition-colors duration-300 focus:bg-transparent text-label-3 dark:text-dark-label-3 hover:text-label-1 dark:hover:text-dark-label-1 rounded-lg" id="headlessui-menu-button-:r94:" type="button" aria-haspopup="true" aria-expanded="false" data-headlessui-state=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-4 w-4"><path fill-rule="evenodd" d="M7.174 5.619a8.064 8.064 0 011.635-.946l.29-1.158A2 2 0 0111.039 2h1.922a2 2 0 011.94 1.515l.29 1.158c.584.252 1.132.57 1.635.946l1.15-.329a2 2 0 012.282.923l.961 1.665a2 2 0 01-.342 2.437l-.86.832a8.151 8.151 0 010 1.888l.86.83a2 2 0 01.342 2.438l-.96 1.665a2 2 0 01-2.283.923l-1.15-.329a8.063 8.063 0 01-1.635.946l-.29 1.158a2 2 0 01-1.94 1.515H11.04a2 2 0 01-1.94-1.515l-.29-1.158a8.064 8.064 0 01-1.635-.946l-1.15.329a2 2 0 01-2.282-.923l-.961-1.665a2 2 0 01.342-2.437l.86-.831a8.158 8.158 0 010-1.889l-.86-.83a2 2 0 01-.342-2.438l.96-1.665a2 2 0 012.283-.923l1.15.329zm-1.7 1.594l-.961 1.665 1.57 1.518-.114.982a6.157 6.157 0 000 1.425l.114.982-1.57 1.518.96 1.665 2.104-.601.794.593c.38.284.793.523 1.23.711l.908.392.53 2.118h1.922l.53-2.118.909-.392a6.07 6.07 0 001.23-.711l.793-.593 2.103.601.961-1.665-1.57-1.518.114-.982a6.172 6.172 0 000-1.425l-.114-.982 1.57-1.518-.96-1.665-2.104.601-.794-.593a6.067 6.067 0 00-1.23-.71l-.908-.392L12.96 4H11.04l-.53 2.119-.909.391a6.064 6.064 0 00-1.23.711l-.793.593-2.103-.601zM12 16a4 4 0 100-8 4 4 0 000 8zm0-2a2 2 0 110-4 2 2 0 010 4z" clip-rule="evenodd"></path></svg></button></div></div></div></div></div><div class="h-full overflow-auto"><div class="group flex h-[48px] cursor-pointer items-center justify-between px-3 py-0 transition-colors"><div class="flex h-full w-full flex-shrink-0 items-center"><div class="flex flex-shrink-0 flex-col justify-between" style="width: 170px;"><div class="flex flex-col items-start"><div class="truncate text-green-s dark:text-dark-green-s"><span class="text-green-s dark:text-dark-green-s text-sm font-medium">Accepted</span></div><span class="text-xs text-label-2 dark:text-dark-label-2" data-state="closed">an hour ago</span></div></div><div class="flex flex-shrink-0 items-center" style="width: 92px;"><div class="bg-fill-primary dark:bg-fill-primary text-label-2 dark:text-dark-label-2 flex items-center gap-1 rounded-[9px] px-1.5 py-[1px] text-xs">Python3</div></div><div class="flex flex-shrink-0 items-center gap-1 pr-1 text-sm text-label-2 dark:text-dark-label-2" style="width: 100px;"><div class="relative text-[14px] leading-[normal] before:block before:h-3.5 before:w-3.5"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="clock" class="svg-inline--fa fa-clock absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M464 256A208 208 0 1 1 48 256a208 208 0 1 1 416 0zM0 256a256 256 0 1 0 512 0A256 256 0 1 0 0 256zM232 120V256c0 8 4 15.5 10.7 20l96 64c11 7.4 25.9 4.4 33.3-6.7s4.4-25.9-6.7-33.3L280 243.2V120c0-13.3-10.7-24-24-24s-24 10.7-24 24z"></path></svg></div><div class="ellipsis line-clamp-1">0 ms</div></div><div class="flex flex-shrink-0 items-center gap-1 pr-1 text-sm text-label-2 dark:text-dark-label-2" style="width: 100px;"><div class="relative text-[14px] leading-[normal] before:block before:h-3.5 before:w-3.5"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="microchip" class="svg-inline--fa fa-microchip absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M184 24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64h-8c-35.3 0-64 28.7-64 64v8H24c-13.3 0-24 10.7-24 24s10.7 24 24 24H64v48H24c-13.3 0-24 10.7-24 24s10.7 24 24 24H64v48H24c-13.3 0-24 10.7-24 24s10.7 24 24 24H64v8c0 35.3 28.7 64 64 64h8v40c0 13.3 10.7 24 24 24s24-10.7 24-24V448h48v40c0 13.3 10.7 24 24 24s24-10.7 24-24V448h48v40c0 13.3 10.7 24 24 24s24-10.7 24-24V448h8c35.3 0 64-28.7 64-64v-8h40c13.3 0 24-10.7 24-24s-10.7-24-24-24H448V280h40c13.3 0 24-10.7 24-24s-10.7-24-24-24H448V184h40c13.3 0 24-10.7 24-24s-10.7-24-24-24H448v-8c0-35.3-28.7-64-64-64h-8V24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H280V24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H184V24zM400 128V384c0 8.8-7.2 16-16 16H128c-8.8 0-16-7.2-16-16V128c0-8.8 7.2-16 16-16H384c8.8 0 16 7.2 16 16zM192 160c-17.7 0-32 14.3-32 32V320c0 17.7 14.3 32 32 32H320c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32H192zm16 48h96v96H208V208z"></path></svg></div><div class="ellipsis line-clamp-1">16.8 MB</div></div><div class="text-label-2 dark:text-dark-label-2 relative h-full w-full max-w-[400px] overflow-hidden overflow-ellipsis whitespace-nowrap py-[13px] pr-2 text-sm leading-[22px]" style=""><div class="hidden w-full flex-1 items-center justify-start space-x-2 whitespace-nowrap group-hover:flex text-blue-s dark:text-dark-blue-s" style=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor"><path fill-rule="evenodd" d="M13 11h7a1 1 0 110 2h-7v7a1 1 0 11-2 0v-7H4a1 1 0 110-2h7V4a1 1 0 112 0v7z" clip-rule="evenodd"></path></svg><span>Notes</span></div></div></div></div><div class="h-[1px] w-full"></div></div></div></div><div class="flexlayout__tab" data-layout-path="/c1/ts0/t0" id="f8456331-056c-4ead-0b7a-658c3d218aed" style="left: 762px; top: 36px; position: absolute; --width: 754px; --height: 277px;"><div class="relative flex h-full flex-col overflow-hidden rounded bg-layer-01 dark:bg-layer-01" id="editor"><div class="flex h-8 items-center justify-between border-b p-1 border-border-quaternary dark:border-border-quaternary"><div class="flex flex-nowrap items-center"><div><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:r1t:"><div><button class="rounded items-center whitespace-nowrap focus:outline-none inline-flex bg-transparent dark:bg-dark-transparent text-text-secondary dark:text-text-secondary active:bg-transparent dark:active:bg-dark-transparent hover:bg-fill-secondary dark:hover:bg-fill-secondary px-1.5 py-0.5 text-sm font-normal group">Python3<div class="relative text-[12px] leading-[normal] p-0.5 before:block before:h-3 before:w-3 ml-1 text-gray-60 dark:text-gray-60"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="chevron-down" class="svg-inline--fa fa-chevron-down absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M239 401c9.4 9.4 24.6 9.4 33.9 0L465 209c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0l-175 175L81 175c-9.4-9.4-24.6-9.4-33.9 0s-9.4 24.6 0 33.9L239 401z"></path></svg></div></button></div></div><div style="position: fixed; z-index: 40; inset: 0px auto auto 0px; transform: translate(776px, 122px);"></div></div></div></div><div class="group rounded px-2 py-0 hover:bg-fill-secondary dark:hover:bg-fill-secondary"><div class="flex items-center" data-state="closed"><button class="rounded items-center whitespace-nowrap focus:outline-none inline-flex group px-0 text-text-secondary dark:text-text-secondary py-0.5 text-sm font-normal"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 12" width="1em" height="1em" fill="currentColor" class="mr-[6px] h-3 w-3 text-text-secondary dark:text-text-secondary"><path fill-rule="evenodd" d="M6.01.7c-.652-.014-1.202.14-1.652.43a2.905 2.905 0 00-.996 1.121c-.449.856-.564 1.899-.564 2.692v.05a1.42 1.42 0 00-.9 1.321v3.572a1.41 1.41 0 001.4 1.414h5.4c.779 0 1.4-.643 1.4-1.414V6.314a1.42 1.42 0 00-.9-1.32v-.051c0-.794-.115-1.813-.564-2.658C8.165 1.405 7.336.73 6.01.7zm2.188 4.2h-4.4c.005-.717.117-1.55.45-2.185.166-.317.38-.571.65-.744.266-.17.616-.282 1.09-.271.923.02 1.444.456 1.763 1.055.331.622.443 1.43.447 2.145z" clip-rule="evenodd"></path></svg>Auto</button></div></div></div><div class="flex items-center gap-1"><button class="relative inline-flex gap-2 items-center justify-center font-medium cursor-pointer focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 transition-colors bg-transparent enabled:hover:bg-fill-secondary enabled:active:bg-fill-primary text-caption rounded text-text-primary group ml-auto p-1" data-state="closed"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-muted-foreground"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="align-left" class="svg-inline--fa fa-align-left absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M24 40C10.7 40 0 50.7 0 64S10.7 88 24 88H264c13.3 0 24-10.7 24-24s-10.7-24-24-24H24zm0 128c-13.3 0-24 10.7-24 24s10.7 24 24 24H424c13.3 0 24-10.7 24-24s-10.7-24-24-24H24zM0 320c0 13.3 10.7 24 24 24H264c13.3 0 24-10.7 24-24s-10.7-24-24-24H24c-13.3 0-24 10.7-24 24zM24 424c-13.3 0-24 10.7-24 24s10.7 24 24 24H424c13.3 0 24-10.7 24-24s-10.7-24-24-24H24z"></path></svg></div></button><button class="relative inline-flex gap-2 items-center justify-center font-medium cursor-pointer focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 transition-colors bg-transparent enabled:hover:bg-fill-secondary enabled:active:bg-fill-primary text-caption rounded text-text-primary group ml-auto p-1" data-state="closed"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-muted-foreground"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="bookmark" class="svg-inline--fa fa-bookmark absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M0 48C0 21.5 21.5 0 48 0l0 48V441.4l130.1-92.9c8.3-6 19.6-6 27.9 0L336 441.4V48H48V0H336c26.5 0 48 21.5 48 48V488c0 9-5 17.2-13 21.3s-17.6 3.4-24.9-1.8L192 397.5 37.9 507.5c-7.3 5.2-16.9 5.9-24.9 1.8S0 497 0 488V48z"></path></svg></div></button><button class="relative inline-flex gap-2 items-center justify-center font-medium cursor-pointer focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 transition-colors bg-transparent enabled:hover:bg-fill-secondary enabled:active:bg-fill-primary text-caption rounded text-text-primary group ml-auto p-1" data-state="closed"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-muted-foreground"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="brackets-curly" class="svg-inline--fa fa-brackets-curly absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path fill="currentColor" d="M152 32c-48.6 0-88 39.4-88 88v45.5c0 10.6-4.2 20.8-11.7 28.3L7 239c-9.4 9.4-9.4 24.6 0 33.9l45.3 45.3c7.5 7.5 11.7 17.7 11.7 28.3V392c0 48.6 39.4 88 88 88h48c13.3 0 24-10.7 24-24s-10.7-24-24-24H152c-22.1 0-40-17.9-40-40V346.5c0-23.3-9.3-45.7-25.8-62.2L57.9 256l28.3-28.3c16.5-16.5 25.8-38.9 25.8-62.2V120c0-22.1 17.9-40 40-40h48c13.3 0 24-10.7 24-24s-10.7-24-24-24H152zm272 0H376c-13.3 0-24 10.7-24 24s10.7 24 24 24h48c22.1 0 40 17.9 40 40v45.5c0 23.3 9.3 45.7 25.8 62.2L518.1 256l-28.3 28.3c-16.5 16.5-25.8 38.9-25.8 62.2V392c0 22.1-17.9 40-40 40H376c-13.3 0-24 10.7-24 24s10.7 24 24 24h48c48.6 0 88-39.4 88-88V346.5c0-10.6 4.2-20.8 11.7-28.3L569 273c9.4-9.4 9.4-24.6 0-33.9l-45.3-45.3c-7.5-7.5-11.7-17.7-11.7-28.3V120c0-48.6-39.4-88-88-88z"></path></svg></div></button><button class="relative inline-flex gap-2 items-center justify-center font-medium cursor-pointer focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 transition-colors bg-transparent enabled:hover:bg-fill-secondary enabled:active:bg-fill-primary text-caption rounded text-text-primary group ml-auto p-1" data-state="closed"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-muted-foreground"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="arrow-rotate-left" class="svg-inline--fa fa-arrow-rotate-left absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M40 224c-13.3 0-24-10.7-24-24V56c0-13.3 10.7-24 24-24s24 10.7 24 24v80.1l20-23.5C125 63.4 186.9 32 256 32c123.7 0 224 100.3 224 224s-100.3 224-224 224c-50.4 0-97-16.7-134.4-44.8c-10.6-8-12.7-23-4.8-33.6s23-12.7 33.6-4.8C179.8 418.9 216.3 432 256 432c97.2 0 176-78.8 176-176s-78.8-176-176-176c-54.3 0-102.9 24.6-135.2 63.4l-.1 .2 0 0L93.1 176H184c13.3 0 24 10.7 24 24s-10.7 24-24 24H40z"></path></svg></div></button><button data-state="closed" class="rounded px-3 py-1.5 font-medium items-center whitespace-nowrap focus:outline-none inline-flex group ml-auto !p-1"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-4 w-4 text-gray-6 dark:text-dark-gray-6 group-hover:text-gray-7 dark:group-hover:text-dark-gray-7"><path fill-rule="evenodd" d="M6.414 19H10a1 1 0 110 2H4a1 1 0 01-1-1v-6a1 1 0 112 0v3.586l4.293-4.293a1 1 0 011.414 1.414L6.414 19zM17.586 5H14a1 1 0 110-2h6a1 1 0 011 1v6a1 1 0 11-2 0V6.414l-4.293 4.293a1 1 0 01-1.414-1.414L17.586 5z" clip-rule="evenodd"></path></svg></button></div></div><div class="flex flex-1 flex-col overflow-hidden pb-2" data-track-load="code_editor" translate="no"><div class="flex-1 overflow-hidden"><div class="h-full w-full" data-keybinding-context="1" data-mode-id="python3"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/1" style="width: 754px; height: 201px;"><div data-mprt="3" class="overflow-guard" style="width: 754px; height: 201px;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: -17px; height: 286px; width: 56px;"><div class="glyph-margin" style="left: 0px; width: 18px; height: 286px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; width: 56px; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 13px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 18px; letter-spacing: 0px; height: 286px;"><div style="position:absolute;top:80px;width:100%;height:18px;"><div class="line-numbers" style="left:18px;width:21px;">5</div></div><div style="position:absolute;top:98px;width:100%;height:18px;"><div class="line-numbers" style="left:18px;width:21px;">6</div></div><div style="position:absolute;top:116px;width:100%;height:18px;"><div class="line-numbers" style="left:18px;width:21px;">7</div></div><div style="position:absolute;top:134px;width:100%;height:18px;"><div class="line-numbers" style="left:18px;width:21px;">8</div></div><div style="position:absolute;top:152px;width:100%;height:18px;"><div class="line-numbers" style="left:18px;width:21px;">9</div></div><div style="position:absolute;top:170px;width:100%;height:18px;"><div class="line-numbers" style="left:18px;width:21px;">10</div></div><div style="position:absolute;top:188px;width:100%;height:18px;"><div class="current-line" style="width:56px; height:18px;"></div><div class="active-line-number line-numbers" style="left:18px;width:21px;">11</div></div><div style="position:absolute;top:26px;width:100%;height:18px;"><div class="cldr codicon codicon-folding-expanded" style="left:39px;width:17px;"></div><div class="line-numbers" style="left:18px;width:21px;">2</div></div><div style="position:absolute;top:44px;width:100%;height:18px;"><div class="cldr codicon codicon-folding-expanded" style="left:39px;width:17px;"></div><div class="line-numbers" style="left:18px;width:21px;">3</div></div><div style="position:absolute;top:62px;width:100%;height:18px;"><div class="line-numbers" style="left:18px;width:21px;">4</div></div><div style="position:absolute;top:8px;width:100%;height:18px;"><div class="cldr codicon codicon-folding-expanded" style="left:39px;width:17px;"></div><div class="line-numbers" style="left:18px;width:21px;">1</div></div></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 56px; height: 201px; width: 698px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1e+06px; transform: translate3d(0px, 0px, 0px); contain: strict; top: -17px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; height: 0px; width: 698px;"><div style="position:absolute;top:80px;width:100%;height:18px;"><div class="cslr selected-text" style="top:0px;left:143px;width:10px;height:18px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:143px;width:10px;height:18px;"></div><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:143px;height:18px;"></div><div class="core-guide core-guide-indent vertical" style="left:0px;height:18px;width:7.1484375px"></div><div class="core-guide core-guide-indent vertical" style="left:28.59375px;height:18px;width:7.1484375px"></div></div><div style="position:absolute;top:98px;width:100%;height:18px;"><div class="cslr selected-text" style="top:0px;left:7px;width:10px;height:18px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:7px;width:10px;height:18px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:7px;height:18px;"></div></div><div style="position:absolute;top:116px;width:100%;height:18px;"><div class="cslr selected-text" style="top:0px;left:157px;width:10px;height:18px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:157px;width:10px;height:18px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:157px;height:18px;"></div></div><div style="position:absolute;top:134px;width:100%;height:18px;"><div class="cslr selected-text" style="top:0px;left:229px;width:10px;height:18px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:229px;width:10px;height:18px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:229px;height:18px;"></div></div><div style="position:absolute;top:152px;width:100%;height:18px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:307px;height:18px;"></div></div><div style="position:absolute;top:170px;width:100%;height:18px;"><div class="cslr selected-text" style="top:0px;left:214px;width:10px;height:18px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:214px;width:10px;height:18px;"></div><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:214px;height:18px;"></div></div><div style="position:absolute;top:188px;width:100%;height:18px;"><div class="cslr selected-text bottom-left-radius top-right-radius bottom-right-radius" style="top:0px;left:0px;width:0px;height:18px;"></div></div><div style="position:absolute;top:26px;width:100%;height:18px;"><div class="cslr selected-text" style="top:0px;left:229px;width:10px;height:18px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:229px;width:10px;height:18px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:229px;height:18px;"></div><div class="core-guide core-guide-indent vertical" style="left:0px;height:18px;width:7.1484375px"></div></div><div style="position:absolute;top:44px;width:100%;height:18px;"><div class="cslr selected-text" style="top:0px;left:272px;width:10px;height:18px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:272px;width:10px;height:18px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:272px;height:18px;"></div><div class="core-guide core-guide-indent vertical" style="left:0px;height:18px;width:7.1484375px"></div><div class="core-guide core-guide-indent vertical" style="left:28.59375px;height:18px;width:7.1484375px"></div></div><div style="position:absolute;top:62px;width:100%;height:18px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:315px;height:18px;"></div><div class="core-guide core-guide-indent vertical" style="left:0px;height:18px;width:7.1484375px"></div><div class="core-guide core-guide-indent vertical" style="left:28.59375px;height:18px;width:7.1484375px"></div><div class="core-guide core-guide-indent vertical" style="left:57.1875px;height:18px;width:7.1484375px"></div></div><div style="position:absolute;top:8px;width:100%;height:18px;"><div class="cslr selected-text" style="top:0px;left:114px;width:10px;height:18px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:114px;width:10px;height:18px;"></div><div class="cslr selected-text top-left-radius top-right-radius" style="top:0px;left:0px;width:114px;height:18px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 13px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 18px; letter-spacing: 0px; width: 698px; height: 286px;"><div style="top:80px;height:18px;" class="view-line"><span><span class="mtkw">·‌·‌·‌·‌·‌·‌·‌·‌</span><span class="mtk13">return</span><span class="mtkw">·‌</span><span class="mtk1">nums</span></span></div><div style="top:98px;height:18px;" class="view-line"><span><span></span></span></div><div style="top:116px;height:18px;" class="view-line"><span><span class="mtk1">solution</span><span class="mtkw">·‌</span><span class="mtk1">=</span><span class="mtkw">·‌</span><span class="mtk1">Solution()</span></span></div><div style="top:134px;height:18px;" class="view-line"><span><span class="mtk1">example_nums</span><span class="mtkw">·‌</span><span class="mtk1">=</span><span class="mtkw">·‌</span><span class="mtk1">[</span><span class="mtk7">3</span><span class="mtk1">,</span><span class="mtkw">·‌</span><span class="mtk7">1</span><span class="mtk1">,</span><span class="mtkw">·‌</span><span class="mtk7">2</span><span class="mtk1">,</span><span class="mtkw">·‌</span><span class="mtk7">10</span><span class="mtk1">,</span><span class="mtkw">·‌</span><span class="mtk7">1</span><span class="mtk1">]</span></span></div><div style="top:152px;height:18px;" class="view-line"><span><span class="mtk1">result</span><span class="mtkw">·‌</span><span class="mtk1">=</span><span class="mtkw">·‌</span><span class="mtk1">solution.runningSum(example_nums)</span></span></div><div style="top:170px;height:18px;" class="view-line"><span><span class="mtk11">print</span><span class="mtk1">(</span><span class="mtk8">"Running</span><span class="mtkw">·‌</span><span class="mtk8">sum:"</span><span class="mtk1">,</span><span class="mtkw">·‌</span><span class="mtk1">result)</span></span></div><div style="top: 188px; height: 18px;" class="view-line"><span><span></span></span></div><div style="top:26px;height:18px;" class="view-line"><span><span class="mtkw">·‌·‌·‌·‌</span><span class="mtk4">def</span><span class="mtkw">·‌</span><span class="mtk11">runningSum</span><span class="mtk1">(</span><span class="mtk14">self</span><span class="mtk1">,</span><span class="mtkw">·‌</span><span class="mtk14">nums</span><span class="mtk1">):</span></span></div><div style="top:44px;height:18px;" class="view-line"><span><span class="mtkw">·‌·‌·‌·‌·‌·‌·‌·‌</span><span class="mtk13">for</span><span class="mtkw">·‌</span><span class="mtk1">i</span><span class="mtkw">·‌</span><span class="mtk13">in</span><span class="mtkw">·‌</span><span class="mtk11">range</span><span class="mtk1">(</span><span class="mtk7">1</span><span class="mtk1">,</span><span class="mtkw">·‌</span><span class="mtk11">len</span><span class="mtk1">(nums)):</span></span></div><div style="top:62px;height:18px;" class="view-line"><span><span class="mtkw">·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌</span><span class="mtk1">nums[i]</span><span class="mtkw">·‌</span><span class="mtk1">=</span><span class="mtkw">·‌</span><span class="mtk1">nums[i</span><span class="mtkw">·‌</span><span class="mtk1">-</span><span class="mtkw">·‌</span><span class="mtk7">1</span><span class="mtk1">]</span><span class="mtkw">·‌</span><span class="mtk1">+</span><span class="mtkw">·‌</span><span class="mtk1">nums[i]</span></span></div><div style="top:8px;height:18px;" class="view-line"><span><span class="mtk4">class</span><span class="mtkw">·‌</span><span class="mtk10">Solution</span><span class="mtk1">:</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer has-selection cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 18px; top: 188px; left: 0px; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 13px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 18px; letter-spacing: 0px; display: block; visibility: hidden; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 684px; height: 12px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 12px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 684px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="251" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 201px; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical fade" style="position: absolute; width: 14px; height: 201px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 12px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 141px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 754px;" class="scroll-decoration"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="off" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 13px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 18px; letter-spacing: 0px; top: 171px; left: 56px; width: 1px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover margin"></div><div data-mprt="4" class="overlayWidgets" style="width: 754px;"><div class="accessibilityHelpWidget" role="dialog" aria-hidden="true" widgetid="editor.contrib.accessibilityHelpWidget" style="display: none; position: absolute;"><div role="document"></div></div><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 201px;"><div class="minimap-shadow-hidden" style="height: 201px;"></div><canvas width="0" height="251" style="position: absolute; left: 0px; width: 0px; height: 201px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="251" style="position: absolute; left: 0px; width: 0px; height: 201px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div></div><div data-mprt="2" class="overflowingContentWidgets"></div></div></div></div><div class="text-label-2 dark:text-dark-label-2 bg-gray-2 dark:bg-dark-gray-2"></div></div><div class="flex h-9 items-center justify-between px-3 py-2"><div class="flex flex-1 items-center justify-between"><div class="text-caption flex items-center gap-2 text-text-tertiary dark:text-text-tertiary">Saved</div><div class="select-none text-xs text-text-tertiary dark:text-text-tertiary">Ln 11, Col 1</div></div></div></div></div><div class="flexlayout__tab" data-layout-path="/c1/ts1/t0" id="dca614bb-8674-61e8-038c-8842e92d2596" style="left: 762px; top: 357px; position: absolute; --width: 754px; --height: 314px; display: none;"><div class="flex h-full w-full flex-col justify-between"><div class="flex-1 overflow-y-auto"><div class=""><div class="mx-5 my-4 flex flex-col space-y-4"><div class="flex w-full flex-row items-start justify-between gap-4"><div class="flex flex-wrap items-center gap-x-2 gap-y-4"><button data-e2e-locator="console-testcase-tag" class="font-medium items-center whitespace-nowrap focus:outline-none inline-flex bg-fill-3 dark:bg-dark-fill-3 hover:bg-fill-2 dark:hover:bg-dark-fill-2 relative rounded-lg px-4 py-1 hover:text-label-1 dark:hover:text-dark-label-1 text-label-1 dark:text-dark-label-1">Case 1</button><button data-e2e-locator="console-testcase-tag" class="font-medium items-center whitespace-nowrap focus:outline-none inline-flex hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2 relative rounded-lg px-4 py-1 hover:text-label-1 dark:hover:text-dark-label-1 bg-transparent dark:bg-dark-transparent">Case 2</button><button data-e2e-locator="console-testcase-tag" class="font-medium items-center whitespace-nowrap focus:outline-none inline-flex hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2 relative rounded-lg px-4 py-1 hover:text-label-1 dark:hover:text-dark-label-1 bg-transparent dark:bg-dark-transparent">Case 3</button><button data-state="closed" class="rounded font-medium whitespace-nowrap focus:outline-none text-gray-5 dark:text-dark-gray-5 hover:text-gray-6 dark:hover:text-dark-gray-6 bg-transparent dark:bg-dark-transparent hover:bg-transparent dark:hover:bg-transparent m-0 flex h-4 w-4 items-center justify-center p-0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-4 w-4"><path fill-rule="evenodd" d="M13 11h7a1 1 0 110 2h-7v7a1 1 0 11-2 0v-7H4a1 1 0 110-2h7V4a1 1 0 112 0v7z" clip-rule="evenodd"></path></svg></button></div></div><div class="space-y-4"><div><div class="flex h-full w-full flex-col space-y-2"><div class="text-xs font-medium text-label-3 dark:text-dark-label-3">nums =</div><div class="font-menlo w-full cursor-text rounded-lg border px-3 py-[10px] bg-fill-3 dark:bg-dark-fill-3 border-transparent" spellcheck="false"><div data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false" class="font-menlo w-full resize-none whitespace-pre-wrap break-words outline-none placeholder:text-label-4 dark:placeholder:text-dark-label-4 sentry-unmask" data-e2e-locator="console-testcase-input" placeholder="Enter Testcase" autocorrect="off" autocapitalize="off" aria-autocomplete="none" contenteditable="true">[1,2,3,4]</div></div></div></div></div></div></div><div class="mt-0 h-0 overflow-hidden opacity-0"><div class="ml-0 mr-5 h-full"><div class="relative h-full"><div class="relative h-full rounded-lg pb-6"><div class="flex flex-1 flex-col overflow-hidden h-full w-full" translate="no"><div class="flex-1 overflow-hidden"><div class="cm-theme" style="font-size: 13px;"><div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2y ͼ29"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div class="cm-gutters" aria-hidden="true" style="min-height: 42px; position: sticky;"><div class="cm-gutter cm-lineNumbers"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;">9</div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px; margin-top: 4px;">1</div><div class="cm-gutterElement" style="height: 14px;">2</div><div class="cm-gutterElement" style="height: 14px;">3</div></div><div class="cm-gutter cm-foldGutter"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;"><span title="Unfold line">›</span></div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px; margin-top: 4px;"></div></div></div><div style="tab-size: 4;" spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true"><div class="cm-activeLine cm-line">[1,2,3,4]</div><div class="cm-line">[1,1,1,1,1]</div><div class="cm-line">[3,1,2,10,1]</div></div><div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;"></div><div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div></div></div></div></div></div></div></div></div></div></div><div class="flex w-full flex-none items-center justify-between gap-2 p-1"><div class="flex items-center"><div class="cursor-pointer mr-1 select-none p-1 text-xs active:bg-fill-3 dark:active:bg-dark-fill-3 rounded-lg px-2 py-1" data-state="closed"><div class="group flex items-center gap-2 text-sm"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-gray-6 dark:text-dark-gray-6 group-hover:text-gray-7 dark:group-hover:text-dark-gray-7"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="code" class="svg-inline--fa fa-code absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path fill="currentColor" d="M399.1 1.1c-12.7-3.9-26.1 3.1-30 15.8l-144 464c-3.9 12.7 3.1 26.1 15.8 30s26.1-3.1 30-15.8l144-464c3.9-12.7-3.1-26.1-15.8-30zm71.4 118.5c-9.1 9.7-8.6 24.9 1.1 33.9L580.9 256 471.6 358.5c-9.7 9.1-10.2 24.3-1.1 33.9s24.3 10.2 33.9 1.1l128-120c4.8-4.5 7.6-10.9 7.6-17.5s-2.7-13-7.6-17.5l-128-120c-9.7-9.1-24.9-8.6-33.9 1.1zm-301 0c-9.1-9.7-24.3-10.2-33.9-1.1l-128 120C2.7 243 0 249.4 0 256s2.7 13 7.6 17.5l128 120c9.7 9.1 24.9 8.6 33.9-1.1s8.6-24.9-1.1-33.9L59.1 256 168.4 153.5c9.7-9.1 10.2-24.3 1.1-33.9z"></path></svg></div><span class="text-label-3 dark:text-dark-label-3 group-hover:text-label-2 dark:group-hover:text-dark-label-2">Source</span></div></div><a target="_blank" class="cursor-pointer" href="https://support.leetcode.com/hc/en-us/articles/32442719377939-How-to-create-test-cases-on-LeetCode" rel="noreferrer" data-state="closed"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-gray-6 dark:text-dark-gray-6 group-hover:text-gray-7 dark:group-hover:text-dark-gray-7"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="circle-question" class="svg-inline--fa fa-circle-question absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M464 256A208 208 0 1 0 48 256a208 208 0 1 0 416 0zM0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256zm169.8-90.7c7.9-22.3 29.1-37.3 52.8-37.3h58.3c34.9 0 63.1 28.3 63.1 63.1c0 22.6-12.1 43.5-31.7 54.8L280 264.4c-.2 13-10.9 23.6-24 23.6c-13.3 0-24-10.7-24-24V250.5c0-8.6 4.6-16.5 12.1-20.8l44.3-25.4c4.7-2.7 7.6-7.7 7.6-13.1c0-8.4-6.8-15.1-15.1-15.1H222.6c-3.4 0-6.4 2.1-7.5 5.3l-.4 1.2c-4.4 12.5-18.2 19-30.6 14.6s-19-18.2-14.6-30.6l.4-1.2zM224 352a32 32 0 1 1 64 0 32 32 0 1 1 -64 0z"></path></svg></div></a></div></div></div></div><div class="flexlayout__tab" data-layout-path="/c1/ts1/t1" id="54e7a449-a16e-c5ef-37dd-325025881c56" style="left: 762px; top: 357px; position: absolute; --width: 754px; --height: 314px;"><div class="flex h-full flex-col justify-between"><div class="flex-1 overflow-y-auto"><div class=""><div class="space-y-4 px-5 py-4"><div class="flex items-center"><div class="text-xl font-medium text-green-s dark:text-dark-green-s" data-e2e-locator="console-result">Accepted</div><div class="ml-4 text-label-3 dark:text-dark-label-3">Runtime: 0 ms</div><div class="ml-auto flex min-w-0 items-center space-x-4"></div></div><div class="flex flex-wrap gap-x-2 gap-y-4"><div><div class="cursor-pointer rounded-lg px-4 py-1 font-medium hover:bg-fill-2 dark:hover:bg-dark-fill-2 hover:text-label-1 dark:hover:text-dark-label-1 bg-fill-3 dark:bg-dark-fill-3 text-label-1 dark:text-dark-label-1"><div class="flex flex-row items-center space-x-[6px]"><div class="h-1 w-1 rounded-full bg-green-s dark:bg-dark-green-s"></div><div>Case 1</div></div></div></div><div><div class="cursor-pointer rounded-lg px-4 py-1 font-medium hover:bg-fill-2 dark:hover:bg-dark-fill-2 hover:text-label-1 dark:hover:text-dark-label-1 text-label-3 dark:text-dark-label-3"><div class="flex flex-row items-center space-x-[6px]"><div class="h-1 w-1 rounded-full bg-green-s dark:bg-dark-green-s"></div><div>Case 2</div></div></div></div><div><div class="cursor-pointer rounded-lg px-4 py-1 font-medium hover:bg-fill-2 dark:hover:bg-dark-fill-2 hover:text-label-1 dark:hover:text-dark-label-1 text-label-3 dark:text-dark-label-3"><div class="flex flex-row items-center space-x-[6px]"><div class="h-1 w-1 rounded-full bg-green-s dark:bg-dark-green-s"></div><div>Case 3</div></div></div></div></div><div class="space-y-4"><div><div class="mb-2 text-xs font-medium text-label-3 dark:text-dark-label-3">Input</div><div class="space-y-2"><div class="group relative rounded-lg bg-fill-4 dark:bg-dark-fill-4"><div class="relative py-3"><div class="mx-3 mb-2 text-xs text-label-3 dark:text-dark-label-3">nums =</div><div class="z-base-1 hidden rounded border group-hover:block border-border-quaternary dark:border-border-quaternary bg-layer-02 dark:bg-layer-02 absolute right-3 top-2.5 z-base-1"><div class="relative cursor-pointer flex h-[22px] w-[22px] items-center justify-center bg-layer-02 dark:bg-layer-02 hover:bg-fill-tertiary dark:hover:bg-fill-tertiary rounded-[4px]" data-state="closed"><div><div data-state="closed"><div class="relative text-[12px] leading-[normal] p-[1px] before:block before:h-3 before:w-3 h-3.5 w-3.5 text-text-primary dark:text-text-primary"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="clone" class="svg-inline--fa fa-clone absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M64 464H288c8.8 0 16-7.2 16-16V384h48v64c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V224c0-35.3 28.7-64 64-64h64v48H64c-8.8 0-16 7.2-16 16V448c0 8.8 7.2 16 16 16zM224 304H448c8.8 0 16-7.2 16-16V64c0-8.8-7.2-16-16-16H224c-8.8 0-16 7.2-16 16V288c0 8.8 7.2 16 16 16zm-64-16V64c0-35.3 28.7-64 64-64H448c35.3 0 64 28.7 64 64V288c0 35.3-28.7 64-64 64H224c-35.3 0-64-28.7-64-64z"></path></svg></div></div></div></div></div><div class="font-menlo mx-3 whitespace-pre-wrap break-all leading-5 text-label-1 dark:text-dark-label-1" style="line-break: anywhere;"><div class="" style="overflow-wrap: break-word;"><div class="align-middle"><div>[1,2,3,4]</div></div></div></div></div></div></div></div><div class="flex h-full w-full flex-col space-y-2"><div class="flex text-xs font-medium text-label-3 dark:text-dark-label-3">Stdout</div><div class="group relative rounded-lg bg-fill-4 dark:bg-dark-fill-4"><div class="relative py-3"><div class="z-base-1 hidden rounded border group-hover:block border-border-quaternary dark:border-border-quaternary bg-layer-02 dark:bg-layer-02 absolute right-3 top-2.5 z-base-1"><div class="relative cursor-pointer flex h-[22px] w-[22px] items-center justify-center bg-layer-02 dark:bg-layer-02 hover:bg-fill-tertiary dark:hover:bg-fill-tertiary rounded-[4px]" data-state="closed"><div><div data-state="closed"><div class="relative text-[12px] leading-[normal] p-[1px] before:block before:h-3 before:w-3 h-3.5 w-3.5 text-text-primary dark:text-text-primary"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="clone" class="svg-inline--fa fa-clone absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M64 464H288c8.8 0 16-7.2 16-16V384h48v64c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V224c0-35.3 28.7-64 64-64h64v48H64c-8.8 0-16 7.2-16 16V448c0 8.8 7.2 16 16 16zM224 304H448c8.8 0 16-7.2 16-16V64c0-8.8-7.2-16-16-16H224c-8.8 0-16 7.2-16 16V288c0 8.8 7.2 16 16 16zm-64-16V64c0-35.3 28.7-64 64-64H448c35.3 0 64 28.7 64 64V288c0 35.3-28.7 64-64 64H224c-35.3 0-64-28.7-64-64z"></path></svg></div></div></div></div></div><div class="font-menlo mx-3 whitespace-pre-wrap break-all leading-5 text-label-1 dark:text-dark-label-1" style="line-break: anywhere;"><div class="" style="overflow-wrap: break-word;"><div class="align-middle"><div>Running sum: [3, 4, 6, 16, 17]
</div></div></div></div></div></div></div><div class="flex h-full w-full flex-col space-y-2"><div class="flex text-xs font-medium text-label-3 dark:text-dark-label-3">Output</div><div class="group relative rounded-lg bg-fill-4 dark:bg-dark-fill-4"><div class="relative py-3"><div class="z-base-1 hidden rounded border group-hover:block border-border-quaternary dark:border-border-quaternary bg-layer-02 dark:bg-layer-02 absolute right-3 top-2.5 z-base-1"><div class="relative cursor-pointer flex h-[22px] w-[22px] items-center justify-center bg-layer-02 dark:bg-layer-02 hover:bg-fill-tertiary dark:hover:bg-fill-tertiary rounded-[4px]" data-state="closed"><div><div data-state="closed"><div class="relative text-[12px] leading-[normal] p-[1px] before:block before:h-3 before:w-3 h-3.5 w-3.5 text-text-primary dark:text-text-primary"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="clone" class="svg-inline--fa fa-clone absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M64 464H288c8.8 0 16-7.2 16-16V384h48v64c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V224c0-35.3 28.7-64 64-64h64v48H64c-8.8 0-16 7.2-16 16V448c0 8.8 7.2 16 16 16zM224 304H448c8.8 0 16-7.2 16-16V64c0-8.8-7.2-16-16-16H224c-8.8 0-16 7.2-16 16V288c0 8.8 7.2 16 16 16zm-64-16V64c0-35.3 28.7-64 64-64H448c35.3 0 64 28.7 64 64V288c0 35.3-28.7 64-64 64H224c-35.3 0-64-28.7-64-64z"></path></svg></div></div></div></div></div><div class="font-menlo mx-3 whitespace-pre-wrap break-all leading-5 text-label-1 dark:text-dark-label-1" style="line-break: anywhere;"><div class="" style="overflow-wrap: break-word;"><div class="align-middle"><div>[1,3,6,10]</div></div></div></div></div></div></div><div class="flex h-full w-full flex-col space-y-2"><div class="flex text-xs font-medium text-label-3 dark:text-dark-label-3">Expected</div><div class="group relative rounded-lg bg-fill-4 dark:bg-dark-fill-4"><div class="relative py-3"><div class="z-base-1 hidden rounded border group-hover:block border-border-quaternary dark:border-border-quaternary bg-layer-02 dark:bg-layer-02 absolute right-3 top-2.5 z-base-1"><div class="relative cursor-pointer flex h-[22px] w-[22px] items-center justify-center bg-layer-02 dark:bg-layer-02 hover:bg-fill-tertiary dark:hover:bg-fill-tertiary rounded-[4px]" data-state="closed"><div><div data-state="closed"><div class="relative text-[12px] leading-[normal] p-[1px] before:block before:h-3 before:w-3 h-3.5 w-3.5 text-text-primary dark:text-text-primary"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="clone" class="svg-inline--fa fa-clone absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M64 464H288c8.8 0 16-7.2 16-16V384h48v64c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V224c0-35.3 28.7-64 64-64h64v48H64c-8.8 0-16 7.2-16 16V448c0 8.8 7.2 16 16 16zM224 304H448c8.8 0 16-7.2 16-16V64c0-8.8-7.2-16-16-16H224c-8.8 0-16 7.2-16 16V288c0 8.8 7.2 16 16 16zm-64-16V64c0-35.3 28.7-64 64-64H448c35.3 0 64 28.7 64 64V288c0 35.3-28.7 64-64 64H224c-35.3 0-64-28.7-64-64z"></path></svg></div></div></div></div></div><div class="font-menlo mx-3 whitespace-pre-wrap break-all leading-5 text-label-1 dark:text-dark-label-1" style="line-break: anywhere;"><div class="" style="overflow-wrap: break-word;"><div class="align-middle"><div>[1,3,6,10]</div></div></div></div></div></div></div></div><div class="mx-auto flex items-center justify-center text-label-3 dark:text-dark-label-3"><div class="flex flex-row rounded px-2 py-[6px] hover:cursor-pointer hover:bg-fill-3 dark:hover:bg-dark-fill-3"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-5 w-5"><path fill-rule="evenodd" d="M12 5.236C10.56 4.156 9.12 3.47 7.68 3.47c-2.16 0-5.399 1.62-5.399 5.94 0 3.835 2.782 7.381 8.345 10.638l.384.221a2 2 0 001.98 0c5.82-3.317 8.729-6.936 8.729-10.86 0-4.319-3.24-5.939-5.4-5.939-1.439 0-2.88.688-4.319 1.767zm-1.2 1.6l1.2.9 1.2-.9c1.238-.928 2.267-1.367 3.12-1.367 1.804 0 3.399 1.396 3.399 3.94 0 2.993-2.346 5.981-7.357 8.912l-.362.21c-5.26-2.998-7.719-6.058-7.719-9.122 0-2.544 1.595-3.94 3.4-3.94.852 0 1.881.44 3.119 1.367z" clip-rule="evenodd"></path></svg><div class="ml-1">Contribute a testcase</div></div></div></div></div><div class="mt-0 h-0 overflow-hidden opacity-0"><div class="h-full space-y-2"><div class="flex flex-col pt-4"><div class="flex flex-col gap-2 px-4"><div class="text-sd-muted-foreground text-xs font-medium leading-none">Input</div><hr class="dark:border-dark-divider-2 border-sd-border h-px w-full rounded-full"></div><div class="px-4"><div style="max-height: 2000px;"><div class="flex flex-1 flex-col overflow-hidden h-full w-full" translate="no"><div class="flex-1 overflow-hidden"><div class="cm-theme" style="font-size: 13px;"><div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ87 ͼ5n"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div class="cm-gutters" aria-hidden="true" style="min-height: 42px; position: sticky;"><div class="cm-gutter cm-lineNumbers"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;">9</div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px; margin-top: 4px;">1</div><div class="cm-gutterElement" style="height: 14px;">2</div><div class="cm-gutterElement" style="height: 14px;">3</div></div><div class="cm-gutter cm-foldGutter"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;"><span title="Unfold line">›</span></div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px; margin-top: 4px;"></div></div></div><div style="tab-size: 4;" spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true"><div class="cm-activeLine cm-line">[1,2,3,4]</div><div class="cm-line">[1,1,1,1,1]</div><div class="cm-line">[3,1,2,10,1]</div></div><div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;"><div class="cm-cursor cm-cursor-primary" style="left: 55.8375px; top: 5.60004px; height: 15.2px;"></div></div><div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div></div></div></div></div></div></div></div></div><div class="flex flex-col pt-4"><div class="flex flex-col gap-2 px-4"><div class="text-sd-muted-foreground text-xs font-medium leading-none">Stdout</div><hr class="dark:border-dark-divider-2 border-sd-border h-px w-full rounded-full"></div><div class="px-4"><div style="max-height: 2000px;"><div class="flex flex-1 flex-col overflow-hidden h-full w-full" translate="no"><div class="flex-1 overflow-hidden"><div class="cm-theme" style="font-size: 13px;"><div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ88 ͼ66"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div class="cm-gutters" aria-hidden="true" style="min-height: 56px; position: sticky;"><div class="cm-gutter cm-lineNumbers"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;">9</div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px; margin-top: 4px;">1</div><div class="cm-gutterElement" style="height: 14px;">2</div><div class="cm-gutterElement" style="height: 14px;">3</div><div class="cm-gutterElement" style="height: 14px;">4</div></div><div class="cm-gutter cm-foldGutter"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;"><span title="Unfold line">›</span></div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px; margin-top: 4px;"></div></div></div><div style="tab-size: 4;" spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true"><div class="cm-activeLine cm-line">Running sum: [3, 4, 6, 16, 17]</div><div class="cm-line"><br></div><div class="cm-line"><br></div><div class="cm-line"><br></div></div><div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;"><div class="cm-cursor cm-cursor-primary" style="left: 55.8375px; top: 5.6001px; height: 15.2px;"></div></div><div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div></div></div></div></div></div></div></div></div><div class="flex flex-col pt-4"><div class="flex flex-col gap-2 px-4"><div class="text-sd-muted-foreground text-xs font-medium leading-none">Output</div><hr class="dark:border-dark-divider-2 border-sd-border h-px w-full rounded-full"></div><div class="px-4"><div style="max-height: 2000px;"><div class="flex flex-1 flex-col overflow-hidden h-full w-full" translate="no"><div class="flex-1 overflow-hidden"><div class="cm-theme" style="font-size: 13px;"><div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ89 ͼ6p"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div class="cm-gutters" aria-hidden="true" style="min-height: 42px; position: sticky;"><div class="cm-gutter cm-lineNumbers"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;">9</div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px; margin-top: 4px;">1</div><div class="cm-gutterElement" style="height: 14px;">2</div><div class="cm-gutterElement" style="height: 14px;">3</div></div><div class="cm-gutter cm-foldGutter"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;"><span title="Unfold line">›</span></div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px; margin-top: 4px;"></div></div></div><div style="tab-size: 4;" spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true"><div class="cm-activeLine cm-line">[1,3,6,10]</div><div class="cm-line">[1,2,3,4,5]</div><div class="cm-line">[3,4,6,16,17]</div></div><div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;"><div class="cm-cursor cm-cursor-primary" style="left: 55.8375px; top: 5.59998px; height: 15.2001px;"></div></div><div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div></div></div></div></div></div></div></div></div><div class="pb-4"><div class="flex flex-col pt-4"><div class="flex flex-col gap-2 px-4"><div class="text-sd-muted-foreground text-xs font-medium leading-none">Expected</div><hr class="dark:border-dark-divider-2 border-sd-border h-px w-full rounded-full"></div><div class="px-4"><div style="max-height: 2000px;"><div class="flex flex-1 flex-col overflow-hidden h-full w-full" translate="no"><div class="flex-1 overflow-hidden"><div class="cm-theme" style="font-size: 13px;"><div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ8a ͼ78"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div class="cm-gutters" aria-hidden="true" style="min-height: 42px; position: sticky;"><div class="cm-gutter cm-lineNumbers"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;">9</div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px; margin-top: 4px;">1</div><div class="cm-gutterElement" style="height: 14px;">2</div><div class="cm-gutterElement" style="height: 14px;">3</div></div><div class="cm-gutter cm-foldGutter"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;"><span title="Unfold line">›</span></div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px; margin-top: 4px;"></div></div></div><div style="tab-size: 4;" spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true"><div class="cm-activeLine cm-line">[1,3,6,10]</div><div class="cm-line">[1,2,3,4,5]</div><div class="cm-line">[3,4,6,16,17]</div></div><div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;"><div class="cm-cursor cm-cursor-primary" style="left: 55.8375px; top: 5.59998px; height: 15.2px;"></div></div><div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div><div data-layout-path="/s0" class="flexlayout__splitter flexlayout__splitter_vert" style="cursor: ew-resize; left: 754px; top: 0px; width: 8px; height: 671.594px; position: absolute;"></div><div data-layout-path="/c1/s0" class="flexlayout__splitter flexlayout__splitter_horz" style="cursor: ns-resize; left: 762px; top: 313px; width: 754px; height: 8px; position: absolute;"></div><div class="flexlayout__tabset_header_sizer" style="visibility: hidden;">FindHeaderBarSize</div><div class="flexlayout__tabset_sizer" style="visibility: hidden;">FindTabBarSize</div><div class="flexlayout__border_sizer" style="visibility: hidden;">FindBorderBarSize</div></div></div></div></div></div></div><div role="region" aria-label="Notifications (F8)" tabindex="-1" style="pointer-events:none"><ol tabindex="-1" class="z-message pointer-events-none fixed left-0 top-0 flex max-h-screen w-full flex-col-reverse items-center gap-4 p-4"></ol></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"isRobotVisit":false,"isMobile":false,"dehydratedState":{"mutations":[],"queries":[]},"_nextI18Next":{"initialI18nStore":{"en":{"common":{"404":{"title":"Page Not Found - LeetCode","pageNotFound":"Page Not Found","message":"Sorry, but we can't find the page you are looking for..."},"meta":{"title":"","description":"","keywords":""},"ok":"OK","cancel":"Cancel","confirm":"Confirm","update":"Update","submit":"Submit","save":"Save","netFailed":"Debugger failed to connect","header":{"logo":{"url":"","description":""},"title":{"problemset-all":""},"action":{"login":{"text":"","url":""}}},"conjunctions":{"and":"and","or":"or"},"pages":{"leetcode":"LeetCode","explore":"Explore","problems":"Problems","interview":{"interview":"Interview","onlineInterview":"Online Interview","assessment":"Assessment"},"contest":"Contest","discuss":"Discuss","store":{"store":"Store","redeem":"Redeem","premium":"Premium","shop":"Micro-shop"},"admin":{"admin":"Admin","library":"Library","review":"Review","operations":"User Management","scores":"Points","contribute":"Contribution","backend":"Administration","internalContest":"Internal Contest Dashboard","contestDashboard":"Contest Dashboard","contestAdmin":"Contest Cheating Dashboard","emailBatch":"Email Batch","dangerZone":"Danger Zone","dbTestcase":"DB Testcase Converter","tagManagement":"Tag Management","questionFeedback":"Question Feedback"},"mobileApp":"Mobile App","playground":"Playground","signIn":"Sign in","register":"Register","signOut":"Sign Out"},"userMenu":{"renew":"Renew","getPremium":"Access all features with our Premium subscription!","orders":"Orders","tryNewFeatures":"Try New Features","translateQuestions":"Display problems in Chinese","unmockUser":"Unmock User","revertToOldVersion":"Revert to old version","categories":{"myList":"My Lists","notebook":"Notebook","submissions":"Submissions","session":"Session","points":"Points","progress":"Progress"},"appearance":"Appearance","appearanceContent":{"auto":"System Default","light":"Light","dark":"Dark"},"account":"Settings"},"streakCounter":{"finished":"Well done! Come back for tomorrow's challenge!","unfinished":"Solve today's Daily Challenge to refresh your streak!","buyTimeTravelTicket":"Buy Time Travel Ticket","missedOneDayThisMonth":"You missed 1 day this month. ","missedDaysThisMonth":"You missed {{count}} days this month. "},"playground":{"playground":"Playground","myPlaygrounds":"My Playgrounds","remainingPlaygrounds":"Remaining","renew":"Renew","templates":{"consoleApplication":"Console Application","empty":"New Playground","frontend":"Frontend","machineLearning":"Machine Learning"}},"links":{"premium":"/subscribe/","discuss":"/discuss/","assessment":"/assessment/","shop":"https://detail.youzan.com/show/goods/newest?alias=271n43vr9hen7","onlineInterview":"https://interview.leetcode.com/interview/","profileArticles":"/submissions/","orders":"/store/orders/","tryNewFeatures":"/new/","explore":"/explore/","admin":{"scores":"/points/admin","operations":"/user_management"},"playground":"/playground","account":"/profile"},"pagination":{"perpage":"/ page"},"expand":"Expand","collapse":"Collapse","difficulty":{"easy":"Easy","medium":"Medium","hard":"Hard"},"easterEgg":{"rewardMessage":"Congratulations! You just found 10 LeetCoins. Happy LeetCoding!"},"markdown":{"heading":"heading","quote":"Quote"},"mentions":{"users":"Users","problems":"Problems"},"confirmModal":{"title":"Are you sure?","confirmBtn":"Confirm","cancelBtn":"Cancel"},"saving":"Saving...","saved":"Saved","autoSaved":"Save automatically","loginRequired":"Sign in required","verifiedRequired":"You need to verify your email","phoneVerifiedRequired":"Your need to verify your phone","maybeVerifiedRequired":"You need to verify your email","dailyCheckIn":"+1 Daily Check-in","copy":"Copy","copyToEditor":"Copy To Editor","copied":"Copied!","copyLink":"Copy Link","viewMore":"View more","viewLess":"View less","code":"Code","survey":{"veryDissatisfied":"Very Dissatisfied","verySatisfied":"Very Satisfied","next":"Next","continue":"Continue","submit":"Submit","questionNo":"Question {{current}} of {{total}}","thanksMsg":"🎉 Thanks for your feedback!"},"qdNav":{"backTitle":"Problem List","expandPanel":"Expand Panel","preQuestion":"Prev Question","nextQuestion":"Next Question","pickOne":"Pick one","openInNewTab":"Open in New Tab"},"premiumModal":{"learnMore":"Learn more","subscribe":"Subscribe"},"truncatedContent":{"viewAll":"View all","viewLess":"View less","openRaw":"Open Raw","showMore":"Show more","showLess":"Show less"},"safariNotUse":"The current version of Safari is too low. For better experience, upgrade to the latest version","account":{"emailVerifyModal":{"title":"Verify your account","description":"Please verify your email address in order to use your account.","verify":"Verify","cancel":"Cancel"}},"medal":{"metadataTitle":"Badge - LeetCode","congratulation":"Congratulations","genPoster":"Generate Image","genPostering":"Generating","saveImgMobile":"Long press to save the image","saveImgPc":"Right-click to save the image","medalEmpty":"Sorry, there are no medals to grab right now."}},"problems":{"meta":{"title":"{{title}} - LeetCode","description":"Can you solve this real interview question? {{title}} - {{content}}","ogImage":"https://leetcode.com/static/images/LeetCode_Sharing.png","defaultDescription":"Level up your coding skills and quickly land a job. This is the best place to expand your knowledge and get prepared for your next interview."},"tabs":{"description":"Description","editorial":"Editorial","discussion":"Discussion","solutions":"Solutions","submissions":"Submissions","submissionOverview":"Submission Overview","code":"Code","testcase":"Testcase","result":"Test Result","debugger":"Debugger","settings":"Settings","note":"Note","guide":"Guide","preview":"Preview","previewConsole":"Web Console","rawText":"Raw Text","previewCode":"Preview Code","resultDiff":"Diff","disabledTooltips":{"editorial":"Editorial is not available for this question."}},"lockedQuestion":{"subscribeToUnlock":"Subscribe to unlock.","subscribeToUnlockMessage":"Thanks for using LeetCode! To view this question you must subscribe to premium.","subscribe":"Subscribe"},"unsupportedFeature":{"upgradeToIdeTitle":"Upgrade to Dynamic Layout","signInToTryOut":"Sign In to Try Out","tryOut":"Try Out","features":{"frontendQuestion":"New frontend questions are exclusively available in Dynamic Layout. Switch to this format for a more immersive LeetCode experience and access to these questions."}},"feedback":{"feedback":"Feedback","revertToOld":"Revert to last version"},"satisfactionSurvey":{"submitBtnText":"Get LeetCoins"},"panel":{"recommend":"Recommend","description":"Recent hot questions we've picked for you."},"dynamicLayout":{"maximize":"Maximize","exit":"Exit","foldPanel":"Fold","unFoldPanel":"Unfold","moveTabset":"{{name}} and {{count}} tabs","disabledUnFold":"Reset not supported under current layout. Please resize with splitter.","layoutManager":{"hints":"Hints","layouts":"Layouts","featureTitle":"Layout gets messy?","featureContent":"One-click reset is now available! You can even save a specific layout as a template for future use.","gotIt":"Got it","tryNow":"Try now","featureInfo":"Create and manage all your custom layouts from here.","default":"Default","note":"Note-taking","debug":"Debug","saveCurrentLayout":"Save Current Layout","saveNewLayout":"Save New Layout","nameYourLayout":"Name current layout","temporaryTabs":"Temporary Tabs","temporaryTabsWarningBefore":"","temporaryTabsWarningAfter":" will not be saved in custom layout.","temporaryTabsContent":"Temporary visible tabs can only be accessed in specific question, which includes tabs like: solutions details and submissions details.","cancel":"Cancel","save":"Save","layoutSaved":"Layout saved","layoutDeleted":"Layout deleted","upgradeToSaveFirst":"Upgrade to turn on","upgradeToSaveSecond":"custom layouts","subscribe":"Subscribe","apply":"Apply","upgradeToApply":"Upgrade to premium to unlock this layout","delete":"Delete","deleteTitle":"Delete \"{{name}}\"?","deleteContent":"This layout will be permanently deleted and will be unrecoverable.","no":"No","edit":"Edit","editLayout":"Edit Layout","updateToCurrentLayout":"Update to Current Layout"},"featureModal":{"dynamicLayout":"Dynamic Layout","title":"Upgrade to Dynamic Layout","content":"Enjoy the enhanced flexibility and immerse yourself in the coding environment offered by LeetCode's upgraded Dynamic Layout.","tryOut":"Try Out"},"settingRunSubmitPopover":{"title":"Customize Dynamic Toolbar?","content":"You can now move Run, Submit and Debug buttons to Code Editor.","buttonText":"Go to Settings"}},"settings":{"settings":"Settings","lab":"Lab","premium":"Premium","layout":{"categoryTitle":"Dynamic Layout","resetToDefaultLayout":"Default layout","reset":"Reset","runSubmitPosition":"Show Run / Submit / Debug buttons in","toolbar":"ToolBar","code-editor":"Code Editor","revertToSplitViewMode":"Revert to Split View mode"},"editor":{"categoryTitle":"Code Editor","fontSize":"Font size","keyBinding":"Key binding","keyBindingVim":"Vim","keyBindingEmacs":"Emacs","keyBindingStandard":"Standard","tabSize":"Tab size","spaces":"{{count}} spaces","wordWrap":"Word Wrap","relativeLineNumber":"Relative Line Number"},"shortcuts":{"categoryTitle":"Shortcuts","or":"or","general":"General","runCode":"Run code","submit":"Submit","closeTab":"Close tab","maximizePanel":"Maximize / Exit Maximize Panel","fullScreen":"Enter / Exit Full Screen","debug":"Debug","debugStart":"Start Debugging","debugStop":"Stop Debugging","debugSkipForward":"Skip Forward","debugStepOver":"Step over","debugStepIn":"Step in","debugStepOut":"Step out","debugRestart":"Restart","codeEditor":"Code Editor","editorIndent":"To indent one level","editorIndentFew":"To indent one fewer levels","editorMoveLines":"To move lines up / down","editorCut":"Delete line and copy to buffer","editorToggleComment":"Comment / uncomment current selection","editorUndo":"Undo action","editorRedo":"Redo action"},"advanced":{"categoryTitle":"Advanced","premiumTitle":"LeetCode Premium","premiumDesc":"Customize your learning experience within Dynamic Layout through LeetCode Premium.","learnMore":"Learn more","realTimeResizing":"Real-time resizing","realTimeResizingDesc":"Display content responds to panel resizing. Disable if you experiencing graphic performance issues.","multipleTab":"Open multiple instance in new tab","multipleTabDesc":"Elements from lists (solutions, submissions, etc.) can be opened in new tabs. Allowing multiple tabs to be opened at once.","openAfterActive":"Open in active panels","openAfterSimilar":"Open after last position of similar tabs","customLayout":"Save custom layout (cloud)","customLayoutDesc":"Premium users can store up-to 3 customized layouts.","upgrade":"Upgrade","view":"View","multipleTabUpdateAlert":{"title":"Update Settings?","desc":"Update this setting will automatically close all the solutions and submissions opened. Are you sure you want to update settings?","no":"No","update":"Update"}}},"preview":{"goBackTooltip":"Go back","goForwardTooltip":"Go forward","refreshTooltip":"Refresh","openInNewTabTooltip":"Open in new tab","upgradeToGetUrl":"Upgrade to premium to see link"},"previewConsole":{"isEmpty":"Console is empty","clearTooltip":"Clear console","clearedAt":"Console cleared at {{time}}"},"ideGuide":{"introIdeTitle":"Introducing Dynamic Layout","new":"NEW","introInfo":"Unleash your potential with the immersive and flexible coding environment","setTitle":"Show Run \u0026 Submit buttons in","setTip":"You can change the preference at any time in the settings","enableIde":"Enable Dynamic Layout","of":" of ","skipTour":"Skip tour","back":"Back","next":"Next","done":"Done","toolbarTitle":"Toolbar","toolbarContent":"A central hub for key tools such as Run Code, Submit, Notes, etc.","tabsTitle":"Tabs","tabsContent":"Customize your coding space by dragging tabs to create preferred layouts.","resizeTitle":"Resize Panels","resizeContent":"Adjust the workspace to fit your needs by resizing panes using the splitter.","maximizeTitle":"Maximize a Panel","maximizeContent":"Double-click the top bar of a pane to maximize and enhance focus.","expandCollapseTitle":"Expand / Collapse","expandCollapseContent":"Click to expand or collapse a pane, creating space for essential content.","settingsTitle":"Settings","settingsContent":"Customize for Dynamic Layout, Code Editor, Shortcuts and Advanced Settings.","maybeLater":"Maybe later"},"contest":{"toolbar":{"userAcceptedShort":"Users AC","userAccepted":"Users Accepted","userTriedShort":"Users","userTried":"Users Tried","totalAcceptedShort":"Total AC","totalAccepted":"Total Accepted","totalSubmissionsShort":"Submissions","totalSubmissions":"Total Submissions"},"navbar":{"classicMode":"Classic Mode"}},"collaboration":{"invite":"Invite","liveCollaboration":"Collaboration","beta":"Beta","invitePopoverDescBefore":"Invite collaborators to code together on this problem! The collaboration can last up to 3 hours.","invitePopoverDescAfter":"Invite collaborators to code together on this problem! The collaboration can last up to 3 hours.","createLink":"Create Link","copyTip":"Copy and share the link","copied":"Link Copied!","endCollaboration":"End Collaboration","leaveCollaboration":"Leave Collaboration","user":"User","clickToFollow":"Click to follow","clickToUnfollow":"Click to unfollow","failedToJoin":"Failed to Join","failedSignIn":"Please sign in to join this collaboration.","failedPremium":"To view the question of this collaboration, you must subscribe to premium.","failedMaximum":"This collaboration has exceeded the maximum capacity of 5 members. Please try again later.","failedDynamicLayout":"Collaboration is a Dynamic Layout exclusive feature.","failedNotFound":"Link expired or doesn't exist. Please check with the host of this collaboration for more information.","failedJoinedOtherRoom":"You can only join one room at the same time.","failedConnectionFailed":"Connection failed. Please check your internet connection and try again.","generalFailedTitle":"Collaboration Disconnected","failedEnd":"The collaboration has been terminated by the host.","failedSameUser":"Disconnected due to duplicated host connection.","failedHostLost":"Collaboration ended due to host disconnection.","failedMaxTime":"Maximum collaboration duration reached.","signIn":"Sign In","leave":"Leave","subscribe":"Subscribe","tryAgain":"Try Again","gotIt":"Got it","maybeLater":"Maybe later","enableDynamicLayout":"Enable Dynamic Layout","endCollaborationWarning":"Are you sure you want to end this collaboration? After it ends, members can no longer collaborate on coding.","leaveCollaborationWarning":"Are you sure you want to leave this collaboration? When left, You will no longer be able to collaborate on coding.","cancel":"Cancel","end":"End","switchProblem":"Switch Problem","switchProblemWarning":"Everyone in the collaboration will follow you in switching problems. Are you sure you want to switch?","switchLanguage":"Switch Language","switchLanguageWarning":"Switching the language will affect all participants. Are you sure you want to switch the language?","leavingQd":"Exit Current Page","leavingQdWarning":"You're collaborating on this problem. Do you want to leave?","confirm":"Confirm","switch":"Switch","readOnlyOnTip":"Set to read-only mode","readOnlyOffTip":"Set to edit mode","toast":{"joining":"Joining the collaboration...","joinedHost":"The collaboration is started!","joinedGuest":"You've joined in the collaboration. Enjoy it!","anotherParticipant":"Another Participant","userJoined":"{{user}} joined the collaboration","userLeft":"{{user}} left the collaboration","end":"The collaboration has been terminated by the host","leave":"You have exited the collaboration","sameUser":"Disconnected due to duplicated host connection","hostLost":"Collaboration ended due to host disconnection","maxTime":"Maximum collaboration duration reached","switchProblem":"{{user}} has changed the problem","switchLanguage":"{{user}} has changed the language","runCode":"{{user}} ran the code. Result: {{result}}","submit":"{{user}} submitted the code. Result: {{result}}","readOnlyOn":"The host has set you to read-only mode","readOnlyOff":"The host has set you to edit mode","readOnlyEdit":"You can't edit code in read-only mode","readOnlySwitch":"You can't switch question or language in read-only mode","logoutDisconnect":"You have signed out, please sign in and join in again."},"online":"Online","visitorTip":"LeetCoders studying this problem currently."}},"console":{"meta":{"title":"Question Detail"},"console":"Console","run":"Run","to":"to","or":"or","submit":"Submit","execute":"Execute","resetTestcases":"Reset Testcases","debug":"Debug","testcase":"Testcase","testcaseCount":"{{ count }}/{{ max }} testcases","debugger":"Debugger","testcaseNumber":"Case {{ number }}","cloneCurrentTestcase":"Clone current testcase","switchToRawEditor":"Use raw testcase editor","switchToTabEditor":"Use tab-based testcase editor","switchToRawResultEditor":"Use raw test result","switchToTabResultEditor":"Use tab-based test result","switchConsoleToLeft":"Move console to the left side of the page","switchConsoleToRight":"Move console to the right side of the page","testcasePlaceholder":"Enter Testcase","shellTestcaseBlocker":"You don’t need to set testcases for Shell problems.","showFullTree":"Click to view the entire tree","fullTreeTooBig":"Data is too large to display","sourceMode":"Source Mode","sourceModeText":"You can now edit all your testcases in one text editor.","line":"Line","case":"Case","noThanks":"No thanks","tryNow":"Try now","inconsistentResults":"Getting inconsistent results?","inconsistentResultsContent":"You might be using global/static variables or C/C++. The system executes all testcases using the same program instance. Global/static variables affect the program state from one test case to another.","gotIt":"Got it","readMore":"Read more","result":{"result":"Result","stdout":"Stdout","noResult":"You must run your code first","notAvailable":"Not available during contest.","slowdown":{"premium":"You have attempted to run code too soon. Please try again in a few seconds.","first":"You have attempted to run code too soon. Please try again in a few seconds, or","second":"Subscribe","third":"to reduce wait time."},"networkError":"Unknown network error. Please try reloading page.","serverError":"Unknown server error. Please contact our support team.","unknownError":"Something went wrong","compileError":"Compile Error","runtimeError":"Runtime Error","copyCompileError":"Copy error message to clipboard","copyContent":"Copy content to clipboard","copied":"Successfully copied to clipboard!","viewAll":"View all","viewLess":"View less","outputLimitExceeded":"Output Limit Exceeded","timeLimitExceeded":"Time Limit Exceeded","memoryLimitExceeded":"Memory Limit Exceeded","timeout":"Server Request Timeout","internalError":"Internal Error","accepted":"Accepted","finished":"Finished","wrongAnswer":"Wrong Answer","invalidTestcase":"Invalid Testcase","runtime":"Runtime","input":"Input","output":"Output","expected":"Expected","contribution":"Contribute a testcase","pending":"Pending...","premiumPending":"Pending...","judging":"Judging...","debugging":"Debugging...","speedUp":"Speed Up","lastExecutedInput":"Last Executed Input","openTestcase":"Open Testcase","testcasesPassed":"testcases passed","useTestcaseAsInput":"Use Testcase","addedTestcaseMessage":"Successfully added the test","testcaseExistsMessage":"Test already exists in editor","testPassedButTookTooLong":"Testcases passed, but took too long.","cantUseTestcaseAsInput":"Max # of testcases reached","maxTestcaseCountReached":"Max of {{ count }} testcases reached","debugger":"Debugger","moreLine_one":"more line","moreLine_other":"more lines","edit":"Edit","errorTestcaseMsg1":"You've found a test case the system can't handle. Please ","errorTestcaseActionMsg":"submit","errorTestcaseMsg2":" them to help us improve. Thank you!"},"ai":{"title":"LeetWiz","beta":"Beta","analyzingCode":"Analyzing code...","codeErrorHint":"Why am I getting this error?","fullName":"LeetWiz - Your AI helper","shortName":"LeetWiz","description":"Need some help? Try out our new AI assistant, LeetWiz! LeetWiz helps you progress and stay focused on what is important. It will help you identify the cause of runtime/compile errors and provide hints to help you fix them.","fixedError":"You seem to have fixed your runtime/compile error. Keep in mind I only support helping with runtime errors or compile errors for now 😊","morePremiumFeatures":"More premium features"},"info":{"info":"Info","content":"\u003c0\u003eAre 'Run' results inconsistent with 'Submit' results? If you are using global/static variables or C/C++, please check\u003c/0\u003e \u003c1\u003ethis\u003c/1\u003e \u003c0\u003eout.\u003c/0\u003e","ok":"Okay"},"visualizer":{"dataTooLarge":"Data too large to be displayed, input would be truncated.","parseFailed":"Failed to parse your input, please check again.","dataNotSupported":"This doesn't support visualization.","outputDataTypeNotSupported":"Output data type doesn't support visualization","initFailed":"Failed to init the canvas, please refresh the page and try again."},"verifyEmail":"verify email","nonVerifyMsg":"Please verify email to run your code","signToRunOrSubmit":"You need to Login/Sign up to {{action}}","signToRunAndSubmit":"You need to \u003c0\u003eLogin / Sign up\u003c/0\u003e to run or submit","verifyToRunAndSubmit":"You need to \u003c0\u003everify email\u003c/0\u003e to execute or submit your code","notAvailableDuringDebugging":"Not available during debugging","notAvailableDuringExecuting":"Not available during executing","frontendTestcases":{"reset":"Reset","lnCol":"Ln {{lineNumber}}, Col {{column}}","guideTooltip":"Testcase Guide","guideTitle":"Testcase Guide"},"createTestCaseTip":"How to Create Test Cases on LeetCode?"},"code-editor":{"commonConfirmTitle":"Are you sure?","fullScreen":"Full screen","exitFullScreen":"Exit full screen","autocomplete":{"button":"Auto","lspTooltip":"Intelligent code completion based on static code analysis.","basicTooltip":"Basic code completion.","basicWithLspError":"Basic code completion. Double-click to retry intelligent code completion.","lspConnectionError":"Intelligent code complete connection failed","lspNotSupportedTooltip":"The language is not supported by our platform","needToLoginTooltip":"Login to use autocomplete","notPremiumTooltip":"Upgrade to premium to use autocomplete"},"langInfo":"Language Information","settings":{"name":"Settings","fontSize":"Font size","fontSizeDesc":"Choose your preferred font size for the code editor.","theme":"Theme","themeDesc":"Tired of the white background? Try different styles and syntax highlighting.","themeDark":"Dark","themeLight":"Light","themeSystem":"System","keyBinding":"Key binding","keyBindingDesc":"Want to practice Vim or Emacs? We have these key binding options available for you.","keyBindingVim":"Vim","keyBindingEmacs":"Emacs","keyBindingStandard":"Standard","tabSize":"Tab size","tabSizeDesc":"Choose the width of a tab character.","spaces":"{{count}} spaces","wordWrap":"Word Wrap"},"shortcuts":{"name":"Editor Shortcuts","run":"Run code","submit":"Submit","debug":"Debug code","indent":"To indent one level","indentFew":"To indent one fewer levels","moveLines":"To move lines up/down","cut":"Delete line and copy to buffer","toggleComment":"Comment/uncomment current selection","undo":"Undo action","redo":"Redo action","note":"Note"},"reset":{"tip":"Reset to default code definition","confirmContent":"Your current code will be discarded and reset to the default code!","resetServer":"Continue to work on your code from {{time}}","restore":"Restore"},"history":{"title":"{{lang}} Submission Notes","tip":"Submission Notes","description":"Only the code submitted in the current language will be displayed; When you select and confirm the selection, your current code will be overwritten by the code you selected.","status":"Status","runtime":"Runtime","memory":"Memory","time":"Time","topic":"Topic","notes":"Notes","noNotes":"You haven't added notes to any submissions yet!"},"timer":{"start":"Start timer","hide":"Hide timer","show":"Show timer","reset":"Reset timer","pause":"Pause","continue":"Continue","contest":{"penaltyTimeDescription":"Penalty time: 5 min for each wrong submission"}},"debugger":{"loginToDebug":"You need to Login / Sign up to debug","name":"Debugger","stdout":"Standard output","input":"Input","enterTip":"Click on line number to add breakpoints","exit":"Exit","start":"Start Debug","stop":"Stop Debug","startShort":"Debug","stopShort":"Stop","watch":"Watch Expressions","local":"Local Variables","watchHolder":"Please enter the watch expressions value","controlStart":"Start Debug","controlForward":"Skip forward","controlStepOver":"Step over","controlStepOut":"Step out","controlStepIn":"Step in","controlReset":"Restart","exited":"Debugger session exited, terminate it?","startToWatch":"Start debugging session to see watch expressions","watchTip":"You need to Start debugging to add value","startViewVars":"Start debugging session to see local variables","noVars":"No local variables detected","startViewOutput":"Start the debugging session to check output here","noOutput":"No output yet...","edited":"Code has been modified, please restart the debugger","cantAddTestcase":"You have reached maximum number of testcases","langNotSupported":"{{lang}} doesn't support debugger","expressionsNotSupported":"{{lang}} not supported","notPremium":"Upgrade to premium to use debugger","oneClickDebug":"One Click Debug","cppAdditionalTip":"Based on GDB. View the value of nums[i] with *(\u0026nums[i])."},"markDownPlaceholder":"Type here...(Markdown is enabled)","retrieveCode":{"tip":"Retrieve last submitted code","confirmContent":"Your code will be discarded and replaced with your last submission's code!","noData":"You haven't submitted any code!"},"editor-position":"Ln {{lineNumber}}, Col {{column}}","framework":{"switchTooltip":"Switch framework","modalTitle":"Select Framework","modalDescription":"Choose your preferred framework to start with.","modalConfirmTitle":"Confirm switching framework","modalConfirmText":"Changing the framework will reset the unsubmitted code. Are you sure you want to proceed?","modalConfirmBtn":"Proceed","toastSwitchSuccess":"Description has been updated for the {{framework}}.","guide":{"selectFramework":"Select Framework","selectFrameworkDescription":"You can switch to your desired framework from here.","selectFrameworkConfirm":"Got it"}},"saveCode":{"restoredFromCloud":"Restored from Cloud","restoredFromLocal":"Restored from local","upgradeToCloud":"Upgrade to Cloud Saving","savedToCloudToast":"All changes are automatically saved to cloud for Premium user.","savedToLocalToastFirst":"Your code is saved to local, ","savedToLocalToastSecond":" to enable cloud saving.","upgradeToPremium":"upgrade to Premium","savedToCloud":"Saved","savedToLocal":"Saved","saving":"Saving..."},"format":{"tip":"Format Code","formatted":"Formatted!"},"exceedMaxLineLength":"For performance reasons, the number of characters per line is limited to 10,000."},"description":{"status":{"tried":"Attempted","ac":"Solved"},"ok":"OK","somethingWentWrong":"Something went wrong","thanksForVoting":"Thanks for voting!","topics":"Topics","companies":"Companies","pastSixMonths":"0 - 6 months","pastYear":"6 months - 1 year","pastTwoYears":"1 year - 2 years","lastThreeMonths":"0 - 3 months","lastSixMonths":"0 - 6 months","SixMonthsAgo":"6 months ago","hint":"Hint","showHints":"Show Hints","moreActions":"More Actions","feedback":"Feedback","showEnglish":"Show English Translation","showChinese":"Show Chinese Translation","addToListError":"Something went wrong. Please try again.","feedbackForm":{"optionRequiredError":"Please select at least one option.","title":"Feedback","alternative":"You may also \u003c0\u003esubmit via Github\u003c/0\u003e to get feedback in real time.","cancel":"Cancel","submit":"Submit","issuesEncountered":"Issues Encountered","problem":"Problem","additionalFeedback":"Additional Feedback","description":"We try to keep our questions to the highest quality possible. Could you please tell us why you disliked this question?","somethingWentWrong":"Something went wrong","options":{"unclearDescription":"Description or examples are unclear or incorrect","unclearDifficulty":"Difficulty is inaccurate","unclearTestCases":"Testcases are missing or incorrect","runtimeStrict":"Runtime is too strict","edgeCases":"Edge cases are too frustrating to solve","other":"Other","otherPlaceholder":"Additional feedback"}},"accepted":"Accepted","submissions":"Submissions","acRate":"Acceptance Rate","copyright":"Copyright ©️ {{year}} LeetCode All rights reserved","yes":"Yes","no":"No","add2":"Add","seenBefore":"Seen this question in a real interview before?","whichCompany":"Which Company?","whichPosition":"which Position?","whichTimePeriod":"When did you encounter this question?","whichStage":"Which interview stage?","thanksForFeedback":"🎉 Thank you for your feedback!","relatedTopics":"Related Topics","add":"Add","remove":"Remove","createNewList":"Create a new list","nameListPlaceholder":"Enter a list name","cancel":"Cancel","save":"Save","setAsPrivate":"Set as Private","addToList":"Add to List","sqlSchema":"SQL Schema","pandasSchema":"Pandas Schema","confirm":"Confirm","favoriteSignInError":"Sign in to access your lists","feedbackSignInError":"Sign in to give feedback","likeSignInError":"Sign in to like or dislike this question","schemaCopySuccess":"Successfully copied to clipboard","shareQuestionDescription":"Check out this coding interview problem on LeetCode!","viewMyLists":"View my Lists","searchPlaceholder":"Search...","similarQuestions":"Similar Questions","discussion":"Discussion ({{commentCount}})","myLists":"My Lists","create":"Create","addProblemToListSuccess":"Added to ","addedSuccess":"Added success","removeProblemFromListSuccess":"Removed from {{listItemName}}","viewAllLists":"View all lists","listUnExist":"List does not exist","companyListUnExist":"Company list does not exist","listContextNull":"Could not get list context","listContextEmpty":"This list is empty.","companyListContextEmpty":"This company list is empty.","view":"View","points":"pt."},"submissions":{"runtime":"Runtime","memory":"Memory","beat":"Beats","noData":"No data","noSubmission":"Submission does not exist","noCode":"There is no code here","copied":"Copied","pending":"Pending...","testPassedButTookTooLong":"Testcases passed, but took too long.","submittedAt":"submitted at","fullCode":"Full Code","allSubmissions":"All Submissions","success":{"accept":"Accepted","timeTaken":"Time taken: {{time}}","nextQuestion":"Next question","moreChallenges":"More challenges","second_short":"s","minute_short":"m","hour_one":"hr","hour_other":"hrs","solution":"Solution","beatsPercentage":"Beats {{percent}}%","ofUsersWithLanguage":"of users with {{language}}"},"details":{"myCode":"My Submitted Code","otherCode":"My Submitted Code","sampleCode":"Sample {{metric}} submission","backToMyCode":"Back to my position","chartHintForAction":"Click on the chart to check sample codes","fetchingCodeFromServer":"Fetching code from server..."},"buttons":{"close":"Close","details":"Details","solution":"Solution"},"filters":{"allStatuses":"All statuses","allLanguages":"All languages","status":"Status","language":"Language","framework":"Framework","time":"Time","runtime":"Runtime","memory":"Memory","notes":"Notes","penaltyTime":"Penalty Time","minute":"Min"},"notes":{"label":"Notes","placeholder":"Write your notes here"},"relatedTags":{"label":"Related Tags","placeholder":"Select related tags","startTyping":"Start typing to find a tag","noResults":"No tags found"},"chart":{"runtimeDescription":"Accepted Solutions Runtime Distribution (%)","memoryDescription":"Accepted Solutions Memory Distribution (%)","runtimeShortDescription":"Distribution (%)","memoryShortDescription":"Distribution (%)","youAreHere":"You are here!","hintForAction":"Click the distribution chart to view more details","runtime":"Runtime","memory":"Memory","percentLabel":"{{percent}}% of solutions used","runtimeValueLabel":"{{value}} ms of runtime","memoryValueLabel":"{{value}} MB of memory","noData":"Sorry, there are not enough accepted submissions to show data","codeSample":"Code Sample","runtimeCodeSampleInfo":"Runtime: {{value}}ms","memoryCodeSampleInfo":"Memory: {{value}}mb","resetZoom":"Click on the minimap to reset","complexity":"Complexity","runtimeTip":"This metric calculates the function's runtime (effective from 2024.10.19. Submissions made before this date will remain unchanged and will be ranked along with the new data)."},"nonSignedIn":{"signInTitle":"🔥 Join LeetCode to Code!","signInInfo":"View your Submission records here","signInButton":"Register or Sign In"},"failedSubmission":{"runtimeError":"Runtime Error","compileError":"Compile Error","lastTestcase":"Last Executed Input"},"submissionPreview":{"embedCode":"Embed Code","copyEmbedCode":"Copy","copiedEmbedCode":"Copied!","copyEmbedCodeTooltip":"Copy embed code","copyLinkTooltip":"Copy link","openInNewTabTooltip":"Open in new tab","openInPanelTooltip":"Open in panel","maximizeTooltip":"Maximize","minimizeTooltip":"Minimize","invalidSubmissionIdLabel":"Invalid Submission ID","missingSubmissionIdTooltip":"Please enter a Submission ID","nonFeSubmissionIdTooltip":"Please enter a Frontend Question Submission ID","openIn":"Open in"},"complexity":{"timeComplexity":"Time Complexity","spaceComplexity":"Space Complexity","analyzeComplexity":"Analyze Complexity","accurate":"Helpful","notAccurate":"Not helpful","notAccurateTitle":"Not helpful","placeholder":"Inaccurate results, or other feedback?","premiumLimit":"You have attempted to analyze complexity too soon. Please try again tomorrow.","limitTitle":"Upgrade to Analyze more","limitContent":"You have reached analyzing rate limit for today. Upgrade to Premium for enhanced accuracy and further analyzing.","learnMore":"Learn more","subscribe":"Subscribe","tryLater":"The server is busy, please try again later.","noteEmpty":"Please enter some content before submitting."}},"feature-guide":{"layout":"Drag the divider to resize the window based on your preference!","timer":"\u003c0\u003eTimer:\u003c/0\u003e Use the new timer feature to record how much time you spend solving a question!","debugger":"\u003c0\u003eDebugger:\u003c/0\u003e Use the debugger feature to make debugging easy peasy.","problemSwitch":"Quickly navigate to the \u003c0\u003eprevious/next question\u003c/0\u003e here","problemList":"Quickly navigate to the \u003c0\u003eprevious page\u003c/0\u003e here","discussion":"Post any ideas in the \u003c0\u003eDiscussion\u003c/0\u003e. If you want to share a solution, share it under the solution tab!","solution":"Share your solution with other users, and find LeetCode's official solution alongside other users' solutions here.","back":"Back","skip":"Skip","next":"Next","ok":"OK","title":"🎉 Introducing our new question page!"},"feature-guide-dynamic":{"back":"Back","skip":"Skip","next":"Next","explore":"Explore","step1":{"title":"Introducing Dynamic Layout","des":"Enjoy the enhanced flexibility and immerse yourself in the coding environment offered by LeetCode's upgraded Dynamic Layout.","tip":""},"step2":{"title":"Move","des":"Drag tabs/panes to create your custom coding layout effortlessly.","tip":""},"step3":{"title":"Resize","des":"Grab the splitter between panes to resize them, tailoring the workspace to your preferences.","tip":""},"step4":{"title":"Maximize","des":"Maximizing a panel by double-clicking its top, enhancing your coding immersion.","tip":""},"step5":{"title":"New Toolbar","des":"The toolbar: your hub for notes, timer, debugger, run code and submit.","tip":""}},"solutions":{"filter":{"searchPlaceholder":"Search...","tags":{"all":"All","mySolution":"My Solution"},"sortBy":{"placeholder":"Sort by","hot":"Hot","most_posts":"Most Posts","most_relevant":"Most Relevant","most_votes":"Most Votes","newest_to_oldest":"Most Recent","oldest_to_newest":"Oldest to Newest","recent_activity":"Recent Activity","hot_short":"Hot","newest_to_oldest_short":"Recent","most_votes_short":"Votes","most_relevant_short":"Relevant"}},"solution":"Solution","writeSolution":"Solution","continueSolution":"Solution","videoSolutionTooltip":"Video Solution","premiumOnlyTooltip":"Premium Solution","tags":{"official":"Official","pinned":"Pinned","favorite":"My Favorite","mySolution":"My Solution","hidden":"Hidden"},"post":{"invalidSolutionTitle":"Unable to load the solution","invalidSolutionDescription":"Please try exploring other solutions","prevLabel":"Previous","nextLabel":"Next","isAdmin":"Admin","reputationTooltip":"Reputation","share":"Share","addToCollection":"Favorite","isInCollection":"Favorite","votes":"({{votesCount}} votes)","shareCopySuccess":"Copied link to clipboard","addToFavoriteSuccess":"Added to favorite solutions","removeFromFavoriteSuccess":"Removed from favorite solutions","feedbackTooltip":"Feedback","backToTop":"Back to top","genericError":"Something went wrong","signInVoteError":"You must sign in to vote","verifyVoteError":"You must verify your email to vote","rateSuccess":"Thanks for rating this solution!","upvote":"Upvote","comments":"Comments","allSolutions":"All Solutions","more":{"error":"Something went wrong","cancel":"Cancel","edit":"Edit","subscribe":"Subscribe","subscribeMessage":"Subscribed","unsubscribe":"Unsubscribe","unsubscribeMessage":"Unsubscribed","delete":"Delete","deleteMessage":"Deleted","deleteConfirmText":"Are you sure you want to delete this post?","deleteConfirmBtn":"Delete","restore":"Restore","restoreMessage":"Restored","restoreConfirmText":"Are you sure you want to restore this post?","restoreConfirmBtn":"Restore","report":"Report","reportMessage":"Reported","pin":"Pin","pinMessage":"Pinned","pinConfirmText":"Are you sure you want to pin this post?","pinConfirmBtn":"Pin","unpin":"Unpin","unpinMessage":"Unpinned","unpinConfirmText":"Are you sure you want to unpin this post?","unpinConfirmBtn":"Unpin","hide":"Hide","hideMessage":"Hid the post","hideConfirmText":"Are you sure you want to hide this post?","hideConfirmBtn":"Hide","hideFromTrending":"Hide from trending","hideFromTrendingMessage":"Hid post from trending","hideFromTrendingConfirmText":"Are you sure you want to hide this post from trending?","hideFromTrendingConfirmBtn":"Hide from trending","show":"Show","showMessage":"Showed the post","showConfirmText":"Are you sure you want to show this post to everyone?","showConfirmBtn":"Show","moveToDiscussion":"Move to Discussion","moveToDiscussionMessage":"Moved to Discussion","moveToDiscussionConfirmText":"Are you sure you want to move this post to Discussion?","moveToDiscussionConfirmBtn":"Move to Discussion","saved":"Saved","editorsPick":"EditorsPick","officialPick":"OfficialPick","uneditorsPick":"unEditorsPick","undelete":"unDelete","unmute":"unMute","unofficialPick":"unOfficialPick","unsunk":"unSunk","sunk":"Sunk","mute":"Mute"}},"searchResult":{"commentPrefix":" comment","replyPrefix":" reply to ","colon":": "},"noDirectResultsHint":"No results. Here are some related threads.","noResults":"There aren't any solution topics here yet!","noMoreResults":"No more results","backToTop":"Back to top","report":{"reportModalTitle":"Report this content","contentPlaceholder":"Additional feedback","cancel":"Cancel","confirm":"Confirm","advertising":"Spam advertising","sexual":"Sexual content","violent":"Violent content","terrorism":"Promotes terrorism","illegal":"Illegal content","abuse":"Abuse others","nonEnglish":"Non English content","other":"Others","reportSuccess":"Report submitted!","reportError":"Couldn't submit the report, please try again"},"blocker":{"subscribeToUnlock":"Subscribe to unlock.","subscribeSubTitle":"Thanks for using LeetCode! To view this solution you must subscribe to premium.","subscribe":"Subscribe"},"switchToRightTooltip":"Move to right","switchToLeftTooltip":"Move to left","switchFirstTimePopoverContent":"Click \"Switch Layout\" to move the solution panel right or left.","switchFirstTimePopoverBtn":"Got it","shareSolutionBanner":{"lastSubmissionBeats":"Your last submission beat \u003c0\u003e{{percentage}}\u003c/0\u003e of other submissions' runtime.","lastSubmissionBeatsSmall":"Your submission beat \u003c0\u003e{{percentage}}\u003c/0\u003e of others' runtime.","lastSubmissionMemoryBeats":"Your last submission beat \u003c0\u003e{{percentage}}\u003c/0\u003e of other submissions' memory usage.","lastSubmissionMemoryBeatsSmall":"Your submission beat \u003c0\u003e{{percentage}}\u003c/0\u003e of others' memory usage.","signInAndShareSolutions":"Sign in and share solutions.","signIn":"Sign In","shareMySolution":"Share my solution","share":"Share","getACSubmissionsToPublish":"Submit at least 1 AC to publish a solution."},"sideBySide":{"enterMode":"Enter Side by Side Mode","exitMode":"Exit Side by Side Mode","modeOn":"Side by Side Mode on","modeOff":"Side by Side Mode off","enterGuideTitle":"View multiple content?","enterGuideDesc":"Try switching to Side by Side Mode. You can further customize your viewing experience in settings.","exitGuideTitle":"Exit Side by Side Mode","exitGuideDesc":"Exit Side by Side Mode to focus on one tab.","goToSettings":"Go to Settings","gotIt":"Got It"}},"comments":{"edited":"(Edited)","tooShort":"Comment is too short","noComments":"No comments yet.","reply":"Reply","mentionInputPlaceholder":"Tag a user or a problem","user":"Users","problem":"Problems","mdRules":{"inlineCode":"your inline code...","codeBlock":"code block","link":"leetcode","href":"https://leetcode.com"},"pinnedBy":"Pinned by {{pinnedBy}}","share":"Share","edit":"Edit","save":"Save","shareCopySuccess":"Copied link to clipboard","hideReplies":"Hide Replies","showReplies":"Show {{num}} Replies","cancel":"Cancel","confirm":"Confirm","preview":"Preview","comment":"Comment","typeCommentHere":"Type comment here... (Markdown supported)","comments":"Comments","sortBy":"Sort by","newestToOldest":"Newest to Oldest","oldestToNewest":"Oldest to Newest","mostVotes":"Most Votes","best":"Best","editor":"Editor","youMust":"You must","verifyYourEmail":"verify your email","first":"first","readMore":"Read more","somethingWentWrong":"Something went wrong","areYouSure":"Are you sure?","confirmDeleteComment":"Are you sure you want to delete this comment?","confirmRestoreComment":"Are you sure you want to restore this comment?","confirmHideComment":"Are you sure you want to hide this comment from non-authors?","confirmShowComment":"Are you sure you want to show this comment to everyone?","confirmPinComment":"Are you sure you want to pin this comment?","confirmUnpinComment":"Are you sure you want to unpin this comment?","reward":"Reward","delete":"Delete","hide":"Hide","show":"Show","askQuestion":"Ask Question","feedback":"Feedback","tips":"Tips","chooseAType":"Choose a type","showMoreReplies":"Show more replies","hideSuccess":"Comment hidden from non-authors.","showSuccess":"Comment now visible to everyone.","pinSuccess":"Comment has been pinned.","unpinSuccess":"Comment has been unpinned.","deleteSuccess":"Comment Successfully Deleted","restore":"Restore","restoreSuccess":"Comment Successfully Restored","hidden":"Hidden","report":"Report","pin":"Pin","pinned":"Pinned","unpin":"Unpin","hideComment":"Hide Comment","showComment":"Show Comment","move":"Move to Solution","moveTitle":"Title:","moveTitlePlaceholder":"Enter title here","moveSuccess":"Comment successfully moved","genericError":"Something went wrong","postSuccess":"Comment successfully posted"},"post-solution":{"meta":{"newTitle":"{{title}} - LeetCode - New Solution","editTitle":"{{title}} - LeetCode - Edit Solution"},"filterTopic":"Filter topics","publishSolution":"Solution","publishSolutionTooltip":"Submit at least 1 AC to publish a solution","restore":"Restore from draft","overwriteWithLastAc":"Overwrite with the latest AC submission","generatedWithSources":{"lastAc":"Generated from the latest AC submission","submission":"Generated from the chosen submission","draft":"Restored from draft"},"editingSolution":"Editing the existing solution","blockCode":"Code Block","tag":"Tag","related":"Related","selectATag":"Please select at least one tag","post":"Post","publishError":"Could not publish solution","imgUploadSuccuss":"Upload successfully","imgUploadError":"Upload failure","guideTooltip":"Markdown Guide","saved":"Saved"},"new-study-plan":{"detail":{"metadata":{"title":"{{plan}} - Study Plan - LeetCode","description":"Level up your coding skills and quickly land a job. This is the best place to expand your knowledge and get prepared for your next interview.","notFound":"Not Found"},"weekTextAbbr":{"sun":"SUN","mon":"MON","tue":"TUE","wed":"WED","thu":"THU","fri":"FRI","sat":"SAT"},"weekText":{"sun":"Sunday","mon":"Monday","tue":"Tuesday","wed":"Wednesday","thu":"Thursday","fri":"Friday","sat":"Saturday"},"myPlan":"My Plan","problemLeft":"problem left","problemsLeft":"problems left","notification":"Notification","setUpSp":"Set up a study plan","solvedText":"Solved","problem":"problem","problems":"problems","learnMore":"Learn More","you":"You","weeklyRanking":"Weekly Ranking","weeklyRankingToolTip":"The ranking is based on the number of solved problems in this problem list this week, and the leaderboard is updated hourly (no ranking is calculated if no problems are solved this week).","solvePrev":"I commit to solve","solveNext":"problems on every","startTitle":"New Study Plan","confirmStartText":"Once you save it, you cannot make any modifications. Start now?","quitTypeTipPrev":"Quit the study plan by typing ","quitTypeTipNext":" below.","subscribeToUnlock":"Subscribe to unlock","subscribeToUnlockContent":"Thanks for using LeetCode! To view this study plan you must subscribe to premium.","start":"Start","share":"Share","backToExplore":"Back to Plan List","goCurrentPage":"retry this study plan","premiumTip":"Premium Study Plan","copyLink":"Copy Link","copiedSuccess":"Copied to clipboard","more":"More","quit":"Quit","back":"Back","quitTitle":"Are you sure?","quitContent":"When you quit your study plan, all problem solved statues will be reset and you can't restore progress. Are you sure you want to quit?","showTags":"Show tags","summary":"Summary","showMore":"Show More","showLess":"Show Less","award":"Award","awardCongratulation":"Congratulations! You have already earned this badge.","related":"Related","viewMore":"View More","todo":"Todo","attempted":"Attempted","solved":"Solved","markAsSolved":"Mark As Solved","markAsSolvedTip":"You have already solved this question in other place, do you want to “Mark as solved” here?","difficulty":"Difficulty","congratulation":"🎉 Congratulations!","solvedAllProblemsText":"You just solved all the problems from {{title}}!","checkBadge":"Check out the badge on your","profilePage":"Profile page","wearGlory":"and wear the glory!","checkMyStudyPlan":"Check My Study Plan","joinSuccessfully":"Join Successfully","quitSuccessfully":"Quit Successfully","setSuccessfully":"Set Successfully","errorTip":"Something wrong, please try again.","quitTip":"When you quit your study plan, all problem solved statues will be reset and you can't restore progress.","pastSolved":"Past Solved","solution":"Solution","points":"pt.","ranking":"Ranking"},"list":{"metadata":{"title":"Study Plan - LeetCode","desc":"Start a study plan that's tailored to your needs to maximize your learning potential. Track your progress and make consistent growth!"},"title":"Study Plan","ongoing":"Ongoing","myPlan":"My Study Plan","featured":"Featured","showMore":"Show More","revertOldPlan":"Revert to the old study plan","revertOldPlanTipTitle":"🌟 Revert to the old version","revertOldPlanTipDesc":"You can click this button to revert to the old study plan","cancel":"Cancel","iSee":"I see"},"myStudyPlan":{"metadata":{"title":"LeetCode - The World's Leading Online Programming Learning Platform","desc":"Level up your coding skills and quickly land a job. This is the best place to expand your knowledge and get prepared for your next interview."},"title":"My Study Plan","ongoing":"Ongoing","history":"History","noOngoingPlan":"You don’t have the ongoing plan","noHistoryPlan":"You don’t have the history plan"},"common":{"studyPlan":"Study Plan","tryNow":"Try it now!","noTanks":"No, thanks","newPlan":"✨ Brand New Study Plan!","newPlanDesc":"Join a new study plan to maximize your learning potential. Track your progress and focus on the daily questions to make consistent growth","seeAll":"See all","totalProgress":"Total Progress","totalScore":"Total Score","progress":"Progress","completed":"Completed","giveUp":"Give up","ongoing":"Ongoing","ongoingStudyPlan":"Ongoing Study Plan","later":"Later","joinInQDTitle":"Start this study plan?","joinInQD":"Join the study plan to maximize your learning potential. Track your progress and focus on the daily questions to make consistent growth","doNotRemind":"Do not remind me today","exploreButton":"Explore Study Plan","notFoundText":"Sorry, this page could not be found, please check your spelling or explore a new study plan"},"survey":{"submit":"Submit"},"satisfactionSurvey":{"submitBtnText":"Get LeetCoins"}},"problemlist":{"metadata":{"defaultTitle":"Problem List - LeetCode","title":"{{title}} - LeetCode"},"tags":"Tags","todo":"Todo","attempted":"Attempted","solved":"Solved","move":"Move","removeFromList":"Remove from List","addToList":"Add to List","moveToTop":"Move to Top","moveToBottom":"Move to Bottom","nullList":"Oops! This list is no longer available.","privateList":"This is a private list","noQuestions":"No questions in this list yet","goToProblemSet":"View all questions","difficulty":{"easy":"Easy","medium":"Med.","hard":"Hard"},"nav-panel":{"title":"My Lists","fold":"Fold","unfold":"Unfold","createdByMe":"Created by me","savedByMe":"Saved by me","public":"Public","private":"Private","remove":"Remove","listInvalid":"Invalid List"},"description":{"cover":{"editCover":"Edit Cover","emojis":"Emojis","image":"Image","random":"Random","background":"Background","chooseBackground":"Choose a background","Recommend":"Recommend","Smileys \u0026 Emotion":"Smileys \u0026 Emotion","People \u0026 Body":"People \u0026 Body","Animals \u0026 Nature":"Animals \u0026 Nature","Food \u0026 Drink":"Food \u0026 Drink","Activities":"Activities","Travel \u0026 Places":"Travel \u0026 Places","Objects":"Objects","Symbols":"Symbols","Flags":"Flags","uploadImage":"Upload Image","uploadRecommendedSize":"Recommended size Is 200 x 200 pixels","uploadSizeLimit":"The maximum size per file is 5 MB.","cancel":"Cancel","save":"Save"},"operations":{"questions":"questions","public":"Public","private":"Private","publicToast":"List is now public","privateToast":"List is now private","practice":"Practice","random":"Random","listSave":"Save","listSaved":"Saved","listSavedToast":"Saved!","listUnsavedToast":"Removed!","share":"Share","fork":"Fork","forkToast":"List forked!","more":"More","delete":"Delete","deleteList":"Delete list","deleteAlert":"Are you sure you want to delete this list? This action cannot be undone.","cancel":"Cancel","acceptDelete":"Delete","deleteToast":"List deleted!","edit":"Edit","editListInfo":"Edit list info","title":"Title","description":"Description","descriptionPlaceholder":"Describe your list","save":"Save","infoSavedToast":"Changes saved!","clickToReadMore":"Click to read more","nonLoggedInDialog":{"saveTitle":"Save list","saveContent":"Log in to save list.","forkTitle":"Fork list","forkContent":"Log in to fork list.","notNow":"Not now","logIn":"Log in"}},"progress":{"progress":"Progress","resetProgress":"Reset progress","resetAlert":"Resetting progress will move all questions back to incomplete. This action cannot be undone.","cancel":"Cancel","reset":"Reset","resetToast":"Progress Reset!","easy":"Easy","medium":"Med.","hard":"Hard","solved":"Solved","acceptance":"Acceptance","beats":"Beats","attempting":"Attempting","checkReset":"Clear codes saved in code editor"}},"company":{"nullList":"Oops! This company is no longer available.","subscribeText1":"Unlock more popular interview questions with","subscribeText2":"LeetCode Premium to enhance interview prep!","subscribe":"Subscribe","learnMore":"Learn More","freeQuestion":"1 free interview question","claim":"Claim","claiming":"Claiming for you...","saved":"Saved","updated":"Updated: ","description":"Description","filter":"Filter","status":"Status","todo":"Todo","attempted":"Attempted","solved":"Solved","difficulty":"Difficulty","easy":"Easy","medium":"Medium","hard":"Hard","role":"Role","rolePlaceholder":"Select role","reset":"Reset","tags":"Tags","showTags":"Show tags","frequency":"Frequency","discuss":"Discuss","chanceUsedUp":"Chance used up. Subscribe to Premium for more. ","subscribeNow":"Subscribe Now","claimSignIn":"Sign in to claim 1 free interview question. ","signIn":"Sign in","clickToReadMore":"Click for details","interviewTime":"Questions asked in","interviewTimeTip":"Progress is associated with the timeframe you chose.","frequencyTip":"Sort by frequency from high to low.","ok":"OK"},"points":"pt."},"contest":{"meta":{"title":"Contest - LeetCode","description":"Enhance your coding abilities and get valuable real-world feedback by participating in contests on LeetCode. You can also win up to 5000 LeetCoins per contest, as well as bonus prizes from sponsored companies.","keywords":"","ogImage":"https://leetcode.com/static/images/LeetCode_Sharing.png"},"featuredContests":"Featured Contests","sponsorContest":"Sponsor a Contest","contest":"Contest","ranking":"Ranking","startsIn":"Starts in","endsIn":"Ends in","addToCalendar":"Add to Calendar","pastContests":"Past Contests","myContests":"My Contests","public":"Public","virtual":"Virtual","startVirtualContestDescription":"Start a Virtual Contest. Get well-prepared for a ranked match.","whatIsVirtualContest":"What's a Virtual Contest?","virtualContestModal":{"title":"Would you like to start a Virtual Contest?","ongoingTitle":"Would you like to start a new Virtual Contest?","confirmTitle":"Virtual Contest Started","goToContest":"Go to Contest","resumeOngoing":"Resume Ongoing","startNew":"Start New","confirmDescription":"Let‘s go to your Virtual Contest!","freshStartDescription":"Virtual Contests are a way to take part in previous contests. The experience is as close as it gets to real participation, but your rank is not affected.","ongoingDescription":"You already have an ongoing virtual contest. Do you want to drop the ongoing one and start a new one? If you choose so, your current process WILL NOT be saved.","start":"Start Virtual Contest","cancel":"Cancel"},"attended":"Attended","globalRanking":"Global Ranking","rating":"Rating","ratingTooltip":"Rating displayed is the net change from your previous rating followed by your new rating.","viewMore":"View More","virtualContest":"Virtual Contest","finishTime":"Finish Time","solved":"Solved","localTimeBased":"Date \u0026 time is based on the local timezone settings on your device","ratingPending":"Rating update is currently pending","finishTimeTooltip":"Acceptance time of your last solved problem plus penalty time","joinContests":"🏆 Join LeetCode Contests","viewContestInfo":"Register or sign in to view your personalized contest information","registerOrSignIn":"Register or Sign In","crownAlt":"Crown","noContests":"You haven't joined any contests yet.","randomVirtualContest":"Random Virtual Contest","ended":"Ended","rankingPage":{"meta":{"title":"Ranking of {{title}} - LeetCode"},"problemList":"Problem List","ranking":"Ranking","rankingDetailPage":"Ranking Detail Page","titlePrefix":"Ranking of ","titleSuffix":"","akSuffix":" AK!","akTip":"\"AK,\" meaning \"All Killed,\" indicates all problems were solved.","pending":"Pending","ended":"Ended","emptyRankingPlaceholder":"Wish you first to AK","rank":"Rank","rankTipTitle":"While the contest is in progress:","rankTip1":"Rankings may not be updated in real time and could include outdated information.","rankTip2":"Only show the top 200 users","rankTipPending":"Ranking confirmation in progress.","rankTipUpdated":"The ranking results have been confirmed.","rankTipUnrated":"The contest has been unrated.","name":"Name","score":"Score","finishTime":"Finish Time","finishTimeTip":"Acceptance time of your last solved problem plus penalty time","questionPrefix":"Q","bugTipSuffix":" incorrect attempt(s)","you":"You","code":"Code","reportCheating":"Report Cheating","reportCheatingOtherRegion":"Report Cheating in CN Site","reportCheatingSubmitted":"Your report has been submitted. Thanks!","reportCheatingPlaceholder":"You can report solution using disallowed library functions or copying code from other resource as cheating","submit":"Submit","guideTitle":"View Code","guideDescription":"Click here to view the submission.","ok":"OK","tag":"Tag","colon":": "}}},"zh":{"common":{"404":{"title":"力扣","pageNotFound":"页面不存在","message":"抱歉！我们找不到您想访问的页面..."},"meta":{"title":"","description":"","keywords":""},"ok":"好","cancel":"取消","confirm":"确认","update":"更新","submit":"提交","save":"保存","netFailed":"网络错误","header":{"logo":{"url":"","description":""},"title":{"problemset-all":""},"action":{"login":{"text":"","url":""}}},"conjunctions":{"and":"and","or":"或"},"pages":{"leetcode":"LeetCode","explore":"学习","problems":"题库","interview":{"interview":"求职","onlineInterview":"在线面试","assessment":"Assessment"},"contest":"竞赛","discuss":"讨论","store":{"store":"商店","redeem":"力扣周边","premium":"Plus 会员","shop":"精品商城"},"admin":{"admin":"管理员","library":"题库","translation":"翻译","operations":"运营管理","scores":"点数","contribute":"贡献","backend":"后台管理","twoStepVerification":"二步验证","internalContest":"Internal Contest Dashboard","contestAdmin":"Contest Cheating Dashboard","dangerZone":"Danger Zone","review":"Review","contestDashboard":"Contest Dashboard"},"mobileApp":"下载 App","playground":"Playground","myPlayground":"我的 Playground","signIn":"登录","register":"注册","signOut":"退出"},"userMenu":{"renew":"续订","getPremium":"升级 Plus 会员享专属特权","tryNewFeatures":"体验新功能","orders":"订单","resume":"个人资料","translateQuestions":"题目以中文展示","translateQuestionsEn":"题目以英文显示","enterprise":"企业招聘","revertToOldVersion":"经典模式","categories":{"myList":"收藏夹","notebook":"笔记本","submissions":"我的题解","session":"进度管理","points":"积分","progress":"进展分析"},"unmockUser":"Unmock User","account":"账号设置","appearance":"外观","appearanceContent":{"auto":"跟随系统","light":"浅色","dark":"深色"}},"streakCounter":{"finished":"干的好！明天再来挑战！","unfinished":"解决今天的「每日 1 题」，刷新你的连胜记录！","buyTimeTravelTicket":"购买补签卡","missedOneDayThisMonth":"这个月你错过了 1 天.","missedDaysThisMonth":"这个月你错过了 {{count}} 天."},"playground":{"playground":"Playground","remainingPlaygrounds":"数量","renew":"升级","myPlaygrounds":"我的 Playgrounds","templates":{"consoleApplication":"控制台程序","empty":"空白 Playground","frontend":"前端程序","machineLearning":"机器学习"}},"links":{"admin":{"scores":"/library/scores","translation":"/contribution/translation/question/admin/","operations":"/management"},"premium":"/premium","discuss":"/circle","interview":"/company","shop":"https://detail.youzan.com/show/goods/newest?alias=271n43vr9hen7","onlineInterview":"https://leetcode.cn/interview","profileArticles":"/profile/articles","tryNewFeatures":"/new/","orders":"/order","explore":"/leetbook","resume":"/profile/info/","playground":"/playground","assessment":"/assessment/","account":"/profile/info"},"pagination":{"perpage":" 条/页"},"expand":"展开","collapse":"收起","difficulty":{"easy":"简单","medium":"中等","hard":"困难"},"data":{"question":{"difficulty":{"easy":"简单","medium":"中等","hard":"困难"}}},"markdown":{"heading":"heading","quote":"Quote"},"mentions":{"users":"用户","problems":"题目"},"confirmModal":{"title":"确定执行此操作?","confirmBtn":"确定","cancelBtn":"取消"},"saving":"保存中...","saved":"保存成功","autoSaved":"已自动保存","loginRequired":"您尚未登录","verifiedRequired":"请绑定手机号或者邮箱后继续操作","phoneVerifiedRequired":"请绑定手机号后继续操作","maybeVerifiedRequired":"请绑定手机号后继续操作","copy":"复制","copyToEditor":"复制到编辑器","copied":"已复制","copyLink":"复制链接","viewMore":"查看更多","viewLess":"收起","code":"代码","dailyCheckIn":"+1 每日登录","//maybeVerifiedRequired":"maybeVerifiedRequired means email in LCUS and phone in LCCN","easterEgg":{"rewardMessage":"恭喜您获得了 10 积分，Happy LeetCoding!"},"survey":{"veryDissatisfied":"非常不满意","verySatisfied":"非常满意","next":"下一题","continue":"继续","submit":"提交","questionNo":"问卷题目 {{current}}/{{total}}","thanksMsg":"🎉 感谢您的反馈!"},"qdNav":{"backTitle":"题库","expandPanel":"展开面板","preQuestion":"上一题","nextQuestion":"下一题","pickOne":"随机一题","openInNewTab":"在新的标签页打开"},"premiumModal":{"learnMore":"了解更多权益","subscribe":"升级 Plus 会员"},"truncatedContent":{"viewAll":"查看全部","viewLess":"收起","openRaw":"打开源码","showMore":"显示更多","showLess":"显示更少"},"safariNotUse":"当前 Safari 版本过低，为了更好的使用体验，请升级到最新版本","medal":{"metadataTitle":"勋章 - 力扣（LeetCode）","congratulation":"恭喜获得","genPoster":"生成海报","genPostering":"生成中...","saveImgMobile":"长按图片保存","saveImgPc":"右键保存图片","medalEmpty":"暂无可领取的勋章"}},"problems":{"meta":{"title":"{{title}} - 力扣（LeetCode）","description":"{{title}} - {{content}}","ogImage":"https://static.leetcode-cn.com/cn-legacy-assets/images/LeetCode_Sharing.png","defaultDescription":"备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。"},"tabs":{"description":"题目描述","editorial":"官方题解","discussion":"评论","solutions":"题解","submissions":"提交记录","submissionOverview":"提交记录概述","code":"代码","testcase":"测试用例","result":"测试结果","debugger":"调试器","settings":"设置","note":"笔记","guide":"指引","preview":"预览","previewConsole":"Web 控制台","rawText":"原始文本","resultDiff":"差异","disabledTooltips":{"editorial":"Editorial is not available for this question."}},"feedback":{"feedback":"反馈","revertToOld":"回退到上一个版本"},"lockedQuestion":{"subscribe":"升级 Plus 会员","subscribeToUnlockMessage":"感谢使用力扣！您需要升级为 Plus 会员来解锁该题目","subscribeToUnlock":"该题目是 Plus 会员专享题"},"unsupportedFeature":{"upgradeToIdeTitle":"升级至动态布局","signInToTryOut":"登录以体验","tryOut":"立即体验","features":{"frontendQuestion":"新的前端问题仅在动态布局中支持。切换到此格式以获得更加沉浸的LeetCode体验并访问这些问题。"}},"satisfactionSurvey":{"submitBtnText":"提交"},"panel":{"recommend":"为你推荐","description":"为你精选近期热门题目"},"dynamicLayout":{"maximize":"放大","exit":"退出放大","foldPanel":"折叠","unFoldPanel":"展开","moveTabset":"{{name}} 等 {{count}} 个 tab","disabledUnFold":"当前布局结构不支持一键展开，请手动拖拽","layoutManager":{"hints":"帮助","layouts":"布局","featureTitle":"布局过于凌乱？","featureContent":"一键重置布局现已支持！你甚至可以自定义布局模版，随时应用。","gotIt":"我知道了","tryNow":"立即体验","featureInfo":"创建或管理你的布局，获得更佳学习体验。","default":"预设","note":"笔记","debug":"调试","saveCurrentLayout":"保存当前布局","saveNewLayout":"保存新布局","nameYourLayout":"命名当前布局","temporaryTabs":"临时标签页","temporaryTabsWarningBefore":"保存布局时，将不包含 ","temporaryTabsWarningAfter":"","temporaryTabsContent":"临时标签页仅在特定题目下可见，例如题解详情和提交结果详情。","cancel":"取消","save":"保存","layoutSaved":"已保存布局","layoutDeleted":"布局已删除","upgradeToSaveFirst":"Plus 会员解锁","upgradeToSaveSecond":"自定义布局","subscribe":"升级","apply":"应用","upgradeToApply":"Plus 会员解锁此布局","delete":"删除","deleteTitle":"删除 “{{name}}”？","deleteContent":"此布局将被永久删除且不可恢复。","no":"取消","edit":"编辑","editLayout":"编辑布局","updateToCurrentLayout":"更新至当前布局"},"featureModal":{"dynamicLayout":"灵动布局","title":"升级「灵动布局」","content":"屏幕空间由你灵活掌控，聚焦真正重要的内容，畅享更沉浸的编码体验。","tryOut":"立即体验"},"settingRunSubmitPopover":{"title":"自由配置工具栏？","content":"现在你可以将运行 / 提交 / 调试按钮移至代码编辑器。","buttonText":"前往设置"}},"settings":{"settings":"设置","lab":"实验室","premium":"Plus","layout":{"categoryTitle":"灵动布局","resetToDefaultLayout":"重置为默认布局","reset":"重置","runSubmitPosition":"运行 / 提交 / 调试按钮位置","toolbar":"顶部工具栏","code-editor":"代码编辑器","revertToSplitViewMode":"返回双栏布局"},"editor":{"categoryTitle":"代码编辑器","fontSize":"字体大小","keyBinding":"键位绑定","keyBindingVim":"Vim","keyBindingEmacs":"Emacs","keyBindingStandard":"Standard","tabSize":"Tab 长度","spaces":"{{count}} 个空格","wordWrap":"自动换行","relativeLineNumber":"显示相对行号"},"shortcuts":{"categoryTitle":"键盘快捷键","or":"或","general":"常规","runCode":"执行代码","submit":"提交解答","closeTab":"关闭 tab","maximizePanel":"放大 / 退出放大面板","fullScreen":"进入 / 退出全屏","debug":"调试","debugStart":"开始调试","debugStop":"停止调试","debugSkipForward":"继续","debugStepOver":"单步跳过","debugStepIn":"单步调试","debugStepOut":"单步跳出","debugRestart":"重启","codeEditor":"代码编辑器","editorIndent":"行缩进","editorIndentFew":"行减少缩进","editorMoveLines":"上下移动行","editorCut":"剪切","editorToggleComment":"切换行注释","editorUndo":"撤销","editorRedo":"重做"},"advanced":{"categoryTitle":"高级设置","premiumTitle":"LeetCode Plus","premiumDesc":"升级 plus 会员，即可在灵动布局中畅享定制化的学习体验。","learnMore":"了解详情","realTimeResizing":"布局实时变化","realTimeResizingDesc":"拖动调整窗口尺寸时，布局实时变化。","multipleTab":"以新标签页呈现多个内容组件","multipleTabDesc":"列表中的元素（如题解、提交记录等）可在新标签页中打开，并同时允许打开多个标签页。","openAfterActive":"在激活的 Panel 中打开","openAfterSimilar":"在同类标签最新位置后打开","customLayout":"保存自定义布局 (云端)","customLayoutDesc":"会员可额外存储 3 个自定义布局模版。","upgrade":"升级","view":"查看","multipleTabUpdateAlert":{"title":"更新设置?","desc":"更新此项配置，将自动关闭所有已打开的题解和提交记录。确认更新吗？","no":"取消","update":"更新"}}},"preview":{"goBackTooltip":"返回","goForwardTooltip":"前进","refreshTooltip":"刷新","openInNewTabTooltip":"在新标签页中打开","upgradeToGetUrl":"升级至高级会员以查看链接"},"previewConsole":{"isEmpty":"控制台为空","clearTooltip":"清空控制台","clearedAt":"控制台清空于 {{time}}"},"ideGuide":{"introIdeTitle":"灵动布局","new":"全新","introInfo":"沉浸式畅享自由编码体验，潜力无边","setTitle":"选择运行/提交按钮的位置","setTip":"你也可以在设置中随时修改按钮出现的位置","enableIde":"开启灵动布局","of":"/","skipTour":"跳过","back":"上一步","next":"下一步","done":"完成","toolbarTitle":"工具栏","toolbarContent":"包含运行代码、提交、笔记等主要工具。","tabsTitle":"标签页","tabsContent":"通过拖动标签页来，即可定制布局为您理想的样子。","resizeTitle":"调整面板大小","resizeContent":"拖拽分隔条从而实现面板的大小调整，以适应您的空间需求。","maximizeTitle":"最大化一个面板","maximizeContent":"双击面板顶部的标签栏即可最大化该面板并增强您对该页内容的专注度。","expandCollapseTitle":"展开 / 折叠","expandCollapseContent":"点击以展开或折叠面板，为重要内容腾出更多的空间。","settingsTitle":"设置","settingsContent":"自定义灵活布局、代码编辑器、快捷键和高级设置。","maybeLater":"稍后再说"},"contest":{"toolbar":{"userAccepted":"通过的用户数","userAcceptedShort":"通过的用户数","userTried":"尝试过的用户数","userTriedShort":"尝试过的用户数","totalAccepted":"用户总通过次数","totalAcceptedShort":"用户总通过次数","totalSubmissions":"用户总提交次数","totalSubmissionsShort":"用户总提交次数"},"navbar":{"classicMode":"经典模式"}},"collaboration":{"invite":"邀请","liveCollaboration":"代码协同","beta":"Beta","invitePopoverDescBefore":"邀请协同者加入本题一起编程吧！协同最多可持续 3 小时。","invitePopoverDescAfter":"邀请协同者加入本题一起编程吧！协同最多可持续 3 小时。","createLink":"创建链接","copyTip":"复制链接并分享","copied":"已复制链接","endCollaboration":"结束协同","leaveCollaboration":"退出协同","user":"用户","clickToFollow":"点击跟随用户","clickToUnfollow":"点击结束跟随用户","failedToJoin":"暂时无法加入","failedSignIn":"登录后即可加入协同。","failedPremium":"升级为 Plus 会员后，即可加入协同。","failedMaximum":"当前协同已超过 5 人，请稍后再尝试加入。","failedDynamicLayout":"开启灵动布局后，即可加入协同。","failedNotFound":"链接不存在或已失效，请联系协同发起者并确认。","failedJoinedOtherRoom":"一次只能加入一个协同。","failedConnectionFailed":"连接失败。请检查您的网络连接并重试。","generalFailedTitle":"协同已终止","failedEnd":"发起者已结束协同","failedSameUser":"发起者重复进入协同，断开连接","failedHostLost":"发起者断开连接，协同结束","failedMaxTime":"已超过协同时长，协同结束","signIn":"登录","leave":"离开","subscribe":"升级","tryAgain":"重试","gotIt":"我知道了","maybeLater":"以后再说","enableDynamicLayout":"开启灵动布局","endCollaborationWarning":"确定结束协同吗？结束后，成员将无法继续进行代码协同。","leaveCollaborationWarning":"确定退出协同吗？退出后，你将无法继续进行代码协同。","cancel":"取消","end":"结束","switchProblem":"切换题目","switchProblemWarning":"确定切换题目吗？切换后，所有参与者都将同步更新。","switchLanguage":"切换语言","switchLanguageWarning":"确定切换语言吗？切换后，所有参与者都将同步更新。","leavingQd":"离开当前页面","leavingQdWarning":"本题正在协作中，确定离开吗？","confirm":"确定","switch":"切换","readOnlyOnTip":"设置为只读模式","readOnlyOffTip":"设置为编辑模式","toast":{"joining":"加入协同中...","joinedHost":"协同已开启","joinedGuest":"已加入协同","anotherParticipant":"另一位参与者","userJoined":"{{user}} 已加入协同","userLeft":"{{user}} 已退出协同","end":"发起者已结束协同","leave":"已退出协同","sameUser":"发起者重复进入协同，断开连接","hostLost":"发起者断开连接，协同结束","maxTime":"已超协同时长，协同结束","switchProblem":"{{user}} 已切换题目","switchLanguage":"{{user}} 已切换语言","runCode":"{{user}} 已执行代码。结果：{{result}}","submit":"{{user}} 已提交代码。结果：{{result}}","readOnlyOn":"协同房主已将你设置为只读模式","readOnlyOff":"协同房主已将你设置为编辑模式","readOnlyEdit":"只读模式下无法编辑代码","readOnlySwitch":"只读模式下无法切换题目或语言","logoutDisconnect":"当前未登录，请登录后重新加入协同。"},"online":"人在线","visitorTip":"正在本题学习的扣友"}},"console":{"meta":{"title":"题目详情"},"console":"控制台","run":"运行","submit":"提交","resetTestcases":"重置测试用例","debug":"调试","testcase":"测试用例","debugger":"调试器","testcaseNumber":"Case {{ number }}","cloneCurrentTestcase":"克隆当前用例","testcaseCount":"{{ count }}/{{ max }} 个测试用例","switchToRawEditor":"使用文本编辑器编写用例","switchToTabEditor":"使用标签效果编辑器编写用例","switchToRawResultEditor":"使用文本编辑器查看运行结果","switchToTabResultEditor":"使用标签效果编辑器查看运行结果","switchConsoleToLeft":"控制台置于左侧","switchConsoleToRight":"控制台置于右侧","testcasePlaceholder":"请输入测试用例","shellTestcaseBlocker":"Shell 题目无需设置测试用例","sourceMode":"Source Mode","sourceModeText":"你可以在文本编辑器里编写测试用例了","line":"Line","case":"Case","noThanks":"知道了","tryNow":"立即使用","inconsistentResults":"执行跟提交结果不一致?","inconsistentResultsContent":"您的程序可能使用了全局变量或者自定义的类内变量，需要您避免申明类内静态变量以及全局变量，或者手动初始化。","gotIt":"明白了","readMore":"阅读更多","result":{"result":"执行结果","stdout":"标准输出","noResult":"请先执行代码","notAvailable":"竞赛中暂不可见","slowdown":{"premium":"你的提交过于频繁，请稍候重试","first":"你的提交过于频繁，请稍候重试，或","second":"升级 Plus 会员","third":"，可减少等待时间"},"networkError":"网络错误，请稍后刷新页面重试","serverError":"未知的服务器错误，请联系我们的团队进行技术支持。","unknownError":"未知错误","compileError":"编译出错","runtimeError":"执行出错","copyCompileError":"复制错误信息","copied":"已复制","viewAll":"查看全部","viewLess":"收起","outputLimitExceeded":"超出输出限制","timeLimitExceeded":"超出时间限制","memoryLimitExceeded":"超出内存限制","timeout":"请求超时","internalError":"内部错误","accepted":"通过","finished":"完成","wrongAnswer":"解答错误","invalidTestcase":"测试用例非有效值","runtime":"执行用时","input":"输入","output":"输出","expected":"预期结果","contribution":"贡献测试用例","pending":"运行中...","premiumPending":"极速判题中...","judging":"判题中...","debugging":"调试中...","speedUp":"开启极速判题","lastExecutedInput":"最后执行的输入","openTestcase":"查看测试用例","testcasesPassed":"个通过的测试用例","testPassedButTookTooLong":"测试用例通过了，但耗时太长。","useTestcaseAsInput":"添加到测试用例","addedTestcaseMessage":"成功添加测试用例","testcaseExistsMessage":"测试用例已存在","cantUseTestcaseAsInput":"测试用例数达到最大限制","maxTestcaseCountReached":"测试用例数达到上限 {{ count }} 个","debugger":"调试器","copyContent":"已复制到剪切板","moreLine_one":"更多","moreLine_other":"更多","edit":"编辑","errorTestcaseMsg1":"你发现了系统无法通过的测试用例，现在就去","errorTestcaseActionMsg":"提交","errorTestcaseMsg2":"此用例，帮助我们改进~"},"ai":{"title":"LeetWiz","beta":"Beta","analyzingCode":"分析代码...","codeErrorHint":"为什么我会遇到这个 错误？","fullName":"LeetWiz - 一款AI助手","shortName":"LeetWiz","description":"忘记加分号了吗? LeetWiz 帮助你专注于重要的事情，让你不断进步. 它会帮助你找出运行代码/编译错误的原因，并提供解决方法.","fixedError":"您似乎已经修复了运行时/编译错误。请记住，我目前只支持帮助解决运行代码错误或编译错误 😊","morePremiumFeatures":"更多高級功能"},"info":{"info":"注意","content":"\u003c0\u003e执行代码与提交代码的结果不同？如果您在C/C++的代码中使用了全局变量，请看\u003c/0\u003e \u003c1\u003e这里\u003c/1\u003e","ok":"确定"},"execute":"Execute","to":"to","fullTreeTooBig":"数据太大，无法展示","or":"or","showFullTree":"点击查看完整的二叉树","visualizer":{"dataTooLarge":"数据量过大，只展示部分","parseFailed":"生成错误，请检查格式是否正确","dataNotSupported":"不支持可视化","outputDataTypeNotSupported":"输出类型不支持可视化","initFailed":"画布初始化失败，请刷新页面重试"},"verifyEmail":"请绑定邮箱后继续操作","signToRunOrSubmit":"{{action}}需要登录","signToRunAndSubmit":"运行和提交代码需要\u003c0\u003e登录\u003c/0\u003e","verifyToRunAndSubmit":"您的手机号尚未绑定，\u003c0\u003e前往验证\u003c/0\u003e！ ","notAvailableDuringDebugging":"调试状态不可用","notAvailableDuringExecuting":"代码执行中不可用","nonVerifyMsg":"请绑定手机号后继续操作","frontendTestcases":{"reset":"重置","lnCol":"行 {{lineNumber}}，列 {{column}}","guideTooltip":"测试用例指南","guideTitle":"测试用例指南"},"createTestCaseTip":"如何创建测试用例?"},"code-editor":{"commonConfirmTitle":"操作确认","fullScreen":"全屏","exitFullScreen":"退出全屏","autocomplete":{"button":"智能模式","lspTooltip":"智能补全/语法检查","basicTooltip":"基础代码补全。","basicWithLspError":"基础代码补全。双击重试智能代码补全。","lspConnectionError":"连接失败","lspNotSupportedTooltip":"该语言暂不支持智能补全 / 语法检查","needToLoginTooltip":"登录来使用自动补全","notPremiumTooltip":"升级 Plus 会员使用自动补全"},"langInfo":"了解语言环境","settings":{"name":"代码编辑器设置","fontSize":"字体设置","fontSizeDesc":"调整适合你的字体大小。","theme":"主题设置","themeDesc":"切换不同的代码编辑器主题，选择适合你的语法高亮。","themeDark":"Dark","themeLight":"Light","themeSystem":"System","keyBinding":"键位绑定","keyBindingDesc":"想要练习使用 Vim 或者 Emacs？你可以在这里切换这些预设的键位绑定。","keyBindingVim":"Vim","keyBindingEmacs":"Emacs","keyBindingStandard":"Standard","tabSize":"Tab 长度","tabSizeDesc":"选择你想要的 Tab 长度，默认设置为4个空格。","spaces":"{{count}}","wordWrap":"自动换行"},"shortcuts":{"name":"编辑器快捷键","run":"执行代码","submit":"提交解答","debug":"调试","indent":"行缩进","indentFew":"行减少缩进","moveLines":"上下移动行","cut":"剪切","toggleComment":"切换行注释","undo":"撤销","redo":"重做","note":"笔记"},"reset":{"tip":"还原到默认的代码模版","confirmContent":"您将放弃所有更改并初始化代码！","resetServer":"您的代码已在 {{time}} 保存在云端,","restore":"恢复"},"history":{"title":"添加了备注的 {{lang}} 提交记录","tip":"获取备注过的提交记录","description":"仅展示当前语言下提交的代码；选中并确认后，当前代码编辑区的全部内容将会被替换。","status":"结果","runtime":"执行用时","memory":"消耗内存","time":"时间","topic":"标签","notes":"备注","noNotes":"暂无提交记录！"},"timer":{"start":"开始计时","hide":"隐藏","show":"展示","reset":"重置","pause":"暂停","continue":"继续计时","contest":{"penaltyTimeDescription":"每个错误提交增加 5 分钟罚时"}},"debugger":{"loginToDebug":"启用调试功能需要登录","name":"调试器","stdout":"标准输出","input":"输入","enterTip":"点击行号添加断点","exit":"退出调试","start":"开始调试","stop":"停止调试","startShort":"调试","stopShort":"停止","watch":"监听表达式","local":"本地变量","watchHolder":"请输入需要监听的变量，按回车确认","controlStart":"开始调试","controlForward":"继续","controlStepOver":"单步跳过","controlStepOut":"单步跳出","controlStepIn":"单步调试","controlReset":"重置","exited":"已经有一个调试会话在运行，是否将其终止？","startToWatch":"开启调试后查看表达式","watchTip":"开启调试才可添加表达式","startViewVars":"开启调试查看本地变量","noVars":"暂无变量","startViewOutput":"开启调试查看输出","noOutput":"暂无输出...","edited":"代码已变更，需要重启调试","cantAddTestcase":"您已達到最大測試用例數","langNotSupported":"{{lang}}暂不支持调试功能","expressionsNotSupported":"{{lang}} 不支持","notPremium":"升级 Plus 会员使用调试功能","oneClickDebug":"一键调试","cppAdditionalTip":"基于 GDB，请使用 *(\u0026nums[i]) 查看 nums[i] 的值"},"markDownPlaceholder":"请输入...(支持使用 Markdown)","retrieveCode":{"tip":"还原到最新提交的代码","confirmContent":"你确定要使用最近一次提交的代码来替换现有代码吗？","noData":"您尚未提交过任何代码！"},"editor-position":"行 {{lineNumber}}，列 {{column}}","framework":{"switchTooltip":"切换框架","modalTitle":"选择框架","modalDescription":"选择你想要的框架。","modalConfirmTitle":"确认切换框架","modalConfirmText":"切换框架将会重置未提交的代码。你确定要继续吗？","modalConfirmBtn":"继续","toastSwitchSuccess":"已更新 {{framework}} 的描述。","guide":{"selectFramework":"选择框架","selectFrameworkDescription":"你可以在这里切换至理想的框架","selectFrameworkConfirm":"知道了"}},"saveCode":{"restoredFromCloud":"已从云端恢复","restoredFromLocal":"已从本地恢复","upgradeToCloud":"升级云端代码存储","savedToCloudToast":"您是 Plus 会员，代码已自动存储至云端","savedToLocalToastFirst":"代码已存储至本地，","savedToLocalToastSecond":" 解锁云端存储","upgradeToPremium":"升级 Plus 会员","savedToCloud":"已存储","savedToLocal":"已存储","saving":"存储中..."},"format":{"tip":"代码格式化","formatted":"已格式化"},"exceedMaxLineLength":"因性能的缘故，每行的字符数量被限制为 10,000。"},"description":{"status":{"tried":"尝试过","ac":"已解答"},"somethingWentWrong":"网络错误","thanksForVoting":"感谢反馈！","topics":"相关标签","companies":"相关企业","pastSixMonths":"0 - 6 个月","pastYear":"6 个月 - 1 年","pastTwoYears":"1 年 - 2 年","lastThreeMonths":"过去 3 个月","lastSixMonths":"过去 6 个月","SixMonthsAgo":"6 个月前","hint":"提示","showHints":"显示提示","moreActions":"更多操作","feedback":"反馈","showEnglish":"切换为英文","showChinese":"切换为中文","feedbackForm":{"title":"反馈","alternative":"您也可以通过 \u003c0\u003eGitHub 快速反馈通道\u003c/0\u003e 进行提交","cancel":"取消","submit":"提交","issuesEncountered":"遇到问题","problem":"题目","somethingWentWrong":"网络错误","additionalFeedback":"额外的反馈","description":"我们将致力于提高题目质量，你不喜欢的理由是什么？","options":{"unclearDescription":"描述和示例不清楚或不正确","unclearDifficulty":"难度不准确","unclearTestCases":"测试用例缺失或不正确","runtimeStrict":"时间要求太严格","edgeCases":"边界情况太多","other":"其他","otherPlaceholder":"额外的反馈"},"optionRequiredError":"至少选择一个选项."},"accepted":"通过次数","submissions":"提交次数","acRate":"通过率","copyright":"© {{year}} 领扣网络（上海）有限公司","yes":"是","no":"否","add2":"添加","seenBefore":"面试中遇到过这道题?","whichCompany":"请问您应聘的哪家公司？","whichPosition":"请问您应聘的岗位类型？","whichTimePeriod":"您是在什么时候遇到该题的？","whichStage":"请问您进行了哪种形式的面试？","thanksForFeedback":"🎉 谢谢您的反馈！","relatedTopics":"相关标签","add":"加入","remove":"移除","createNewList":"创建题单","nameListPlaceholder":"输入标题","cancel":"取消","save":"保存","setAsPrivate":"设为私密","addToList":"加入收藏夹","sqlSchema":"SQL Schema","pandasSchema":"Pandas Schema","confirm":"确定","favoriteSignInError":"登录后才能收藏题目","changeLanguageError":"登录后才能切换语言","feedbackSignInError":"登录后才能反馈问题","likeSignInError":"登录后才能点赞","schemaCopySuccess":"已复制到剪贴板","shareQuestionDescription":"分享题目","viewMyLists":"查看我的收藏夹","searchPlaceholder":"搜索","ok":"OK","addToListError":"Something went wrong. Please try again.","similarQuestions":"相似题目","discussion":"评论 ({{commentCount}})","myLists":"我的题单","create":"创建","addProblemToListSuccess":"成功添加到","addedSuccess":"添加成功","removeProblemFromListSuccess":"已从 {{listItemName}} 中移除","viewAllLists":"查看全部","unGetListInfo":"无法获取题单信息","listUnExist":"题单不存在","companyListUnExist":"企业题库不存在","listContextNull":"无权限获取题单内容","listContextEmpty":"题单内容为空","companyListContextEmpty":"企业题库内容为空","points":"分"},"submissions":{"runtime":"时间","memory":"内存","beat":"击败","noData":"暂无数据","noSubmission":"暂无数据","copied":"已复制","submittedAt":"提交于","allSubmissions":"全部提交记录","fullCode":"全部代码","success":{"accept":"通过","timeTaken":"用时: {{time}}","nextQuestion":"下一题","moreChallenges":"更多挑战","second_short":"s","minute_short":"m","hour_one":"hr","hour_other":"hrs","solution":"写题解","beatsPercentage":"击败 {{percent}}%","ofUsersWithLanguage":"使用 {{language}} 的用户"},"details":{"myCode":"我提交的代码","otherCode":"他提交的代码","sampleCode":"{{metric}} 的代码示例","backToMyCode":"返回我的位置","chartHintForAction":"点击查看代码","fetchingCodeFromServer":"加载中..."},"buttons":{"close":"关闭","details":"详情","solution":"写题解"},"filters":{"allStatuses":"所有状态","allLanguages":"所有语言","time":"时间","status":"所有状态","language":"所有语言","framework":"所有框架","runtime":"执行用时","memory":"消耗内存","notes":"备注","penaltyTime":"惩罚时间","minute":"分钟"},"notes":{"label":"备注","placeholder":"添加备注，例如「暴力解法」、「方法一」等"},"relatedTags":{"label":"相关标签","placeholder":"选择相关标签","startTyping":"搜索标签","noResults":"暂无标签"},"chart":{"runtimeDescription":"执行用时 (%)","memoryDescription":"消耗内存 (%)","youAreHere":"你在这里","hintForAction":"点击图片查看分布详情","runtime":"执行用时分布","memory":"消耗内存分布","percentLabel":"{{percent}}% 的用户使用了类似解法","runtimeValueLabel":"Runtime: {{value}} ms","memoryValueLabel":"Memory: {{value}} MB","noData":"加载中，暂无数据","memoryShortDescription":"Distribution (%)","runtimeShortDescription":"Distribution (%)","codeSample":"代码示例","runtimeCodeSampleInfo":"执行用时：{{value}}ms","memoryCodeSampleInfo":"消耗内存：{{value}}mb","resetZoom":"点击缩略地图以重置","complexity":"复杂度","runtimeTip":"本指标计算函数运行时间（自 2024.10.19 生效，此日期前提交的代码运行时间不变，但会与新数据一同计算排名）"},"nonSignedIn":{"signInTitle":"🔥 登录力扣开始写代码","signInInfo":"这里会展示你的提交记录 ","signInButton":"登录/注册"},"noCode":"There is no code here","pending":"Pending...","testPassedButTookTooLong":"测试用例通过了，但耗时太长。","failedSubmission":{"runtimeError":"执行出错信息","compileError":"编译出错信息","lastTestcase":"最后执行的输入"},"submissionPreview":{"embedCode":"嵌入代码","copiedEmbedCode":"已复制","copyEmbedCode":"复制","copyEmbedCodeTooltip":"复制嵌入代码","copyLinkTooltip":"复制链接","openInNewTabTooltip":"在新标签页打开","openInPanelTooltip":"在面板中打开","maximizeTooltip":"最大化","minimizeTooltip":"最小化","invalidSubmissionIdLabel":"无效的提交记录 ID","missingSubmissionIdTooltip":"请输入提交记录 ID","nonFeSubmissionIdTooltip":"请输入有效的提交记录 ID","openIn":"打开"},"complexity":{"timeComplexity":"时间复杂度","spaceComplexity":"空间复杂度","analyzeComplexity":"复杂度分析","accurate":"有帮助","notAccurate":"没有帮助","notAccurateTitle":"没有帮助","placeholder":"结果不准确，或其他功能反馈？","premiumLimit":"复杂度分析已达上限，请明天再试吧~","limitTitle":"升级 Plus 会员继续使用","limitContent":"今日复杂度分析已达次数上限，升级会员可继续使用，还能提高结果准确率！","learnMore":"了解更多权益","subscribe":"升级 Plus 会员","tryLater":"前方线路拥挤，请稍后再试。","noteEmpty":"请输入内容再提交哦"}},"feature-guide":{"layout":"支持上下、左右拖拽调整布局","timer":"\u003c0\u003e计时器：\u003c/0\u003e 现在可以在做题过程中使用计时器了！","debugger":"\u003c0\u003e调试器：\u003c/0\u003e 我们将 Debugger 移动到了这里","problemSwitch":"这里可以快速切换到 \u003c0\u003e上一题/下一题\u003c/0\u003e ","problemList":"这里可以快速返回\u003c0\u003e题目列表\u003c/0\u003e","discussion":"新的 \u003c0\u003e“讨论”，\u003c/0\u003e 您可以发布任何想法","solution":"将 \u003c0\u003e“评论”\u003c/0\u003e 的名字修改为新的 \u003c0\u003e“题解” 名\u003c/0\u003e","back":"返回","skip":"跳过","next":"下一步","ok":"确定","title":"🎉 我们的新界面"},"feature-guide-dynamic":{"back":"返回","skip":"跳过","next":"下一步","explore":"探索","step1":{"title":"全新灵动布局","des":"我们珍视每一种独特的思考与学习方式，并致力于提供个性化的支持。","tip":""},"step2":{"title":"自定义布局","des":"不满意默认布局？从此页面内容由你定义，让编码与学习事半功倍。","tip":"拖拽标签页或标签面板以定义布局"},"step3":{"title":"自定义尺寸","des":"屏幕空间受限？现在由你掌控如何利用空间，聚焦真正重要的内容。","tip":"拖拽标签面板间的空隙以改变尺寸"},"step4":{"title":"沉浸式全屏","des":"干扰信息过多？轻松双击即可隔绝干扰，遁入沉浸。","tip":"双击面板顶部进入全屏模式"},"step5":{"title":"全局工具栏","des":"承载聚合力扣核心功能，并将持续拓展，敬请期待。","tip":""}},"solutions":{"filter":{"searchPlaceholder":"搜索","tags":{"all":"不限","mySolution":"我的"},"sortBy":{"placeholder":"排序","hot":"热度最高","most_posts":"发布数量","most_relevant":"默认排序","most_votes":"点赞最多","newest_to_oldest":"最新发布","oldest_to_newest":"最早发布","recent_activity":"默认排序","recent_activity_short":"默认排序","hot_short":"热度最高","newest_to_oldest_short":"最新发布","oldest_to_newest_short":"最早发布","most_votes_short":"点赞最多","most_relevant_short":"默认排序"}},"solution":"题解","writeSolution":"写题解","continueSolution":"继续写题解","tags":{"official":"官方","pinned":"精选","favorite":"收藏","mySolution":"我的题解","hidden":"灰屏"},"post":{"invalidSolutionTitle":"题解不存在","invalidSolutionDescription":"请查看其他题解","prevLabel":"上一篇题解","nextLabel":"下一篇题解","isAdmin":"管理员","reputationTooltip":"声望","share":"分享","addToCollection":"收藏","isInCollection":"已收藏","votes":"({{votesCount}} votes)","shareCopySuccess":"分享链接复制到剪切板","addToFavoriteSuccess":"添加成功","removeFromFavoriteSuccess":"移除成功","feedbackTooltip":"反馈","backToTop":"回到顶部","genericError":"未知错误","upvote":"有用","comments":"评论","allSolutions":"全部题解","more":{"error":"网络错误","cancel":"取消","edit":"编辑","editorsPick":"设为精选","subscribe":"Subscribe","subscribeMessage":"Subscribed","unsubscribe":"Unsubscribe","unsubscribeMessage":"Unsubscribed","delete":"删除","deleteMessage":"删除成功","deleteConfirmText":"确定删除?","deleteConfirmBtn":"删除","remove":"下线","restore":"Restore","restoreMessage":"Restored","restoreConfirmText":"Are you sure you want to restore this post?","restoreConfirmBtn":"Restore","report":"举报","reportMessage":"举报成功","officialPick":"设为官方","pin":"Pin","pinMessage":"Pinned","pinConfirmText":"Are you sure you want to pin this post?","pinConfirmBtn":"Pin","uneditorsPick":"取消精选","undelete":"恢复删除","unmute":"取消屏蔽","unofficialPick":"取消官方","unpin":"Unpin","unpinMessage":"Unpinned","unpinConfirmText":"Are you sure you want to unpin this post?","unpinConfirmBtn":"Unpin","unsunk":"取消下沉","hide":"Hide","hideMessage":"Hid the post","hideConfirmText":"Are you sure you want to hide this post?","hideConfirmBtn":"Hide","hideFromTrending":"Hide from trending","hideFromTrendingMessage":"Hid post from trending","hideFromTrendingConfirmText":"Are you sure you want to hide this post from trending?","hideFromTrendingConfirmBtn":"Hide from trending","show":"Show","showMessage":"Showed the post","showConfirmText":"Are you sure you want to show this post to everyone?","showConfirmBtn":"Show","sunk":"下沉","moveToDiscussion":"Move to Discussion","moveToDiscussionMessage":"Moved to Discussion","moveToDiscussionConfirmText":"Are you sure you want to move this post to Discussion?","moveToDiscussionConfirmBtn":"Move to Discussion","mute":"灰色屏蔽"},"rateSuccess":"Thanks for rating this solution!"},"searchResult":{"commentPrefix":" comment","replyPrefix":" reply to ","colon":": "},"noDirectResultsHint":"No result. Show you some related content","noResults":"暂无相关题解内容","noMoreResults":"已经到底了","backToTop":"回到顶部","report":{"reportModalTitle":"举报","contentPlaceholder":"其他","cancel":"取消","confirm":"确认","advertising":"骚扰广告","sexual":"黄色内容","violent":"暴力内容","terrorism":"恐怖言论","illegal":"违法内容","politics":"政治言论","abuse":"辱骂他人","fake":"造谣传谣","nonEnglish":"Non English content","other":"其他","reportSuccess":"提交成功","reportError":"提交遇到问题，请稍后再试！"},"blocker":{"subscribeToUnlock":"Subscribe to unlock.","subscribeSubTitle":"Thanks for using LeetCode! To view this solution you must subscribe to premium.","subscribe":"Subscribe"},"videoSolutionTooltip":"Video Solution","premiumOnlyTooltip":"Premium Solution","switchToRightTooltip":"移到右边","switchToLeftTooltip":"移到左边","switchFirstTimePopoverContent":"您可以通过点击 “切换视图” 的按钮将题解文章的视图进行左右切换","switchFirstTimePopoverBtn":"明白了","shareSolutionBanner":{"lastSubmissionBeats":"你最近一次提交运行时间超过了 \u003c0\u003e{{percentage}}\u003c/0\u003e 的用户","lastSubmissionBeatsSmall":"你最近一次提交运行时间超过了 \u003c0\u003e{{percentage}}\u003c/0\u003e 的用户","lastSubmissionMemoryBeats":"你最近一次提交运行内存超过了 \u003c0\u003e{{percentage}}\u003c/0\u003e 的用户","lastSubmissionMemoryBeatsSmall":"你最近一次提交运行内存超过了 \u003c0\u003e{{percentage}}\u003c/0\u003e 的用户","signInAndShareSolutions":"登录并分享题解","signIn":"登录","shareMySolution":"发布题解","share":"分享","getACSubmissionsToPublish":"你需要先通过这道题目才能发布题解"},"sideBySide":{"enterMode":"开启双栏模式","exitMode":"退出双栏模式","modeOn":"已开启双栏模式","modeOff":"已退出双栏模式","enterGuideTitle":"浏览多份内容?","enterGuideDesc":"试试开启双栏模式，你还可以进一步在设置中自定义你的浏览体验。","exitGuideTitle":"退出双栏模式","exitGuideDesc":"退出后，即可专注浏览唯一标签页。","goToSettings":"打开设置","gotIt":"我知道了"}},"comments":{"edited":"(编辑过)","tooShort":"评论过短","noComments":"暂无评论","reply":"回复","mentionInputPlaceholder":"用户或题目","user":"用户","problem":"题目","mdRules":{"inlineCode":"行内代码...","codeBlock":"code block","link":"leetcode","href":"https://leetcode.cn"},"pinnedBy":"被 {{pinnedBy}} 置顶","share":"分享","edit":"编辑","save":"保存","shareCopySuccess":"已复制到剪切板","hideReplies":"隐藏回复","showReplies":"展示 {{num}} 条回复","cancel":"取消","confirm":"确定","preview":"预览","comment":"评论","typeCommentHere":"请输入评论...","comments":"评论","sortBy":"排序","newestToOldest":"最新","oldestToNewest":"最早","mostVotes":"赞成数","best":"最热","editor":"编辑","youMust":"您需要先","verifyYourEmail":"绑定邮箱","first":"first","readMore":"展开全部","somethingWentWrong":"未知错误","areYouSure":"操作确认","confirmDeleteComment":"确定删除该条评论？","confirmRestoreComment":"确定恢复该条评论？","confirmHideComment":"确定将该条评论灰色屏蔽？","confirmShowComment":"确定将该条评论取消灰色屏蔽？","confirmPinComment":"确定置顶该评论？","confirmUnpinComment":"确定移除置顶？","reward":"赞赏","delete":"删除","hide":"隐藏","show":"展示","askQuestion":"问问题","feedback":"反馈","tips":"提示","chooseAType":"请选择一个类型","showMoreReplies":"展示更多","hideSuccess":"灰色屏蔽成功.","showSuccess":"取消灰色屏蔽成功.","pinSuccess":"Comment has been pinned.","unpinSuccess":"Comment has been unpinned.","deleteSuccess":"删除成功","restore":"Restore","restoreSuccess":"成功恢复评论","hidden":"Hidden","report":"举报","pin":"设为精选","pinned":"精选","unpin":"取消精选","hideComment":"灰色屏蔽","showComment":"取消灰色屏蔽","move":"Move to Solution","moveTitle":"Title:","moveTitlePlaceholder":"Enter title here","moveSuccess":"Comment Successfully Moved","postSuccess":"发布成功","genericError":"Something went wrong","signInVoteError":"You must sign in to vote","verifyVoteError":"You must verify your email to vote"},"post-solution":{"meta":{"newTitle":"{{title}} - LeetCode - New Solution","editTitle":"{{title}} - LeetCode - Edit Solution"},"filterTopic":"搜索标签","publishSolution":"写题解","publishSolutionTooltip":"您需要先通过这道题目才能发布题解","restore":"是否清空草稿？","discard":"清空","discardConfirmTitle":"您确定要清空草稿吗？","discardConfirmContent":"如果清空草稿，会删除当前编辑器中的所有内容","discardConfirmOk":"确定","discardConfirmCancel":"取消","guide":"力扣「Markdown 编辑器」使用说明","check":"查看","blockCode":"「代码块」","tag":"标签","related":"与题相关","selectATag":"请为该题解选择至少1个标签","post":"发布题解","publishError":"发布失败","imgUploadSuccuss":"上传成功","imgUploadError":"上传失败，请重试","guideTooltip":"Markdown 指引","saved":"已保存为草稿"},"new-study-plan":{"detail":{"metadata":{"title":"{{plan}} - 学习计划 - 力扣（LeetCode）全球极客挚爱的技术成长平台","description":"学习计划 - 力扣（LeetCode）全球极客挚爱的技术成长平台","notFound":"未找到学习计划"},"weekTextAbbr":{"sun":"周日","mon":"周一","tue":"周二","wed":"周三","thu":"周四","fri":"周五","sat":"周六"},"weekText":{"sun":"周日","mon":"周一","tue":"周二","wed":"周三","thu":"周四","fri":"周五","sat":"周六"},"myPlan":"我的计划","problemLeft":"题待完成","problemsLeft":"题待完成","notification":"注意","setUpSp":"设置学习计划","solvedText":"完成","problem":"题","problems":"题","learnMore":"更多信息","you":"你","weeklyRanking":"周榜","weeklyRankingToolTip":"按本周完成题目数计算排名，每小时更新一次榜单数据（若本周未完成任何计划内题目，不计算排名）","solvePrev":"以下时间每天完成","solveNext":"道题","startTitle":"设置学习计划","confirmStartText":"计划保存后不可修改哦，确定保存吗？","quitTypeTipPrev":"请输入本计划标题：","quitTypeTipNext":" ","subscribeToUnlock":"升级 Plus 会员","subscribeToUnlockContent":"升级到 Plus 会员，可解锁该学习计划","start":"开始","share":"分享","backToExplore":"返回学习计划","goCurrentPage":"重新尝试该计划","premiumTip":"开通会员","copyLink":"复制链接","copiedSuccess":"已复制分享链接","more":"更多","quit":"退出","back":"返回","quitTitle":"关闭学习计划","quitContent":"当关闭此学习计划时，所有已解决问题的都会被重置，且无法恢复进度。你确定你要关闭吗？","showTags":"显示标签","summary":"概述","showMore":"展开","showLess":"收起","award":"勋章","awardCongratulation":"太棒啦！你已经获得此勋章","related":"相关计划","viewMore":"查看更多","todo":"待完成","attempted":"尝试过","solved":"已解答","markAsSolved":"标记为已解决","markAsSolvedTip":"你以前曾解决过这道题目，是否将其 '标记为已解决' ？","difficulty":"难度","congratulation":"🎉 恭喜你！","solvedAllProblemsText":"你已经解决了 {{title}} 中的所有问题！","checkBadge":"前往您的","profilePage":"个人主页","wearGlory":"并佩戴勋章！","checkMyStudyPlan":"回到我的学习计划","joinSuccessfully":"已加入","quitSuccessfully":"已退出","setSuccessfully":"已设置","errorTip":"遇到些问题，请再次尝试","quitTip":"若您退出该学习计划，所有已解决的问题都将被重置，且无法恢复。","pastSolved":"解答过","solution":"题解","points":"分","ranking":"排名"},"list":{"metadata":{"title":"学习计划 - 在 LeetCode 上持续练习来获得面试的成功"},"title":"学习计划","ongoing":"进行中","myPlan":"我的学习计划","featured":"精选","showMore":"展开","revertOldPlan":"查看旧版的学习计划","revertOldPlanTipTitle":"🌟 返回到旧版的学习计划","revertOldPlanTipDesc":"你可以点击该按钮前往旧版的学习计划","cancel":"取消","iSee":"知道了"},"myStudyPlan":{"metadata":{"title":"我的学习计划 - 力扣 (LeetCode) 全球极客挚爱的技术成长平台","desc":"加入到该学习计划可以追踪你的做题进度，有效地获得能力的提升！"},"title":"我的学习计划","ongoing":"进行中","history":"已结束的计划","noOngoingPlan":"暂无进行中的计划","noHistoryPlan":"暂无已结束的计划"},"common":{"studyPlan":"学习计划","tryNow":"立即开启","noTanks":"暂不尝试","newPlan":"✨ 全新的学习计划！","newPlanDesc":"加入一个新的学习计划，最大限度地发挥你的学习潜力。追踪你的进展，专注于每天的问题，以取得持续增长","seeAll":"查看更多","totalProgress":"完成进度","totalScore":"得分","progress":"完成进度","completed":"完成时间","giveUp":"退出时间","ongoing":"进行中","ongoingStudyPlan":"进行中的学习计划","later":"暂不参与","joinInQDTitle":"是否开始该学习计划？","joinInQD":"加入到该学习计划可以追踪你的做题进度，有效地获得能力的提升！","doNotRemind":"今天不再提示","exploreButton":"探索学习计划","notFoundText":"抱歉，无法找到该网页，请检查你的输入内容或重新探索一个新的学习计划"},"survey":{"submit":"提交"},"satisfactionSurvey":{"submitBtnText":"提交"}},"problemlist":{"metadata":{"defaultTitle":"题单 - 力扣（LeetCode）全球极客挚爱的技术成长平台","title":"{{title}} - 力扣（LeetCode）全球极客挚爱的技术成长平台"},"tags":"Tags","todo":"待完成","attempted":"尝试过","solved":"已解答","move":"拖动排序","removeFromList":"移除","addToList":"添加至题单","moveToTop":"置顶","moveToBottom":"置底","nullList":"Oops, 该题单不存在！","privateList":"该题单已设为私密","noQuestions":"暂无题目","goToProblemSet":"前往题库","difficulty":{"easy":"简单","medium":"中等","hard":"困难"},"nav-panel":{"title":"我的题单","fold":"折叠","unfold":"展开","createdByMe":"我创建的","savedByMe":"我收藏的","public":"公开","private":"私密","remove":"取消收藏","listInvalid":"题单已失效"},"description":{"cover":{"editCover":"修改封面","emojis":"表情符号","image":"自定义","random":"随机一图","background":"背景色","chooseBackground":"请选择背景色","Recommend":"推荐","Smileys \u0026 Emotion":"表情","People \u0026 Body":"角色","Animals \u0026 Nature":"动物与自然","Food \u0026 Drink":"食物与饮品","Activities":"活动","Travel \u0026 Places":"旅行与景点","Objects":"物品","Symbols":"符号","Flags":"旗帜","uploadImage":"上传图片","uploadRecommendedSize":"建议尺寸为 200 x 200 像素","uploadSizeLimit":"每个文件的最大尺寸为 5 MB","cancel":"取消","save":"保存"},"operations":{"questions":"题","public":"公开","private":"私密","publicToast":"题单已公开","privateToast":"已设为私密","practice":"开始练习","random":"随机一题","listSave":"收藏","listSaved":"已收藏","listSavedToast":"已收藏","listUnsavedToast":"已取消收藏","share":"分享","fork":"Fork","forkToast":"题单已 Fork!","more":"更多","delete":"删除","deleteList":"删除题单","deleteAlert":"您确定要删除此题单吗？本操作无法撤销。","cancel":"取消","acceptDelete":"确定","deleteToast":"题单已删除","edit":"编辑","editListInfo":"编辑题单信息","title":"标题","description":"描述","descriptionPlaceholder":"请简述本题单内容主题，例如：收集有趣的动态规划题","save":"保存","infoSavedToast":"保存成功！","clickToReadMore":"点击查看全文","nonLoggedInDialog":{"saveTitle":"收藏题单","saveContent":"登录后即可收藏题单","forkTitle":"Fork 题单","forkContent":"登录后即可 fork 题单","notNow":"以后再说","logIn":"登录"}},"progress":{"progress":"进度","resetProgress":"重置进度","resetAlert":"重置后，本题单进度将被清除（不影响题库或其他题单）。确定重置吗？此操作不可撤销。","cancel":"取消","reset":"确定","resetToast":"进度已重置","easy":"简单","medium":"中等","hard":"困难","solved":"已解答","acceptance":"通过率","beats":"击败比例","attempting":"尝试过","checkReset":"同时清除代码编辑器草稿"}},"company":{"nullList":"Oops, 该企业不存在！","subscribeText1":"升级至 Plus 会员","subscribeText2":"解锁更多企业高频面试题。","subscribe":"升级 Plus 会员","learnMore":"查看权益","freeQuestion":"免费高频面试题","claim":"领取","claiming":"领取中…","saved":"人收藏","updated":"更新时间: ","description":"简介","filter":"筛选","status":"状态","todo":"未开始","attempted":"尝试过","solved":"已解答","difficulty":"难度","easy":"简单","medium":"中等","hard":"困难","role":"岗位","rolePlaceholder":"请选择","reset":"清空筛选","tags":"标签","showTags":"显示标签","frequency":"出题频率","discuss":"讨论","chanceUsedUp":"免费机会已用完，升级 Plus 会员获取更多高频面试题。","subscribeNow":"升级会员","claimSignIn":"登录后领取 1 道面试题。","signIn":"登录","clickToReadMore":"点击查看详情","interviewTime":"面试时间","interviewTimeTip":"题单进度与当前所选面试时间相关","frequencyTip":"按出题频率倒序排列","ok":"好的"},"points":"分"},"contest":{"meta":{"title":"Contest - LeetCode","description":"Level up your coding skills and quickly land a job. This is the best place to expand your knowledge and get prepared for your next interview.","keywords":"","ogImage":"https://leetcode.com/static/images/LeetCode_Sharing.png"},"featuredContests":"Featured Contests","sponsorContest":"Sponsor a Contest","contest":"Contest","ranking":"Ranking","startsIn":"Starts in","endsIn":"Ends in","addToCalendar":"Add to Calendar","pastContests":"Past Contests","myContests":"My Contests","public":"Public","virtual":"Virtual","startVirtualContestDescription":"Start a Virtual Contest. Get well-prepared for a ranked match.","whatIsVirtualContest":"What's a Virtual Contest?","virtualContestModal":{"title":"Would you like to start a Virtual Contest?","ongoingTitle":"Would you like to start a new Virtual Contest?","confirmTitle":"Virtual Contest Started","goToContest":"Go to Contest","resumeOngoing":"Resume Ongoing","startNew":"Start New","confirmDescription":"Let‘s go to your Virtual Contest!","freshStartDescription":"Virtual Contests are a way to take part in previous contests. The experience is as close as it gets to real participation, but your rank is not affected.","ongoingDescription":"You already have an ongoing virtual contest. Do you want to drop the ongoing one and start a new one? If you choose so, your current process WILL NOT be saved.","start":"Start Virtual Contest","cancel":"Cancel"},"attended":"Attended","globalRanking":"Global Ranking","rating":"Rating","ratingTooltip":"Rating displayed is the net change from your previous rating followed by your new rating.","viewMore":"View More","virtualContest":"Virtual Contest","finishTime":"Finish Time","solved":"Solved","localTimeBased":"Date \u0026 time is based on the local timezone settings on your device","ratingPending":"Rating update is currently pending","finishTimeTooltip":"Acceptance time of your last solved problem plus penalty time","joinContests":"🏆 Join LeetCode Contests","viewContestInfo":"Register or sign in to view your personalized contest information","registerOrSignIn":"Register or Sign In","crownAlt":"Crown","noContests":"You haven't joined any contests yet.","randomVirtualContest":"Random Virtual Contest","ended":"Ended","rankingPage":{"meta":{"title":"{{title}} 排名 - 力扣（LeetCode）"},"problemList":"题目列表","ranking":"排名","rankingDetailPage":"排行榜详情","titlePrefix":"","titleSuffix":" 排名","akSuffix":" 人 AK！","akTip":"\"AK\" 即 \"All Killed\"，指本场竞赛题全部解出。","pending":"未开始","ended":"已结束","emptyRankingPlaceholder":"AK 等你来","rank":"排名","rankTipTitle":"竞赛过程中：","rankTip1":"排名信息可能无法实时更新，会有延迟","rankTip2":"仅展示 Top 200 用户","rankTipPending":"排名确认中","rankTipUpdated":"排名已确认","rankTipUnrated":"本场竞赛不计排名","name":"用户名","score":"得分","finishTime":"完成时间","finishTimeTip":"完成时间为通过时间和处罚时间的总和","questionPrefix":"题目","bugTipSuffix":" 次错误尝试","you":"我","code":"代码","reportCheating":"举报作弊","reportCheatingOtherRegion":"前往美服举报作弊","reportCheatingSubmitted":"已举报","reportCheatingPlaceholder":"你可以检举违规库、函数的使用，或者抄袭等其他作弊行为","submit":"提交","guideTitle":"查看代码","guideDescription":"点击此处可查看用户解答。","ok":"好的","tag":"标签","colon":"："}}}},"initialLocale":"en","ns":["common","problems","console","code-editor","description","submissions","feature-guide","feature-guide-dynamic","solutions","comments","post-solution","new-study-plan","problemlist","contest"],"userConfig":{"i18n":{"defaultLocale":"zh","locales":["en","zh"]},"react":{"useSuspense":false},"reloadOnPrerender":false,"default":{"i18n":{"defaultLocale":"zh","locales":["en","zh"]},"react":{"useSuspense":false},"reloadOnPrerender":false}}}},"__N_SSP":true},"page":"/problems/[slug]/[[...tab]]","query":{"slug":"running-sum-of-1d-array"},"buildId":"diRKLFNMGEC0z7HrVLWmm","isFallback":false,"gssp":true,"scriptLoader":[]}</script><div id="modal-root"></div><next-route-announcer><p aria-live="assertive" id="__next-route-announcer__" role="alert" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 1px; margin: -1px; overflow: hidden; padding: 0px; position: absolute; width: 1px; white-space: nowrap; overflow-wrap: normal;"></p></next-route-announcer><div id="headlessui-portal-root"><div data-headlessui-portal=""><div style="position: fixed; z-index: 40; top: 50px; left: 1284.36px;"></div></div><div data-headlessui-portal=""></div><div data-headlessui-portal=""></div><div data-headlessui-portal=""></div><div data-headlessui-portal=""></div><div data-headlessui-portal=""></div><div data-headlessui-portal=""></div><div data-headlessui-portal=""></div></div><iframe allow="join-ad-interest-group" data-tagging-id="G-CDRWKZTDEX" data-load-time="1731589789447" height="0" width="0" src="./Running Sum of 1d Array - LeetCode_files/rul.html" style="display: none; visibility: hidden;"></iframe><script src="./Running Sum of 1d Array - LeetCode_files/monaco-97aac266332974a36c55_0.34.7.js.download" crossorigin="anonymous"></script><div><div class="z-modal-2 bg-lc-layer-01 dark:bg-dark-lc-background-index fixed left-0 top-0 flex h-full w-[600px] -translate-x-full transform flex-col transition-all duration-500"><div class="relative border-b px-6 py-5 font-medium border-lc-fill-01 dark:border-dark-lc-fill-01"><div class="w-[500px]"><a href="https://leetcode.com/problemset/"><div class="cursor-pointer items-center flex"><div class="truncate flex items-center text-xl text-lc-text-primary dark:text-dark-lc-text-primary"><span class=" inline-block max-w-[360px] overflow-hidden text-ellipsis whitespace-nowrap" title="Problem List">Problem List</span></div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="ml-2 inline-block h-4 w-4 shrink-0 text-lc-icon-primary dark:text-dark-lc-icon-primary"><path fill-rule="evenodd" d="M7.913 19.071l7.057-7.078-7.057-7.064a1 1 0 011.414-1.414l7.764 7.77a1 1 0 010 1.415l-7.764 7.785a1 1 0 01-1.414-1.414z" clip-rule="evenodd"></path></svg><div class="flex flex-1 justify-end"><div data-state="closed"><div class="relative flex items-center justify-center h-4.5 w-4.5"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="absolute left-0 top-0 h-full w-full fill-transparent" style="stroke-width: 11;"><defs><lineargradient x1="1" y1="0" x2="0" y2="0" id="gradientProgressCircleInfo"><stop offset="0%" stop-color="#007AFF"></stop><stop offset="100%" stop-color="#73B6FF"></stop></lineargradient></defs><circle cx="50" cy="50" r="42" class="stroke-sd-primary/20"></circle><circle cx="50" cy="50" r="42" class="stroke-sd-success" style="stroke-linecap: round; stroke-dasharray: 1.76, 262.24; stroke-dashoffset: 66;"></circle></svg></div></div></div></div></a></div></div><div style="cursor: pointer; position: absolute; right: 26px; top: 22px;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="inline-block h-5 w-5 shrink-0 fill-none stroke-current text-lc-icon-secondary dark:text-dark-lc-icon-secondary"><path stroke-linecap="round" stroke-width="2" d="M19 5L5 19m14 0L5 5"></path></svg></div><div class="relative overflow-auto p-4"><div class="z-base-1 relative flex min-h-full flex-col"><div class="mb-4 flex items-center justify-end px-1"><button class="relative inline-flex items-center justify-center font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-sd-ring disabled:pointer-events-none disabled:opacity-50 border border-sd-input bg-transparent hover:bg-sd-accent hover:text-sd-accent-foreground h-7 text-xs rounded-full w-[76px] gap-2 px-3 py-1.5 text-sd-muted-foreground"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="eye-slash" class="svg-inline--fa fa-eye-slash absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path fill="currentColor" d="M38.8 5.1C28.4-3.1 13.3-1.2 5.1 9.2S-1.2 34.7 9.2 42.9l592 464c10.4 8.2 25.5 6.3 33.7-4.1s6.3-25.5-4.1-33.7L525.6 386.7c39.6-40.6 66.4-86.1 79.9-118.4c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C465.5 68.8 400.8 32 320 32c-68.2 0-125 26.3-169.3 60.8L38.8 5.1zm151 118.3C226 97.7 269.5 80 320 80c65.2 0 118.8 29.6 159.9 67.7C518.4 183.5 545 226 558.6 256c-12.6 28-36.6 66.8-70.9 100.9l-53.8-42.2c9.1-17.6 14.2-37.5 14.2-58.7c0-70.7-57.3-128-128-128c-32.2 0-61.7 11.9-84.2 31.5l-46.1-36.1zM394.9 284.2l-81.5-63.9c4.2-8.5 6.6-18.2 6.6-28.3c0-5.5-.7-10.9-2-16c.7 0 1.3 0 2 0c44.2 0 80 35.8 80 80c0 9.9-1.8 19.4-5.1 28.2zm9.4 130.3C378.8 425.4 350.7 432 320 432c-65.2 0-118.8-29.6-159.9-67.7C121.6 328.5 95 286 81.4 256c8.3-18.4 21.5-41.5 39.4-64.8L83.1 161.5C60.3 191.2 44 220.8 34.5 243.7c-3.3 7.9-3.3 16.7 0 24.6c14.9 35.7 46.2 87.7 93 131.1C174.5 443.2 239.2 480 320 480c47.8 0 89.9-12.9 126.2-32.5l-41.9-33zM192 256c0 70.7 57.3 128 128 128c13.3 0 26.1-2 38.2-5.8L302 334c-23.5-5.4-43.1-21.2-53.7-42.3l-56.1-44.2c-.2 2.8-.3 5.6-.3 8.5z"></path></svg></div>Tag</button></div><div><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1406" href="https://leetcode.com/problems/stone-game-iii" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1406. Stone Game III</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1407" href="https://leetcode.com/problems/top-travellers" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1407. Top Travellers</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1408" href="https://leetcode.com/problems/string-matching-in-an-array" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1408. String Matching in an Array</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1409" href="https://leetcode.com/problems/queries-on-a-permutation-with-key" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1409. Queries on a Permutation With Key</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1410" href="https://leetcode.com/problems/html-entity-parser" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1410. HTML Entity Parser</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1411" href="https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1411. Number of Ways to Paint N × 3 Grid</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1412" href="https://leetcode.com/problems/find-the-quiet-students-in-all-exams" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1412. Find the Quiet Students in All Exams</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1413" href="https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1413. Minimum Value to Get Positive Step by Step Sum</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1414" href="https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1415" href="https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1415. The k-th Lexicographical String of All Happy Strings of Length n</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1416" href="https://leetcode.com/problems/restore-the-array" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1416. Restore The Array</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1417" href="https://leetcode.com/problems/reformat-the-string" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1417. Reformat The String</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1418" href="https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1418. Display Table of Food Orders in a Restaurant</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1419" href="https://leetcode.com/problems/minimum-number-of-frogs-croaking" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1419. Minimum Number of Frogs Croaking</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1420" href="https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1420. Build Array Where You Can Find The Maximum Exactly K Comparisons</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1421" href="https://leetcode.com/problems/npv-queries" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1421. NPV Queries</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1422" href="https://leetcode.com/problems/maximum-score-after-splitting-a-string" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1422. Maximum Score After Splitting a String</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1423" href="https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1423. Maximum Points You Can Obtain from Cards</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1424" href="https://leetcode.com/problems/diagonal-traverse-ii" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1424. Diagonal Traverse II</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1425" href="https://leetcode.com/problems/constrained-subsequence-sum" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1425. Constrained Subsequence Sum</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1426" href="https://leetcode.com/problems/counting-elements" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1426. Counting Elements</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1427" href="https://leetcode.com/problems/perform-string-shifts" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1427. Perform String Shifts</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1428" href="https://leetcode.com/problems/leftmost-column-with-at-least-a-one" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1428. Leftmost Column with at Least a One</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1429" href="https://leetcode.com/problems/first-unique-number" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1429. First Unique Number</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1430" href="https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1430. Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1431" href="https://leetcode.com/problems/kids-with-the-greatest-number-of-candies" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1431. Kids With the Greatest Number of Candies</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1432" href="https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1432. Max Difference You Can Get From Changing an Integer</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1433" href="https://leetcode.com/problems/check-if-a-string-can-break-another-string" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1433. Check If a String Can Break Another String</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1434" href="https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1434. Number of Ways to Wear Different Hats to Each Other</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1435" href="https://leetcode.com/problems/create-a-session-bar-chart" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1435. Create a Session Bar Chart</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1436" href="https://leetcode.com/problems/destination-city" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1436. Destination City</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1437" href="https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1437. Check If All 1's Are at Least Length K Places Away</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1438" href="https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1439" href="https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1440" href="https://leetcode.com/problems/evaluate-boolean-expression" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1440. Evaluate Boolean Expression</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1441" href="https://leetcode.com/problems/build-an-array-with-stack-operations" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1441. Build an Array With Stack Operations</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1442" href="https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1442. Count Triplets That Can Form Two Arrays of Equal XOR</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1443" href="https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1443. Minimum Time to Collect All Apples in a Tree</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1444" href="https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1444. Number of Ways of Cutting a Pizza</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1445" href="https://leetcode.com/problems/apples-oranges" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1445. Apples &amp; Oranges</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1446" href="https://leetcode.com/problems/consecutive-characters" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1446. Consecutive Characters</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1447" href="https://leetcode.com/problems/simplified-fractions" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1447. Simplified Fractions</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1448" href="https://leetcode.com/problems/count-good-nodes-in-binary-tree" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1448. Count Good Nodes in Binary Tree</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1449" href="https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1449. Form Largest Integer With Digits That Add up to Target</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1450" href="https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1450. Number of Students Doing Homework at a Given Time</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1451" href="https://leetcode.com/problems/rearrange-words-in-a-sentence" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1451. Rearrange Words in a Sentence</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1452" href="https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1452. People Whose List of Favorite Companies Is Not a Subset of Another List</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1453" href="https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1453. Maximum Number of Darts Inside of a Circular Dartboard</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1454" href="https://leetcode.com/problems/active-users" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1454. Active Users</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1455" href="https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1456" href="https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1456. Maximum Number of Vowels in a Substring of Given Length</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1457" href="https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1457. Pseudo-Palindromic Paths in a Binary Tree</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1458" href="https://leetcode.com/problems/max-dot-product-of-two-subsequences" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1458. Max Dot Product of Two Subsequences</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1459" href="https://leetcode.com/problems/rectangles-area" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1459. Rectangles Area</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1460" href="https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1460. Make Two Arrays Equal by Reversing Subarrays</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1461" href="https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1461. Check If a String Contains All Binary Codes of Size K</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1462" href="https://leetcode.com/problems/course-schedule-iv" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1462. Course Schedule IV</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1463" href="https://leetcode.com/problems/cherry-pickup-ii" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1463. Cherry Pickup II</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1464" href="https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1464. Maximum Product of Two Elements in an Array</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1465" href="https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1466" href="https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1466. Reorder Routes to Make All Paths Lead to the City Zero</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1467" href="https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1467. Probability of a Two Boxes Having The Same Number of Distinct Balls</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1468" href="https://leetcode.com/problems/calculate-salaries" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1468. Calculate Salaries</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1469" href="https://leetcode.com/problems/find-all-the-lonely-nodes" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1469. Find All The Lonely Nodes</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1470" href="https://leetcode.com/problems/shuffle-the-array" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1470. Shuffle the Array</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1471" href="https://leetcode.com/problems/the-k-strongest-values-in-an-array" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1471. The k Strongest Values in an Array</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1472" href="https://leetcode.com/problems/design-browser-history" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1472. Design Browser History</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1473" href="https://leetcode.com/problems/paint-house-iii" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1473. Paint House III</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1474" href="https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1474. Delete N Nodes After M Nodes of a Linked List</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1475" href="https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1475. Final Prices With a Special Discount in a Shop</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1476" href="https://leetcode.com/problems/subrectangle-queries" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1476. Subrectangle Queries</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1477" href="https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1477. Find Two Non-overlapping Sub-arrays Each With Target Sum</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1478" href="https://leetcode.com/problems/allocate-mailboxes" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1478. Allocate Mailboxes</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1479" href="https://leetcode.com/problems/sales-by-day-of-the-week" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1479. Sales by Day of the Week</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary activeItem bg-sd-primary hover:!bg-sd-primary" id="1480" href="https://leetcode.com/problems/running-sum-of-1d-array" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="flex items-center" data-state="closed"><div class="relative text-[14px] leading-[normal] p-[1px] before:block before:h-3.5 before:w-3.5 text-sd-success"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="check" class="svg-inline--fa fa-check absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M441 103c9.4 9.4 9.4 24.6 0 33.9L177 401c-9.4 9.4-24.6 9.4-33.9 0L7 265c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0l119 119L407 103c9.4-9.4 24.6-9.4 33.9 0z"></path></svg></div></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body max-w-[75%] font-medium text-sd-primary-foreground"><div class="ellipsis line-clamp-1">1480. Running Sum of 1d Array</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1481" href="https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1481. Least Number of Unique Integers after K Removals</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1482" href="https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1482. Minimum Number of Days to Make m Bouquets</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1483" href="https://leetcode.com/problems/kth-ancestor-of-a-tree-node" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1483. Kth Ancestor of a Tree Node</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1484" href="https://leetcode.com/problems/group-sold-products-by-the-date" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1484. Group Sold Products By The Date</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1485" href="https://leetcode.com/problems/clone-binary-tree-with-random-pointer" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1485. Clone Binary Tree With Random Pointer</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1486" href="https://leetcode.com/problems/xor-operation-in-an-array" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1486. XOR Operation in an Array</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1487" href="https://leetcode.com/problems/making-file-names-unique" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1487. Making File Names Unique</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1488" href="https://leetcode.com/problems/avoid-flood-in-the-city" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1488. Avoid Flood in The City</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1489" href="https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1490" href="https://leetcode.com/problems/clone-n-ary-tree" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1490. Clone N-ary Tree</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1491" href="https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1491. Average Salary Excluding the Minimum and Maximum Salary</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1492" href="https://leetcode.com/problems/the-kth-factor-of-n" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1492. The kth Factor of n</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1493" href="https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1493. Longest Subarray of 1's After Deleting One Element</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1494" href="https://leetcode.com/problems/parallel-courses-ii" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1494. Parallel Courses II</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1495" href="https://leetcode.com/problems/friendly-movies-streamed-last-month" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1495. Friendly Movies Streamed Last Month</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1496" href="https://leetcode.com/problems/path-crossing" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1496. Path Crossing</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1497" href="https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1497. Check If Array Pairs Are Divisible by k</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1498" href="https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1498. Number of Subsequences That Satisfy the Given Sum Condition</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1499" href="https://leetcode.com/problems/max-value-of-equation" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1499. Max Value of Equation</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1500" href="https://leetcode.com/problems/design-a-file-sharing-system" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1500. Design a File Sharing System</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1501" href="https://leetcode.com/problems/countries-you-can-safely-invest-in" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1501. Countries You Can Safely Invest In</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1502" href="https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1502. Can Make Arithmetic Progression From Sequence</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1503" href="https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1503. Last Moment Before All Ants Fall Out of a Plank</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1504" href="https://leetcode.com/problems/count-submatrices-with-all-ones" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1504. Count Submatrices With All Ones</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1505" href="https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1506" href="https://leetcode.com/problems/find-root-of-n-ary-tree" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1506. Find Root of N-Ary Tree</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1507" href="https://leetcode.com/problems/reformat-date" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1507. Reformat Date</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1508" href="https://leetcode.com/problems/range-sum-of-sorted-subarray-sums" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1508. Range Sum of Sorted Subarray Sums</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1509" href="https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1509. Minimum Difference Between Largest and Smallest Value in Three Moves</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1510" href="https://leetcode.com/problems/stone-game-iv" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1510. Stone Game IV</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1511" href="https://leetcode.com/problems/customer-order-frequency" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1511. Customer Order Frequency</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1512" href="https://leetcode.com/problems/number-of-good-pairs" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1512. Number of Good Pairs</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1513" href="https://leetcode.com/problems/number-of-substrings-with-only-1s" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1513. Number of Substrings With Only 1s</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1514" href="https://leetcode.com/problems/path-with-maximum-probability" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1514. Path with Maximum Probability</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1515" href="https://leetcode.com/problems/best-position-for-a-service-centre" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1515. Best Position for a Service Centre</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1516" href="https://leetcode.com/problems/move-sub-tree-of-n-ary-tree" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1516. Move Sub-Tree of N-Ary Tree</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1517" href="https://leetcode.com/problems/find-users-with-valid-e-mails" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1517. Find Users With Valid E-Mails</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1518" href="https://leetcode.com/problems/water-bottles" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1518. Water Bottles</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1519" href="https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1519. Number of Nodes in the Sub-Tree With the Same Label</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1520" href="https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1520. Maximum Number of Non-Overlapping Substrings</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1521" href="https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1521. Find a Value of a Mysterious Function Closest to Target</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1522" href="https://leetcode.com/problems/diameter-of-n-ary-tree" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1522. Diameter of N-Ary Tree</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1523" href="https://leetcode.com/problems/count-odd-numbers-in-an-interval-range" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1523. Count Odd Numbers in an Interval Range</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1524" href="https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1524. Number of Sub-arrays With Odd Sum</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1525" href="https://leetcode.com/problems/number-of-good-ways-to-split-a-string" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1525. Number of Good Ways to Split a String</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1526" href="https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1526. Minimum Number of Increments on Subarrays to Form a Target Array</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1527" href="https://leetcode.com/problems/patients-with-a-condition" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1527. Patients With a Condition</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1528" href="https://leetcode.com/problems/shuffle-string" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1528. Shuffle String</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1529" href="https://leetcode.com/problems/minimum-suffix-flips" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1529. Minimum Suffix Flips</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1530" href="https://leetcode.com/problems/number-of-good-leaf-nodes-pairs" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1530. Number of Good Leaf Nodes Pairs</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1531" href="https://leetcode.com/problems/string-compression-ii" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1531. String Compression II</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1532" href="https://leetcode.com/problems/the-most-recent-three-orders" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1532. The Most Recent Three Orders</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1533" href="https://leetcode.com/problems/find-the-index-of-the-large-integer" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1533. Find the Index of the Large Integer</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1534" href="https://leetcode.com/problems/count-good-triplets" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1534. Count Good Triplets</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1535" href="https://leetcode.com/problems/find-the-winner-of-an-array-game" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1535. Find the Winner of an Array Game</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1536" href="https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1536. Minimum Swaps to Arrange a Binary Grid</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1537" href="https://leetcode.com/problems/get-the-maximum-score" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1537. Get the Maximum Score</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1538" href="https://leetcode.com/problems/guess-the-majority-in-a-hidden-array" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1538. Guess the Majority in a Hidden Array</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1539" href="https://leetcode.com/problems/kth-missing-positive-number" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1539. Kth Missing Positive Number</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1540" href="https://leetcode.com/problems/can-convert-string-in-k-moves" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1540. Can Convert String in K Moves</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1541" href="https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1541. Minimum Insertions to Balance a Parentheses String</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1542" href="https://leetcode.com/problems/find-longest-awesome-substring" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1542. Find Longest Awesome Substring</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1543" href="https://leetcode.com/problems/fix-product-name-format" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1543. Fix Product Name Format</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1544" href="https://leetcode.com/problems/make-the-string-great" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1544. Make The String Great</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1545" href="https://leetcode.com/problems/find-kth-bit-in-nth-binary-string" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1545. Find Kth Bit in Nth Binary String</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1546" href="https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1" data-state="closed">1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1547" href="https://leetcode.com/problems/minimum-cost-to-cut-a-stick" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1547. Minimum Cost to Cut a Stick</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1548" href="https://leetcode.com/problems/the-most-similar-path-in-a-graph" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1548. The Most Similar Path in a Graph</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1549" href="https://leetcode.com/problems/the-most-recent-orders-for-each-product" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1549. The Most Recent Orders for Each Product</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1550" href="https://leetcode.com/problems/three-consecutive-odds" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1550. Three Consecutive Odds</div></div></div><p class="text-[14px] text-sd-easy">Easy</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1551" href="https://leetcode.com/problems/minimum-operations-to-make-array-equal" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1551. Minimum Operations to Make Array Equal</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1552" href="https://leetcode.com/problems/magnetic-force-between-two-balls" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1552. Magnetic Force Between Two Balls</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1553" href="https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1553. Minimum Number of Days to Eat N Oranges</div></div></div><p class="text-[14px] text-sd-hard">Hard</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary bg-fill-quaternary dark:bg-fill-quaternary" id="1554" href="https://leetcode.com/problems/strings-differ-by-one-character" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1554. Strings Differ by One Character</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a><a class="group flex flex-col rounded-[8px] duration-300 hover:bg-fill-primary dark:hover:bg-fill-primary" id="1555" href="https://leetcode.com/problems/bank-account-summary" target="_self" rel="https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/"><div class="flex h-[44px] w-full items-center space-x-3 px-4"><div><div><div class="h-4 w-4"></div><div class="flex items-center" data-state="closed"></div></div></div><div class="relative flex h-full w-full cursor-pointer items-center"><div class=" flex w-0 flex-1 items-center space-x-2"><div class="text-body text-sd-foreground max-w-[75%] font-medium"><div class="ellipsis line-clamp-1">1555. Bank Account Summary</div></div></div><p class="text-[14px] text-sd-medium">Med.</p></div></div></a></div></div></div></div></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><script src="./Running Sum of 1d Array - LeetCode_files/2461-e958d665c2ab5afd.js.download"></script><script src="./Running Sum of 1d Array - LeetCode_files/6419-bf2b0e67c50692b3.js.download"></script><script src="./Running Sum of 1d Array - LeetCode_files/5891-983742785a4dde23.js.download"></script><script src="./Running Sum of 1d Array - LeetCode_files/719-46205b2a2c9cd287.js.download"></script><script src="./Running Sum of 1d Array - LeetCode_files/9521-fe99975ff5fe1038.js.download"></script><script src="./Running Sum of 1d Array - LeetCode_files/7107-beb8d57336790611.js.download"></script><script src="./Running Sum of 1d Array - LeetCode_files/1179-3a467ec6b88ae472.js.download"></script><script src="./Running Sum of 1d Array - LeetCode_files/8307-39cff2dd6db4307e.js.download"></script><script src="./Running Sum of 1d Array - LeetCode_files/4764-73021b0c137199cf.js.download"></script><script src="./Running Sum of 1d Array - LeetCode_files/2265-9cd1a8e9fb0f4124.js.download"></script><iframe allow="join-ad-interest-group" data-tagging-id="G-CDRWKZTDEX" data-load-time="1731589954874" height="0" width="0" src="./Running Sum of 1d Array - LeetCode_files/rul(1).html" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="G-CDRWKZTDEX" data-load-time="1731590167287" height="0" width="0" src="./Running Sum of 1d Array - LeetCode_files/rul(2).html" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="G-CDRWKZTDEX" data-load-time="1731590727661" height="0" width="0" src="./Running Sum of 1d Array - LeetCode_files/rul(3).html" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="G-CDRWKZTDEX" data-load-time="1731594556420" height="0" width="0" src="./Running Sum of 1d Array - LeetCode_files/rul(4).html" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="G-CDRWKZTDEX" data-load-time="1731594737301" height="0" width="0" src="./Running Sum of 1d Array - LeetCode_files/rul(5).html" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="G-CDRWKZTDEX" data-load-time="1731594859555" height="0" width="0" src="./Running Sum of 1d Array - LeetCode_files/rul(6).html" style="display: none; visibility: hidden;"></iframe><script src="./Running Sum of 1d Array - LeetCode_files/[[...slug]]-336526233f10d9dd.js.download"></script></body></html>