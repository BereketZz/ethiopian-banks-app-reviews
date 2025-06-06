<h1>Ethiopian Mobile Banking Review Analysis</h1>

<p>This project is part of Omega Consultancy’s Week 2 Data Challenge. It focuses on scraping, preprocessing, and analyzing Google Play Store reviews for mobile banking apps from three Ethiopian banks: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank.</p>

<h2> Task1 Project Goals</h2>
<ul>
  <li>Scrape at least <strong>400 reviews per bank</strong> from the Google Play Store.</li>
  <li>Preprocess review data for quality and consistency.</li>
  <li>Prepare cleaned dataset for further sentiment and thematic analysis.</li>
</ul>

<h2> Tools & Technologies</h2>
<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>Google Play Scraper (unofficial API)</li>
  <li>Jupyter Notebook / Google Colab</li>
  <li>GitHub for version control</li>
</ul>

<h2>Data Description</h2>
<p>Each review record includes the following fields:</p>
<ul>
  <li><code>review</code> - Text of the user review</li>
  <li><code>rating</code> - User's rating (1 to 5 stars)</li>
  <li><code>date</code> - Date of review (YYYY-MM-DD)</li>
  <li><code>bank</code> - Bank name (CBE, BOA, or Dashen)</li>
  <li><code>source</code> - Always "Google Play"</li>
</ul>

<h2> Preprocessing Methodology</h2>
<ol>
  <li><strong>Removed duplicate reviews</strong> using the text field as a unique identifier.</li>
  <li><strong>Dropped missing or null values</strong> for review, rating, or date fields.</li>
  <li><strong>Trimmed whitespace</strong> and removed empty string reviews.</li>
  <li><strong>Standardized date format</strong> to YYYY-MM-DD.</li>
</ol>

<h2> Output</h2>
<p>The cleaned dataset is saved as:</p>
<pre><code>clean_bank_reviews.csv</code></pre>
<p>It contains 1,150+ high-quality reviews across the three banks.</p>


