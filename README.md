A non-LDP reporting solution for FOLIO.  A work in progress; stay tuned for updates!

# Methodology

Rather than export data to a separate data warehouse for later analysis, this repo aims to make a reporting-capable schema within the FOLIO database using Views.  Based largely on the work of Jon Miller at UChicago (https://github.com/jemiller0/Folio/blob/master/FolioLibrary/Folio.sql)

**Advantages:**
 - Data is realtime
 - Fewer moving parts (external database, synchronization tool) to maintain

**Neutral Differences:**
 - Data retention levels may be different than when using a warehouse
 - Relationalization may be different per table than how LDP does it
 - Data security policies and responsible entities may be different than with a warehouse

**Disadvantages:**
 - Additional load on your FOLIO database; be careful of heavy-duty reports

# Requirements

- Python
  - Jinja2
- SQL access to your FOLIO database with an account able to:
  - Create Schema
  - Create Views
  - Create Roles
  - Grant privileges
- Network access to your FOLIO database from whatever client you're going to use
