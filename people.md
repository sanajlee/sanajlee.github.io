---
layout: page
title: people
permalink: /people
published: true
---

<style>
.people-note {
  color: #666;
  font-size: 0.95em;
  margin-bottom: 1.5rem;
}

.people-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.2rem;
  margin-top: 1rem;
}

/* 핵심: 가로형 카드 */
.person-card {
  display: flex;
  gap: 1rem;
  align-items: center;

  border: 1px solid #e8e8e8;
  border-radius: 14px;
  padding: 1rem;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

/* 사진 작게 */
.person-photo {
  width: 90px;
  height: 90px;
  object-fit: cover;
  border-radius: 10px;
  background: #f3f3f3;
  flex-shrink: 0;
}

/* 텍스트 영역 */
.person-text {
  flex: 1;
}

.person-name {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 0.2rem;
}

.person-role {
  color: #555;
  font-size: 0.95rem;
  margin-bottom: 0.5rem;
}

.person-bio {
  font-size: 0.95rem;
  line-height: 1.6;
  color: #333;
}

/* 모바일 대응 */
@media (max-width: 640px) {
  .person-card {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .person-photo {
    width: 100px;
    height: 100px;
  }
}
</style>

## People

### Current Students

<div class="people-grid">

  <div class="person-card">
    <img class="person-photo" src="uploads/chiikawa.jpg" alt="손욱염">
    
    <div class="person-text">
      <div class="person-name">손욱염 Sun, Xuran</div>
      <div class="person-role">M.A. Student</div>

      <div class="person-bio">
        Interests: L2 Learning, Interlanguage
      </div>
    </div>
  </div>
</div>

### Alumni

<div class="people-grid">

  <div class="person-card">
    <img class="person-photo" src="uploads/kitty.png" alt="강민지">
    
    <div class="person-text">
      <div class="person-name">강민지 Kang, Minji</div>
      <div class="person-role">Former M.A. Student</div>

      <div class="person-bio">
        Dissertation: Improving Multiple-Choice Distractor Generation via Enhanced Reading Comprehension and Human Feedback
      </div>
    </div>
  </div>

</div>