#                   --What is Xss--
# A Cross-Site Scripting (XSS) attack occurs when a malicious script is injected into an otherwise trusted and 
# legitimate website. Because web browsers inherently trust the code coming from these trusted domains, they 
# will execute the attacker's script as if it were an authorized part of the website.
#                   --How an XSS Attack Works--
# When a website lacks proper security checks (like input validation or output encoding), a hacker can embed 
# executable code—most commonly JavaScript—directly into web pages or URLs. When an unsuspecting user visits 
# the compromised page, the victim's browser is tricked into running this injected code.
#
#                   --Types of XSS Attacks--  
# 1. Stored (Persistent) XSS: The attacker posts malicious code directly to the website (e.g., in a comment 
#    section or profile update). The code is permanently stored in the site's database, meaning it triggers 
#    automatically for every user who views that specific page.
# 2. Reflected (Non-Persistent) XSS: The malicious code is embedded into a URL or form input. The code is not 
#    stored on the server but is immediately "reflected" back to the user who clicks a specially crafted link. 
#    Attackers typically distribute these links via phishing or social engineering.
# 3. DOM-based XSS: This vulnerability exists entirely on the client-side. An attacker manipulates the 
#    website's client-side JavaScript to process data from the URL (like a query parameter) in an unsafe 
#    way, causing the browser to execute the script.
# 
# Example: 
# <script>alert('XSS Attack!');</script>
# <img src='asdf' onerror=alert('You've been hacked!')>
# <img src= '' onerror=prompt()>
# <img src=1 onerror="javascript:alert(1)">
