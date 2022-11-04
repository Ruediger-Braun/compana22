.. -*- coding: utf-8 -*-

=========================================
Computergestützte Mathematik zur Analysis
=========================================

-------------------------------------------------------------------
Übersicht über die verwendeten Befehle, nach Lektionen geordnet
-------------------------------------------------------------------

Inhaltsverzeichnis
==================

.. contents:: Inhaltsverzeichnis

Lektion 1
*********

Numerisch
==========

+     ``+, -, *, /, **``

      arithmetische Operatoren


Symbolisch
==========

+     ``from sympy import *``

      Import der Bibliothek

*     ``S(x)``

      ``x`` als sympy-Ausdruck

+     ``Rational``
	    
      rationale Zahl (im Gegensatz zur Fließkommazahl)

Funktionen
==========

+     ``pi``

      Kreiszahl

+     ``sin, cos, tan, cot``

      trigonometrische Funktionen

+     ``asin, acos, atan, acot``

      inverse trigonometrische Funktionen

+     ``sqrt``

      Quadratwurzel

+     ``log, ln``

      natürlicher Logarithmus

+     ``exp``

      Exponentialfunktion

+     ``E``

      Eulersche Zahl

+     ``factorial``

      Fakultät

Beliebig genaue Fließkommazahlen
================================

+   ``N`` 

    numerische Auswertung in wählbarer Präzision


Sympyfizierungen
================

+   ``type``

    Typ eines Objekts

Variablen
=========

+   ``=``

    Zuweisung

Symbole
=======

+   ``x = S('x')``

    Einrichtung eines Symbols



+   ``symplify``

    Vereinfachung

+   ``==``

    Vergleich 


zurück zum Inhaltsverzeichnis_


Lektion 2
*********

Ersetzungen
===========

+   ``subs``

    Ersetzung (Methode)

factor und expand
=================

+   ``expand``

    Ausmultiplizieren

+   ``factor``

    Faktorisieren von Ausdrücken

+   ``cancel``

    Kürzen 

siehe auch Vereinfachungen_


Objekte
=======

+   ``is_prime``

    Primzahltest (Methode)


Primzahltest
============

+   ``isprime``

    Primzahltest (Funktion)

Vereinfachungen
===============

+   ``simplify``

    unspezifische Vereinfachungen

+   ``ratsimp``

    Vereinfachung von Brüchen

+   ``powsimp``

    Vereinfachung von Potenzen

+   ``%%timeit``

    ``jupyter``-Makro zur Laufzeitnessung

+   ``I``

    imaginäre Einheit (symbolisch)

+   ``j``

    imaginäre Einheit (Standard-Python)



Auswertung von Ausdrücken
=========================

+   NaN

    Not a Number (Ergebnis einer illegalen Fließkommaoperation)

Grenzwerte
==========

+   ``limit``

    Grenzwert

+   ``oo``

    Unendlich

+   ``zoo``

    unendlich ferner Punkt $\tilde\infty$ der komplexen Ebene (d.h. $\tilde\infty = -\tilde\infty$)

+   ``print``

    Ausgabe

+   ``Limit``

    träger Operator zu ``limit``

+   ``doit``

    Auswertung eines trägen Operators

zurück zum Inhaltsverzeichnis_

Lektion 3
*********

Ableitungen
===========

+   ``diff``

    Ableitung

Beispiel: Grenzwert mot Regel von l'Hôpital
===========================================

+   ``numer``

    Zähler

+   ``denom``

    Nenner

Ableitungen mit Parameter
=========================

+   ``collect``

    Ausklammern gemeinsamer Faktoren


Annahmen (assumptions)
======================

+   ``Symbol(x, real=True)``
        
    das Symbol wird als reell vereinbart

    Andere Annahmen: ``positive``, ``ǹegative``, ``integer``, ``even``, ``odd``

+   ``_assumptions``

    die zu einem Objekt vereinbarten Annahmen (Attribut eines Objekts)

Unbestimmte Integrale
=====================

+   ``Integral``

    Integral (träger Operator)

Bestimmte Integrale
===================

+   ``n``

    numerische Auswertung (Methode)

Boolesche Operatoren
====================

+   ``==``, ``!=``

    Test auf Gleichheit bzw. Ungleichheit

+   ``>``, ``>=``, ``<``, ``<=``

    Größenvergleich

+   ``True``, ``False``

    Wahrheitswerte

+   ``&``, ``|``, ``~``

    Operatoren "und", "oder" bzw. "nicht" bei Anwendung auf Symbole (für Wahrheitswerte gibt es noch ``and``, ``or`` und ``not``)

Fallunterscheidungen
====================

+   ``Piecewise``

    Fallunterscheidung 

zurück zum Inhaltsverzeichnis_

.. Verwandlung in html:  pandoc --embed-resources --standalone -o befehle.html --toc befehle.rst 



