# TrustCheck API

A simple FastAPI application that scrapes Trustpilot ratings for a given domain.

## Overview
This API fetches Trustpilot ratings (e.g., "Excellent", "Good", "Bad") for a specified domain by scraping the Trustpilot review page. It uses FastAPI for the backend and BeautifulSoup for web scraping.

## Features
- **Endpoint**: `/rating/{domain}` - Returns the Trustpilot rating for a domain.
- **CORS Enabled**: Accessible from web clients (e.g., Chrome extensions).
- **Error Handling**: Returns "No rating found" if scraping fails or the domain lacks a Trustpilot page.

## Prerequisites
- Python 3.8+
- Git

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/codevader01/Trust_Checker.git
   cd Trust_Checker
