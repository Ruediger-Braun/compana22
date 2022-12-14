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

    unendlich ferner Punkt der komplexen Ebene  (die komplexe Ebene hat nur einen)

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

Lektion 4
*********

Listen und Arrays
=================

+   ``[]``

    Liste

+   ``append``

    anhängen an Liste

+   ``len``
    
    Länge einer Liste oder einer anderen Kollektion 

+   ``del``

    entfernen eines Listenelements
    
+   ``import numpy as np``

    Import der Grundbibliothek zur Numerik

+   ``np.array``

    Array 

+   ``init_printing``

    Listensatz mit LaTeX

+   ``dtype``

    Typ der Elemente eines Arrays

Schleifen
=========

+   ``range``

    konsekutiver Bereich ganzer Zahlen

+   ``list``

    Umwandlung in Liste

+   ``for``

    Schleife (Schleifenkörper wird eingerückt

Verzweigungen
=============

+   ``if``, ``elif``, ``else``

    Verzweigung

Dictionary
==========

+   ``{}``

    Assoziativer Speicher, dictionary

+   *a*``[``*key*``]``

    Element von *a* zum Schlüssel *key*

+   ``{}``

    Menge 

+   ``set()``

    leere Menge

+   ``|``, ``&``, ``-``

    Vereinigung, Durchschnitt und Mengendifferenz

+   ``in``

    Test auf Nitgliedschaft

+   ``add``

    Hinzufügen eines Elements

Polynome
========

+   ``degree``

    Grad

+   ``coeff``

    Koeffizient

+   ``args``

    Argumente eines Ausdrucks

zurück zum Inhaltsverzeichnis_

Lektion 5
+++++++++

Funktionen
==========

+   ``def``

    Definition einer Funktion (Funktionskörper wird eingerückt)

Mathematische Funktion vs. Programmfunktion
===========================================

+   ``lambdify``

    Verwandlung eines Sympy-Ausdrucks in eine Funktion

Einfache Plots von Ausdrücken
=============================

+   ``plot``

    Plot

+   ``legend``, ``show``

    Methoden eines Plots

Lösungen von Gleichungen
========================

+   ``Eq``

    Gleichung

+   ``solve``

    Lösung


+   ``raise``

    Auslösung einer Fehlerbedingung (exception)

Sympy rechnet komplex
=====================

+   ``I``

    imaginäre Einheit

+   ``re``, ``im``

    Real- und Imaginärteil (symbolisch)

+   ``conjugate``

    konjugiert komplexe Zahl

+   ``expand(complex=True)``

    Ausmultiplikation unter Berücksichtung der Regeln für Real- und Imaginärteil komplexer Zahlen

Mengen von Nullstellen
======================

+   ``solveset``

    Lösung von Gleichungen und Ungleichungen, Rückgabe als Menge

+   ``zip``

    Verschmelzung zweier Folgen zu einer Folge von Paaren

zurück zum Inhaltsverzeichnis_


   

Lektion 6
+++++++++

Nullstellen von Polynomen
=========================

+   ``CRootOf``

    Nullstelle eines irreduziblen Polynoms

+   ``minimal_polynomial``

    Minimalpolynom

Ungleichungen
=============

+   ``Interval``

    Intervall

+   ``EmptySet``

    leere Menge als Element der Booleschen Mengenalgebra

Die Lambertsche W-Funktion
==========================

Annahmen bei Integralen
=======================

Die Argumentfunktion
====================

+   ``arg``

    Argument einer komplexen Zahl

Beispiel für ein Integral einer periodischen Funktion
=====================================================

+   ``floor``, ``ceil``

    größste ganze Zahl unterhalb und kleinste ganze Zahl oberhalb einer Zahl

zurück zum Inhaltsverzeichnis_

Lektion 7
+++++++++

Weitere Integrale
=================

Summen
======

+   ``Sum``

    symbolische Summe

+   ``Abs``

    symbolischer Absolutbetrag

+   ``zeta``

    Riemannsche ζ-Funktion

Zeichenketten
=============

Polarkoordinaten
================

+   ``atan2``

    Winkelanteil der Polarkoordinaten

Potenzfunktionen
================

zurück zum Inhaltsverzeichnis_

Lektion 8
+++++++++

nutzergesteuerte trigonometrische Vereinfachungen
=================================================

+   ``trigsimp``

    trogonometrische Umformungen

+   ``count_ops``

    Anzahl der Operatoren eines Ausdrucks

Reihendarstellungen
===================

+   ``series``

    Reihenentwicklung

+   ``removeO``

    Entfernung des O-Terms

+   ``O``

    der O-Term

Beispiel mit der Lambert-Funktion
=================================

Vektoren und Matrizen
=====================

+   ``Matrix``

    Matrix

+   ``row``, ``col``

    Zugriff auf Zeilen und Spalten einer Matrix

variable Vektoren
=================

zurück zum Inhaltsverzeichnis_

.. Verwandlung in html:  pandoc --embed-resources --standalone -o befehle.html --toc befehle.rst 







