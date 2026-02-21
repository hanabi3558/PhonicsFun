# Project 07 - Phonics Fun! 進度追蹤

## 專案概述
兒童 Phonics（自然發音）互動學習網頁應用，單一 `index.html` 檔案（約 2000 行），包含 HTML + CSS + JavaScript，無外部框架依賴。

## 目前架構
- **index.html** - 主程式（所有邏輯、樣式、資料都在此檔）
- **6 張海報圖片** - Phase 1~6 的 Phonics 海報（webp/jpg/png）

## 功能模組

### 已完成的功能
1. **首頁 (Home Screen)**
   - 毛毛蟲吉祥物、標題、語音選擇器
   - 整體進度條與星星顯示
   - Phase 1~6 格狀選單

2. **Phase 詳情頁**
   - 每個 Phase 提供 4 種學習模式入口

3. **Flashcard 學習模式**
   - 翻牌顯示字母/音素 → 對應單字+emoji
   - 發音按鈕（TTS）、上/下一張、標記已學習

4. **Quiz 測驗模式**
   - 選擇題測驗、即時回饋、成績結算頁面

5. **Match 配對遊戲**
   - 記憶翻牌配對（音素 ↔ 單字）
   - 三種難度（Easy 4 / Medium 6 / Hard 8 對）
   - 計時器、步數統計

6. **Blending 拼讀模式**
   - 逐音素發音 → 混合拼讀完整單字
   - 三種速度（Slow / Normal / Fast）
   - 點擊個別音素聽發音

7. **共用功能**
   - Web Speech API（TTS）語音朗讀
   - LocalStorage 進度儲存
   - 慶祝動畫（confetti + 獎盃彈窗）
   - 響應式手機友善設計

### Phonics 資料涵蓋範圍
| Phase | 主題 | 內容 |
|-------|------|------|
| 1 | Alphabet Sounds | 26 個字母音 a-z |
| 2 | Phonics Sounds | s a t p i n m d g o c k ck e u r h b f ff l ll ss |
| 3 | Digraphs & Vowels | ch sh th ng ai ee igh oa oo ar or ur ow oi ear air ure er |
| 4 | Adjacent Consonants | CVCC/CCVC 混合子音 |
| 5 | Long Vowels | a_e e_e i_e o_e u_e 長母音 |
| 6 | Suffixes & More | -ing -ed -er -est -ful -ly -ness 等字尾 |

## 待辦 / 可改進項目
- [ ] （尚未有明確的下一步任務，等待使用者指示）

## 技術筆記
- 純前端，無需 build 工具或伺服器
- 使用 CSS 變數管理配色
- TTS 使用 `window.speechSynthesis`
- 進度儲存於 `localStorage`（key: `phonicsProgress`）
- 所有動畫使用 CSS @keyframes

---
*最後更新：2026-02-15*
