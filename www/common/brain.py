#!/usr/bin/python3

import cgi
import cgitb; cgitb.enable();


def www_print_head(appname, tags=None):
  print("""
<!DOCTYPE html>
<html lang="en" prefix="og: http://ogp.me/ns#">
  <head>
    <title>Brain-1 - {appname}</title>
    <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="description" content="The front-end starter kit from Superawesome">
  <meta name="author" content="syzygyfpga.io">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/png" href="/assets/images/favicons/favicon-32x32.png" sizes="32x32">
  <link rel="stylesheet" href="/assets/css/styles-brain1.css">
""".format(appname=appname))
  if tags is not None: print(tags)
  print("</head>")


def www_print_title(appname, appdesc):
  print("""
  <body>
    <header class="page-header">
      <div class="page-header-content">
        <div class="page-header-content-wrap"><a class="page-header-logo" href="/" title="Go to homepage"><img src="/assets/images/logo.svg" alt="Syzygy Logo"></a></div><a class="menu-link" href="http://syzygyfpga.io">syzygyfpga.io</a>
      </div>
    </header>
    <main role="main">
      <section class="hero hero-page">
        <div class="hero-content">
          <div class="container">
            <h1 class="hero-title txtc">{appname}</h1>
            <p class="text-sm txtc">{appdesc}</p>
          </div>
        </div>
      </section>
  """.format(appname=appname, appdesc=appdesc))


def www_print_foot():
  print("""
      </main>
    </body>
  </html>
  """)


def www_start_section(title=None):
  print("""
  <section class="section pb-none">
  <div class="container text-content">
  """)

  if (title is not None):
    print('<h2 class="section-title">{title}</h2>'.format(title=title))

  print("""
  <div class="row">
  <div class="col-sm-12">
  """)


def www_end_section():
  print("""
  </div>
  </div>
  </div>
  </section>
  """)
