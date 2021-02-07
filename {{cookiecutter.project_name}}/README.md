# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Project Features

* {{ cookiecutter.project_name}}
* A starter KiCad project structured in a manner of <https://hackaday.com/2017/05/18/kicad-best-practises-library-management/>

## Getting Started

## Resources

Below are some handy resource links.

* [KiCad](https://www.kicad.org/) is a Cross Platform and Open Source Electronics Design Automation suite.

## Authors

* **{{ cookiecutter.author_name }}** - *Initial Work* - [github](https://github.com/{{cookiecutter.github_user}})

See also the list of [contributors](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_github_repo_name}}/contributors) who participated in this project.

## License

{%- if cookiecutter.license == "MIT" -%}
MIT License

Copyright (c) {% now 'utc', '%Y' %}, {{cookiecutter.author_name}}

Permission is hereby granted, free of charge, to any person obtaining a copy of this hardware, software, and associated documentation files (the "Product"), to deal in the Product without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Product, and to permit persons to whom the Product is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Product.

THE PRODUCT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE PRODUCT OR THE USE OR OTHER DEALINGS IN THE PRODUCT.

{%- elif cookiecutter.license == "CC-A-SA" -%}
Creative Commons Attribution Share A like License

This is a human-readable summary of the full license below.

You are free:
* **to Share**—to copy, distribute and transmit the work, and
* **to Remix**—to adapt the work

Under the following conditions
* **Attribution**—You must attribute the work in the manner specified by the author or licensor (but not in any way that suggests that they endorse you or your use of the work.)
* **Share Alike**—If you alter, transform, or build upon this work, you may distribute the resulting work only under the same, similar or a compatible license.

With the understanding that:
* **Waiver** — Any of the above conditions can be waived if you get permission from the copyright holder.
* **Other Rights** — In no way are any of the following rights affected by the license:
    * your fair dealing or fair use rights;
    * the author's moral rights; and
    * rights other persons may have either in the work itself or in how the work is used, such as publicity or privacy rights.
* **Notice**—For any reuse or distribution, you must make clear to others the license terms of this work. The best way to do that is with a link to <http://creativecommons.org/licenses/by-sa/3.0/>

{%- elif cookiecutter.license == "CC-A" -%}
Creative Commons Attribution License

You are free:
* **to Share**—to copy, distribute and transmit the work, and
* **to Remix**—to adapt the work
  
Under the following conditions:
* **Attribution**—You must attribute the work in the manner specified by the author or licensor (but not in any way that suggests that they endorse you or your use of the work.)

With the understanding that:
* **Waiver—Any** of the above conditions can be waived if you get permission from the copyright holder.
* **Other Rights**—In no way are any of the following rights affected by the license:
    * your fair dealing or fair use rights;
    * the author's moral rights; and
    * rights other persons may have either in the work itself or in how the work is used, such as publicity or privacy rights.
* **Notice**—For any reuse or distribution, you must make clear to others the license terms of this work. The best way to do that is with a link to <http://creativecommons.org/licenses/by/3.0/>
  
{%- elif cookiecutter.license == "TAPR" -%}
TAPR Open Hardware License (OHL)

Visit the TAPR website for the [full text of the TAPR Open Hardware License (OHL)](http://www.tapr.org/ohl.html). The numbered sections of the agreement take precedence over this preamble.

* You may modify the documentation and make products based upon it.
* You may use products for any legal purpose without limitation.
* You may distribute unmodified documentation, but you must include the complete package as you received it.
* You may distribute products you make to third parties, if you either include the documentation on which the product is based, or make it available without charge for at least three years to anyone who requests it.

You may distribute modified documentation or products based on it, if you:
  * License your modifications under the OHL.
  * Include those modifications, following the requirements stated below.
  * Attempt to send the modified documentation by email to any of the developers who have provided their email address. This is a good faith obligation -- if the email fails, you need do nothing more and may go on with your distribution.

If you create a design that you want to license under the OHL, you should:
  * Include the OHL document in a file named LICENSE.TXT (or LICENSE.PDF) that is included in the documentation package.
  * If the file format allows, include a notice like "Licensed under the TAPR Open Hardware License (<www.tapr.org/OHL>)" in each documentation file. While not required, you should also include this notice on printed circuit board artwork and the product itself; if space is limited the notice can be shortened or abbreviated.
  * Include a copyright notice in each file and on printed circuit board artwork.

If you wish to be notified of modifications that others may make, include your email address in a file named "CONTRIB.TXT" or something similar.

Any time the OHL requires you to make documentation available to others, you must include all the materials you received from the upstream licensors. In addition, if you have modified the documentation:
  * You must identify the modifications in a text file (preferably named "CHANGES.TXT") that you include with the documentation. That file must also include a statement like "These modifications are licensed under the TAPR Open Hardware License."
  * You must include any new files you created, including any manufacturing files (such as Gerber files) you create in the course of making products.
  * You must include both "before" and "after" versions of all files you modified.
  * You may include files in proprietary formats, but you must also include open format versions (such as Gerber, ASCII, Postscript, or PDF) if your tools can create them.

{%- elif cookiecutter.license == "BSD" -%}

BSD License

Copyright (c) {% now 'utc', '%Y' %}, {{cookiecutter.github_user}}. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

  * Redistributions of product specifications, source code, and documentation must retain the above copyright notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS PRODUCT IS PROVIDED BY **{{cookiecutter.author_name}}** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL **{{cookiecutter.author_name}}** OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS PRODUCT, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the hardware, software, and documentation are those of the authors and should not be interpreted as representing official policies, either expressed or implied, of **{{cookiecutter.author_name}}**.

{%- elif cookiecutter.license == "OSHD" -%}

**Introduction**
Open Source Hardware Definition v1.0

Open Source Hardware (OSHW) is a term for tangible artifacts -- machines, devices, or other physical things -- whose design has been released to the public in such a way that anyone can make, modify, distribute, and use those things. This definition is intended to help provide guidelines for the development and evaluation of licenses for Open Source Hardware.

Hardware is different from software in that physical resources must always be committed for the creation of physical goods. Accordingly, persons or companies producing items ("products") under an OSHW license have an obligation to make it clear that such products are not manufactured, sold, warrantied, or otherwise sanctioned by the original designer and also not to make use of any trademarks owned by the original designer.

The distribution terms of Open Source Hardware must comply with the following criteria:

1. **Documentation**

The hardware must be released with documentation including design files, and must allow modification and distribution of the design files. Where documentation is not furnished with the physical product, there must be a well-publicized means of obtaining this documentation for no more than a reasonable reproduction cost, preferably downloading via the Internet without charge. The documentation must include design files in the preferred format for making changes, for example the native file format of a CAD program. Deliberately obfuscated design files are not allowed. Intermediate forms analogous to compiled computer code -- such as printer-ready copper artwork from a CAD program -- are not allowed as substitutes. The license may require that the design files are provided in fully-documented, open format(s).

2. **Scope**

The documentation for the hardware must clearly specify what portion of the design, if not all, is being released under the license.

3. **Necessary Software**

If the licensed design requires software, embedded or otherwise, to operate properly and fulfill its essential functions, then the license may require that one of the following conditions are met:

a) The interfaces are sufficiently documented such that it could reasonably be considered straightforward to write open source software that allows the device to operate properly and fulfill its essential functions. For example, this may include the use of detailed signal timing diagrams or pseudocode to clearly illustrate the interface in operation.

b) The necessary software is released under an OSI-approved open source license.

4. **Derived Works**

The license shall allow modifications and derived works, and shall allow them to be distributed under the same terms as the license of the original work. The license shall allow for the manufacture, sale, distribution, and use of products created from the design files, the design files themselves, and derivatives thereof.

5. **Free redistribution**

The license shall not restrict any party from selling or giving away the project documentation. The license shall not require a royalty or other fee for such sale. The license shall not require any royalty or fee related to the sale of derived works.

6. **Attribution**

The license may require derived documents, and copyright notices associated with devices, to provide attribution to the licensors when distributing design files, manufactured products, and/or derivatives thereof. The license may require that this information be accessible to the end-user using the device normally, but shall not specify a specific format of display. The license may require derived works to carry a different name or version number from the original design.

7. **No Discrimination Against Persons or Groups**

The license must not discriminate against any person or group of persons.

8. **No Discrimination Against Fields of Endeavor**

The license must not restrict anyone from making use of the work (including manufactured hardware) in a specific field of endeavor. For example, it must not restrict the hardware from being used in a business, or from being used in nuclear research.

9. **Distribution of License**

The rights granted by the license must apply to all to whom the work is redistributed without the need for execution of an additional license by those parties.

10. **License Must Not Be Specific to a Product**

The rights granted by the license must not depend on the licensed work being part of a particular product. If a portion is extracted from a work and used or distributed within the terms of the license, all parties to whom that work is redistributed should have the same rights as those that are granted for the original work.

11. **License Must Not Restrict Other Hardware or Software**

The license must not place restrictions on other items that are aggregated with the licensed work but not derivative of it. For example, the license must not insist that all other hardware sold with the licensed item be open source, nor that only open source software be used external to the device.

12. **License Must Be Technology-Neutral**

No provision of the license may be predicated on any individual technology, specific part or component, material, or style of interface or use thereof.

{%- elif cookiecutter.license == "CERN-OHL-P" -%}
CERN Open Hardware Licence Version 2 - Permissive


Preamble

CERN has developed this licence to promote collaboration among
hardware designers and to provide a legal tool which supports the
freedom to use, study, modify, share and distribute hardware designs
and products based on those designs. Version 2 of the CERN Open
Hardware Licence comes in three variants: this licence, CERN-OHL-P
(permissive); and two reciprocal licences: CERN-OHL-W (weakly
reciprocal) and CERN-OHL-S (strongly reciprocal).

The CERN-OHL-P is copyright CERN 2020. Anyone is welcome to use it, in
unmodified form only.

Use of this Licence does not imply any endorsement by CERN of any
Licensor or their designs nor does it imply any involvement by CERN in
their development.


1 Definitions

  1.1 'Licence' means this CERN-OHL-P.

  1.2 'Source' means information such as design materials or digital
      code which can be applied to Make or test a Product or to
      prepare a Product for use, Conveyance or sale, regardless of its
      medium or how it is expressed. It may include Notices.

  1.3 'Covered Source' means Source that is explicitly made available
      under this Licence.

  1.4 'Product' means any device, component, work or physical object,
      whether in finished or intermediate form, arising from the use,
      application or processing of Covered Source.

  1.5 'Make' means to create or configure something, whether by
      manufacture, assembly, compiling, loading or applying Covered
      Source or another Product or otherwise.

  1.6 'Notice' means copyright, acknowledgement and trademark notices,
      references to the location of any Notices, modification notices
      (subsection 3.3(b)) and all notices that refer to this Licence
      and to the disclaimer of warranties that are included in the
      Covered Source.

  1.7 'Licensee' or 'You' means any person exercising rights under
      this Licence.

  1.8 'Licensor' means a person who creates Source or modifies Covered
      Source and subsequently Conveys the resulting Covered Source
      under the terms and conditions of this Licence. A person may be
      a Licensee and a Licensor at the same time.

  1.9 'Convey' means to communicate to the public or distribute.


2 Applicability

  2.1 This Licence governs the use, copying, modification, Conveying
      of Covered Source and Products, and the Making of Products. By
      exercising any right granted under this Licence, You irrevocably
      accept these terms and conditions.

  2.2 This Licence is granted by the Licensor directly to You, and
      shall apply worldwide and without limitation in time.

  2.3 You shall not attempt to restrict by contract or otherwise the
      rights granted under this Licence to other Licensees.

  2.4 This Licence is not intended to restrict fair use, fair dealing,
      or any other similar right.


3 Copying, Modifying and Conveying Covered Source

  3.1 You may copy and Convey verbatim copies of Covered Source, in
      any medium, provided You retain all Notices.

  3.2 You may modify Covered Source, other than Notices.

      You may only delete Notices if they are no longer applicable to
      the corresponding Covered Source as modified by You and You may
      add additional Notices applicable to Your modifications.

  3.3 You may Convey modified Covered Source (with the effect that You
      shall also become a Licensor) provided that You:

       a) retain Notices as required in subsection 3.2; and

       b) add a Notice to the modified Covered Source stating that You
          have modified it, with the date and brief description of how
          You have modified it.

  3.4 You may Convey Covered Source or modified Covered Source under
      licence terms which differ from the terms of this Licence
      provided that You:

       a) comply at all times with subsection 3.3; and

       b) provide a copy of this Licence to anyone to whom You
          Convey Covered Source or modified Covered Source.


4 Making and Conveying Products

You may Make Products, and/or Convey them, provided that You ensure
that the recipient of the Product has access to any Notices applicable
to the Product.


5 DISCLAIMER AND LIABILITY

  5.1 DISCLAIMER OF WARRANTY -- The Covered Source and any Products
      are provided 'as is' and any express or implied warranties,
      including, but not limited to, implied warranties of
      merchantability, of satisfactory quality, non-infringement of
      third party rights, and fitness for a particular purpose or use
      are disclaimed in respect of any Source or Product to the
      maximum extent permitted by law. The Licensor makes no
      representation that any Source or Product does not or will not
      infringe any patent, copyright, trade secret or other
      proprietary right. The entire risk as to the use, quality, and
      performance of any Source or Product shall be with You and not
      the Licensor. This disclaimer of warranty is an essential part
      of this Licence and a condition for the grant of any rights
      granted under this Licence.

  5.2 EXCLUSION AND LIMITATION OF LIABILITY -- The Licensor shall, to
      the maximum extent permitted by law, have no liability for
      direct, indirect, special, incidental, consequential, exemplary,
      punitive or other damages of any character including, without
      limitation, procurement of substitute goods or services, loss of
      use, data or profits, or business interruption, however caused
      and on any theory of contract, warranty, tort (including
      negligence), product liability or otherwise, arising in any way
      in relation to the Covered Source, modified Covered Source
      and/or the Making or Conveyance of a Product, even if advised of
      the possibility of such damages, and You shall hold the
      Licensor(s) free and harmless from any liability, costs,
      damages, fees and expenses, including claims by third parties,
      in relation to such use.


6 Patents

  6.1 Subject to the terms and conditions of this Licence, each
      Licensor hereby grants to You a perpetual, worldwide,
      non-exclusive, no-charge, royalty-free, irrevocable (except as
      stated in this section 6, or where terminated by the Licensor
      for cause) patent licence to Make, have Made, use, offer to
      sell, sell, import, and otherwise transfer the Covered Source
      and Products, where such licence applies only to those patent
      claims licensable by such Licensor that are necessarily
      infringed by exercising rights under the Covered Source as
      Conveyed by that Licensor.

  6.2 If You institute patent litigation against any entity (including
      a cross-claim or counterclaim in a lawsuit) alleging that the
      Covered Source or a Product constitutes direct or contributory
      patent infringement, or You seek any declaration that a patent
      licensed to You under this Licence is invalid or unenforceable
      then any rights granted to You under this Licence shall
      terminate as of the date such process is initiated.


7 General

  7.1 If any provisions of this Licence are or subsequently become
      invalid or unenforceable for any reason, the remaining
      provisions shall remain effective.

  7.2 You shall not use any of the name (including acronyms and
      abbreviations), image, or logo by which the Licensor or CERN is
      known, except where needed to comply with section 3, or where
      the use is otherwise allowed by law. Any such permitted use
      shall be factual and shall not be made so as to suggest any kind
      of endorsement or implication of involvement by the Licensor or
      its personnel.

  7.3 CERN may publish updated versions and variants of this Licence
      which it considers to be in the spirit of this version, but may
      differ in detail to address new problems or concerns. New
      versions will be published with a unique version number and a
      variant identifier specifying the variant. If the Licensor has
      specified that a given variant applies to the Covered Source
      without specifying a version, You may treat that Covered Source
      as being released under any version of the CERN-OHL with that
      variant. If no variant is specified, the Covered Source shall be
      treated as being released under CERN-OHL-S. The Licensor may
      also specify that the Covered Source is subject to a specific
      version of the CERN-OHL or any later version in which case You
      may apply this or any later version of CERN-OHL with the same
      variant identifier published by CERN.

  7.4 This Licence shall not be enforceable except by a Licensor
      acting as such, and third party beneficiary rights are
      specifically excluded.

{%- else -%}
Copyright (c) {% now 'utc', '%Y' %}, {{cookiecutter.author_name}}

All rights reserved.
{%- endif -%}