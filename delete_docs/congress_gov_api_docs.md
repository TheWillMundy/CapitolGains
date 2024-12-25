================================================
File: /Documentation/HouseRequirementEndpoint.md
================================================
# House requirement endpoints

## Coverage

Coverage information for House requirements data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about House requirements data within [About Communications to the House](https://www.congress.gov/help/house-communications) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the House requirement API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/house-requirement/house_requirement).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that House requirement items at the list level cannot be filtered ([https://api.congress.gov/v3/house-requirement](https://api.congress.gov/v3/house-requirement)).

`<api-root>`

The `<api-root>` is only present in the XML format.

`<houseReqirements>`

Parent container for House requirements. A `<houseReqirements>` element may include the following children:

- `<item>`
  - Container for a House requirement item. An `<item>` element is repeatable and may include the following children:
    - `<number>` (e.g. 12478)
      - The assigned requirement number.
    - `<updateDate>` (e.g. 2021-11-05)
      - The date of update in Congress.gov.
    - `<url>` (e.g. <https://api.congress.gov/v3/house-requirement/12478>)
      - A referrer URL to the House requirement item in the API.

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<houseRequirement>`

Parent container for a House requirement item. A `<houseRequirement>` element may include the following children:

- `<number>` (e.g. 12478)
  - The assigned House requirement number.
- `<updateDate>` (e.g. 2021-11-05)
  - The date of update in Congress.gov.
- `<parentAgency>` (e.g. Executive Office of the President)
  - The government entity mandated to submit a report.
- `<frequency>` (e.g. If specified circumstances arise.)
  - The set interval for when a report is mandated to be submitted.
- `<nature>` (e.g. Approval of recommendations related to reducing the costs of federal real estate.)
  - The brief description of the report.
- `<legalAuthority>` (e.g. Public Law 114–287, section 13(c)(1); (130 Stat. 1471))
  - Citations to the statute associated with the House requirement.
- `<activeRecord>` (e.g., True)
  - Flag to indicate whether the requirement is active.
  - Possible values are "True" and "False".
- `<submittingAgency>` (e.g., Office of Management and Budget)
  - The government agency mandated to submit a report.
- `<submittingOfficial>` (e.g., Director)
  - The government official mandated to submit a report.
- `<matchingCommunications>` (the below data is taken from <https://api.congress.gov/v3/house-requirement/8070?api_key=>):
  - Container for matching communications to the requirement. A `<matchingCommunications>` element includes the following children:
    - `<count>` (e.g., 85138)
      - The number of matching communications to the requirement.
    - `<url>` (e.g., <https://api.congress.gov/v3/house-requirement/8070/matching-communications>)
      - A referrer URL to the matching communications level of the house requirement API. Click [here](#matching-communications-level) for more information on the matching communications level. 

### Matching Communications Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<matchingCommunications>`

Parent container for matching House communications to the requirement. A `<matchingCommunications>` element may include the following children:

- `<item>`
  - Container for a House communication item. An `<item>` element is repeatable and may include the following children:
    - `<chamber>` (e.g. House)
      - The chamber where the communication was received. This value will always be set to "House".
    - `<number>` (e.g. 1)
      - The assigned communication number.
    - `<communicationType>`
      - Container for communication type information. A `<communicationType>` element may include the following children:
        - `<code>` (e.g. EC)
          - The code for the type of communication.
          - Possible values are "EC", "PM", "PT", and "ML".
        - `<name>` (e.g. Executive Communication)
          - The name of the type of communication.
          - Possible values are "Executive Communication", "Presidential Message", "Petition", and "Memorial".
    - `<congress>` (e.g. 115)
      - The congress during which the communication was received.
      - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
    - `<url>` (e.g. <https://api.congress.gov/v3/house-communication/115/EC/1>)
      - A referrer URL to the communication item in the API.


================================================
File: /Documentation/HearingEndpoint.md
================================================
# Hearing endpoints

## Coverage 

Coverage information for hearing data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about hearing data at [About Committees and Committee Materials](https://www.congress.gov/help/committee-materials#committee-hearings) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the hearing API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/hearing/hearing_list).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that hearing items at the list level can be filtered by congress (e.g., 116) and by chamber (e.g., house) - <https://api.congress.gov/v3/hearing/116/house?api_key=>.

`<api-root>`

The `<api-root>` is only present in the XML format.

`<hearings>`

Container for hearings. A `<hearings>` container may include the following children:

- `<item>`
     - Container for an individual hearing. An `<item>` element is repeatable and may include the following children:
         - `<jacketNumber>` (e.g., 37721)
             - The jacket identifier of the hearing. The `<jacketNumber>` is printed on the front page of a hearing and is usually five digits.
         - `<updateDate>` (e.g., 2022-06-30 03:50:22+00:00)
             - The date of update in Congress.gov.
         - `<chamber>` (e.g., Senate)
             - The chamber where the hearing was held. 
             - Possible values are "House", "Senate", and "NoChamber".
         - `<congress>` (e.g., 116)
             - The congress during which the hearing was held.
             - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
         - `<number>` (e.g., 64)
             - The hearing number. 
             - Hearings may or may not be numbered by their associated committee.
         - `<part>`
             - The hearing's part number, if printed in parts.
         - `<url>` (e.g., <https://api.congress.gov/v3/hearing/116/senate/37721>)
             - A referrer URL to the hearing item in the API.

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<hearing>`

Parent container for a single hearing. A `<hearing>` element may include the following children:

- `<jacketNumber>` (e.g., 37721)
     - The jacket identifier of the hearing. The `<jacketNumber>` is printed on the front page of a hearing and is usually five digits.
- `<libraryOfCongressIdentifier>` (e.g., LC64252)
     - The Library of Congress identifier for a hearing. While unlikely, this number may change.
- `<number>` (e.g., 64)
     - The hearing number. 
     - Hearings may or may not be numbered by their associated committee.
- `<part>`
     - The hearing part number, if printed in parts.
- `<updateDate>` (e.g., 2022-06-30 03:50:22+00:00)
     - The date of update in Congress.gov.
- `<congress>` (e.g., 116)
     - The congress during which the hearing was held.
     - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
- `<title>` (e.g., OUTSIDE PERSPECTIVES ON THE COLLECTION OF BENEFICIAL OWNERSHIP INFORMATION)
     - The title of the hearing.
- `<citation>` (e.g., S.Hrg.116-64)
     - The hearing's citation.
     - Hearings may or may not be numbered by their associated committee.
- `<chamber>` (e.g., Senate)
     - The chamber where the hearing was held. 
     - Possible values are "House", "Senate", and "NoChamber".
- `<committees>`
     - Container for the committees that held the hearing. A `<committees>` element may include the following children:
         - `<item>`
             - Container for an individual committee that held the hearing. An `<item>` element is repeatable and may include the following children:
                 - `<name>` (e.g., Senate Banking, Housing, and Urban Affairs Committee)
                     - The name of the committee.
                 - `<systemCode>` (e.g., ssbk00)
                     - Unique ID value for the committee.
                 - `<url>` (e.g., https://api.congress.gov/v3/committee/senate/ssbk00)
                     - A referrer URL to the committee item in the API. Documentation for the committee endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeEndpoint.md).
- `<dates>`
     - Container for dates when the hearing was held. A `<dates>` element may include the following children:
         - `<item>`
             - Container for an individual date when the hearing was held. An `<item>` element is repeatable and may include the following children:
                 - `<date>` (e.g., 2019-06-20)
                     - A date when the hearing was held.
- `<formats>`
     - Container for the hearing transcript text formats. A `<formats>` element may include the following children:
         - `<item>`
             - Container for an individual hearing transcript text format. An `<item>` element is repeatable and may include the following children.
                 - `<type>` (e.g., PDF)
                     - The format type for the hearing transcript text.
                     - Possible values are "PDF" and "Formatted Text".
                 - `<url>` (e.g., <https://congress.gov/116/chrg/CHRG-116shrg37721/CHRG-116shrg37721.pdf>)
                     - The URL for the hearing transcript text in Congress.gov.
- `<associatedMeeting>`
     - Container for the hearing meeting information. An `<associatedMeeting>` element may include the following children:
         - `<eventID>`
             - The individual hearing meeting event identifier.
         - `<URL>`
             - Referrer URL to the committee hearing meeting item in the API. 


================================================
File: /Documentation/CommitteeReportEndpoint.md
================================================
# Committee Report endpoints

## Coverage

Coverage information for committee reports data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about committee reports data at [About Committee Reports of the U.S. Congress](https://www.congress.gov/help/committee-reports) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the committee report API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/committee-report/committee_reports).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that committee report items at the list level can be filtered down by congress (e.g. 117) and by report type (e.g. hrpt) – <https://api.congress.gov/v3/committee-report/117/hrpt?api_key>=.

`<api-root>`

The `<api-root>` is only present in the XML format.

`<reports>`

 Parent container for committee reports. A `<reports>` element may include the following children:

- `<item>`
  - Container for an individual committee report. An `<item>` element is repeatable and may include the following children:
    - `<citation>` (e.g., H. Rept. 117-351)
      - The report's citation, which consists of the report type, congress number, and the assigned report number.
    - `<url>` (e.g., <https://api.congress.gov/v3/committee-report/117/HRPT/351>)
      - A referrer URL to the report item in the API.
    - `<updateDate>` (e.g., 2022-08-13 19:26:27+00:00)
      - The date of update in Congress.gov
    - `<congress>` (e.g., 117)
      - The congress during which the committee report was produced.
      - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
    - `<chamber>` (e.g., House)
      - The chamber where the committee report was produced.
      - Possible values are "House" and "Senate".
    - `<type>` (e.g., HRPT)
      - The type of report.
      - Possible values are "HRPT", "SRPT", and "ERPT".
    - `<number>` (e.g., 351)
      - The assigned committee report number.
    - `<part>` (e.g., 1)
      - The part number of the report.
      - Committee reports without parts will have a value of 1. If there are multiple parts, the number value may be 2, 3, etc.

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<committeeReports>`

Parent container for multiple committee report parts within a single report. A `<committeeReports>` element may include the following children:

- `<committeeReport>`
  - Container for a single report or report part. A `<committeeReport>` element may include the following children:
    - `<committees>`
      - Container for the committees associated with a report. A `<committees>` element may include the following children, which are repeatable:
        - `<item>`
          - Container for an individual committee associated with a report. An `<item>` element is repeatable and may include the following children:
        - `<url>` (e.g., <https://api.congress.gov/v3/committee/house/hsba00>)
          - A referrer URL to the committee item in the API. Documentation for the committee endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeEndpoint.md).
        - `<systemCode>` (e.g., hsba00)
          - Unique ID value for the committee.
        - `<name>` Financial Services Committee
          - The name of the committee.
    - `<congress>` (e.g., 117)
      - The congress during which the committee report was produced.
      - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
    - `<chamber>` (e.g., House)
      - The chamber where the committee report was produced.
      - Possible values are "House" and "Senate".
    - `<sessionNumber>` (e.g., 2)
      - The session of congress during which the report was produced.
      - Possible values are "1" and "2".
    - `<citation>` (e.g., H. Rept. 117-351)
      - The report's citation, which consists of the report type, congress number, and the assigned report number.
    - `<number>` (e.g., 351)
      - The assigned committee report number.
    - `<part>` (e.g., 1)
      - The part number of the report.
      - Committee reports without parts will have a value of 1. If there are multiple parts, the number value may be 2, 3, etc.
    - `<type>` (e.g., HRPT)
      - The type of report.
      - Possible values are "HRPT", "SRPT", and "ERPT".  
    - `<updateDate>` (e.g., 2022-06-21T23:26:16Z)
      - The date of update in Congress.gov.
    - `<isConferenceReport>` (e.g., False)
      - Flag indicating whether the report is a conference report.
      - Possible values are "True" or "False".
    - `<title>` (e.g., EXPANDING FINANCIAL ACCESS FOR UNDERSERVED COMMUNITIES ACT)
      - The title of the committee report.
    - `<issueDate>` (e.g., 2022-06-07T04:00:00Z)
      - The date the report was issued.
    - `<reportType>` (e.g., H.Rept.)
      - The type of report.
      - Possible values are "S.Rept", "H.Rept", and "Ex.Rept".
    - `<text>`
      - Container for committee report text. A `<text>` element may include the following children:
        - `<count>` (e.g., 2)
          - The number of text formats for the committee report.
        - `<url>` (e.g., <https://api.congress.gov/v3/committee-report/117/hrpt/351/text>)
          - A referrer URL to the text level of the committee report API. Click [here](#text-level) for more information about the text level.
  - `<associatedTreaties>`
    - Container for associated treaties to the executive report. An `<associatedTreaties>` element may include the following children (the below data is taken from <https://api.congress.gov/v3/committee-report/117/erpt/5?api_key>=):
      - `<item>`
        - Container for an associated treaty. An `<item>` element is repeatable and may include the following children:
          - `<congress>` (e.g., 117)
            - The congress during which the treaty was submitted.
            - Unlike bills and resolutions, treaties remain active in a congress until they are ratified or returned to the President.
          - `<number>` (e.g., 3)
            - The assigned treaty number.
          - `<part>`
            - The treaty part, if the treaty was partitioned.
            - Possible values include "A", "B", "C", etc.
          - `<url>` (e.g., <https://api.congress.gov/v3/treaty/117/3>)
            - A referrer URL to the treaty item on the API.
            - Documentation for the treaty endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/TreatyEndpoint.md).
  - `<associatedBill>`
    - Container for associated bills to the committee report. An `<associatedBill>` element may include the following children:
      - `<item>`
        - Container for an associated bill. An `<item>` element is repeatable and may include the following children:
          - `<congress>` (e.g., 117)
            - The congress during which a bill or resolution was introduced or submitted.
          - `<type>` (e.g., HR)
            - The type of bill or resolution.
            - Possible values are "HR", "S", "HJRES", "SJRES", "HCONRES", "SCONRES", "HRES", and "SRES".
          - `<number>` (e.g., 7003)
            - The assigned bill or resolution number.
          - `<url>` (e.g., <https://api.congress.gov/v3/bill/117/hr/7003>)
            - A referrer URL to the bill or resolution item in the API. Documentation for the bill endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/BillEndpoint.md).

### Text Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<textVersions>`

Parent container for the text versions of a committee report. A `<textVersion>` element may include the following children, which are repeatable:

- `<item>`
  - Container for a text version of the report. An `<item>` element is repeatable and may include the following children:
    - `<formats>`
      - Container for a text format for the committee report. A `<formats>` element may include the following children:
        - `<item>`
          - Container for a report version. An `<item>` element is repeatable and may include the following children:
            - `<url>` (e.g., <https://www.congress.gov/117/crpt/hrpt351/generated/CRPT-117hrpt351.htm>)
              - The URL for the text version format for the committee report.
              - Work is scheduled to make the URL absolute, instead of relative.
            - `<type>` (e.g., Formatted Text)
              - The format type for the committee report text.
              - Possible values are "Formatted Text" and "PDF".
            - `<isErrata>` (e.g., N)
              - Flag indicating whether the text is errata or not.
              - Possible values are "Y" or "N".


================================================
File: /Documentation/TreatyEndpoint.md
================================================
# Treaty endpoints

## Coverage

Coverage information for treaty data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about treaty data at [About Treaty Documents](https://www.congress.gov/help/treaty-documents) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the treaty API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/treaty/treaty_list).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that treaty document items at the list level can be filtered down by congress of submission (e.g. 117) – <https://api.congress.gov/v3/treaty?api_key>=.

`<api-root>`

The `<api-root>` is only present in the XML format.

`<treaties>`  

Parent container for treaties. A `<treaties>` element may include the following children:

- `<item>`
  - Container for an individual treaty. An `<item>` element is repeatable and may include the following children:
    - `<congressReceived>` (e.g., 117)
      - The congress during which the treaty was submitted.
      - Unlike bills and resolutions, treaties remain active in a congress until they are ratified or returned to the President.
      - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
    - `<congressConsidered>` (e.g., 117)
      - The congress during which the treaty was ratified or returned to the President.
    - `<number>` (e.g., 3)
      - The assigned treaty number.
    - `<suffix>`
      - The treaty part, if the treaty was partitioned.
      - Possible values include "A", "B", "C", etc.
    - `<transmittedDate>` (e.g., 2022-07-11T00:00:00Z)
      - The date the treaty was transmitted to the Senate.
    - `<resolutionText>` (e.g., `<![CDATA[<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" lang="en"><head><meta name="meta:creation-date" content="2022/08/03 18:28:08" /><meta name="dc:title" content="[117] TreatyRes. 6 for TreatyDoc. 117 - 3" /><meta name="Creation-Date" content="2022/08/03 18:28:08" /><meta name="dcterms:created" content="2022/08/03 18:28:08" /><meta name="Content-Type" content="application/rtf" /><title>[117] TreatyRes. 6 for TreatyDoc. 117 - 3</title></head><body><p>As approved by the Senate: </p><p><i>Resolved (two-thirds of the Senators present concurring therein),</i></p><p></p><p><b>SECTION 1. SENATE ADVICE AND CONSENT SUBJECT TO DECLARATIONS AND CONDITIONS.</b></p><p></p><p>The Senate advises and consents to the ratification of the Protocols to the North Atlantic Treaty of 1949 on the Accession of the Republic of Finland and the Kingdom of Sweden, which were signed on July 5, 2022, by the United States of America and other parties to the North Atlantic Treaty of 1949 (Treaty Doc. 117-3), subject to the declarations of section 2 and the condition of section 3.</p><p><b>SEC. 2. DECLARATIONS.</b></p><p></p><p>The advice and consent of the Senate under section 1 is subject to the following declarations:</p><p>(1)Reaffirmation That United States Membership in NATO Remains a Vital National Security Interest of the United States.- The Senate declares that-</p><p>(A)for more than 70 years the North Atlantic Treaty Organization (NATO) has served as the preeminent organization to defend the countries in the North Atlantic area against all external threats;</p><p>(B)through common action, the established democracies of North America and Europe that were joined in NATO persevered and prevailed in the task of ensuring the survival of democratic government in Europe and North America throughout the Cold War;</p><p>(C)NATO enhances the security of the United States by embedding European states in a process of cooperative security planning and by ensuring an ongoing and direct leadership role for the United States in European security affairs;</p><p>(D)the responsibility and financial burden of defending the democracies of Europe and North America can be more equitably shared through an alliance in which specific obligations and force goals are met by its members;</p><p>(E)the security and prosperity of the United States is enhanced by NATO's collective defense against aggression that may threaten the security of NATO members; and</p><p>(F)United States membership in NATO remains a vital national security interest of the United States.</p><p>(2)Strategic Rationale for NATO Enlargement.- The Senate declares that-</p><p>(A)the United States and its NATO allies face continued threats to their stability and territorial integrity;</p><p>(B)an attack against Finland or Sweden, or the destabilization of either arising from external subversion, would threaten the stability of Europe and jeopardize United States national security interests;</p><p>(C)Finland and Sweden, having established democratic governments and having demonstrated a willingness to meet the requirements of membership, including those necessary to contribute to the defense of all NATO members, are in a position to further the principles of the North Atlantic Treaty and to contribute to the security of the North Atlantic area; and</p><p>(D)extending NATO membership to Finland and Sweden will strengthen NATO, enhance stability in Europe, and advance the interests of the United States and its NATO allies.</p><p>(3)Support for NATO's Open Door Policy.- The policy of the United States is to support NATO's Open Door Policy that allows any European country to express its desire to join NATO and demonstrate its ability to meet the obligations of NATO membership.</p><p>(4)Future Consideration of Candidates for Membership in NATO.-</p><p>(A)Senate Finding.-The Senate finds that the United States will not support the accession to the North Atlantic Treaty of, or the invitation to begin accession talks with, any European state (other than Finland and Sweden), unless-</p><p>(i)the President consults with the Senate consistent with Article II, section 2, clause 2 of the Constitution of the United States (relating to the advice and consent of the Senate to the making of treaties); and</p><p>(ii)the prospective NATO member can fulfill all of the obligations and responsibilities of membership, and the inclusion of such state in NATO would serve the overall political and strategic interests of NATO and the United States.</p><p>(B)Requirement for Consensus and Ratification.-The Senate declares that no action or agreement other than a consensus decision by the full membership of NATO, approved by the national procedures of each NATO member, including, in the case of the United States, the requirements of Article II, section 2, clause 2 of the Constitution of the United States (relating to the advice and consent of the Senate to the making of treaties), will constitute a commitment to collective defense and consultations pursuant to Articles 4 and 5 of the North Atlantic Treaty.</p><p>(5)Influence of Non-NATO Members on NATO Decisions.- The Senate declares that any country that is not a member of NATO shall have no impact on decisions related to NATO enlargement.</p><p>(6)Support for 2014 Wales Summit Defense Spending Benchmark.--The Senate declares that all NATO members should spend a minimum of 2 percent of their Gross Domestic Product (GDP) on defense and 20 percent of their defense budgets on major equipment, including research and development, by 2024, as outlined in the 2014 Wales Summit Declaration.</p><p><b>SEC. 3. CONDITION.</b></p><p></p><p>The advice and consent of the Senate under section 1 is subject to the following conditions</p><p>(1)Presidential Certification.-Prior to the deposit of the instrument of ratification, the President shall certify to the Senate as follows:</p><p>(A)The inclusion of Finland and Sweden in NATO will not have the effect of increasing the overall percentage share of the United States in the common budgets of NATO.</p><p>(B)The inclusion of Finland and Sweden in NATO does not detract from the ability of the United States to meet or to fund its military requirements outside the North Atlantic area.</p><p><b>SEC. 4. DEFINITIONS.</b></p><p></p><p>In this resolution:</p><p>(1)NATO Members.-The term &ldquo;NATO members&rdquo; means all countries that are parties to the North Atlantic Treaty.</p><p>(2)Non-NATO Members.-The term &ldquo;non-NATO members&rdquo; means all countries that are not parties to the North Atlantic Treaty.</p><p>(3)North Atlantic Area.-The term &ldquo;North Atlantic Area&rdquo; means the area covered by Article 6 of the North Atlantic Treaty, as applied by the North Atlantic Council.</p><p>(4)North Atlantic Treaty.-The term &ldquo;North Atlantic Treaty&rdquo; means the North Atlantic Treaty, signed at Washington April 4, 1949 (63 Stat. 2241; TIAS 1964), as amended.</p><p>(5)United States Instrument of Ratification.-The term &ldquo;United States instrument of ratification&rdquo; means the instrument of ratification of the United States of the Protocols to the</p><p>North Atlantic Treaty of 1949 on the Accession of the Republic of Finland and the Kingdom of Sweden.</p></body></html>]]>`)
      - The text of the resolution of ratification.
      - Note that the text is encased in CDATA and includes HTML codes.
    - `<topic>` (e.g., International Law and Organization)
      - The assigned topic of the treaty.  
    - `<updateDate>` (e.g., 2022-08-04T02:46:11Z)
      - The date of update on Congress.gov.
    - `<parts>`
      - Container for treaty part information. A `<parts>` element may include the following children (the below data is taken from <https://api.congress.gov/v3/treaty/114/13>):
        - `<count>` (e.g., 2)
          - The number of treaty parts.
        - `<urls>`
          - Container for the referrer URLs to the treaty part items in the API. A `<urls>` element may include the following children:
            - `<item>` (e.g., <https://api.congress.gov/v3/treaty/114/13/B>)
              - A referrer URL to the treaty part item in the API.
    - `<url>` (e.g., <http://https://api.congress.gov/v3/treaty/117/3>)
      - A referrer URL to the treaty item on the API.

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<treaty>`

- Parent container for an individual treaty. A `<treaty>` element may include the following children:
  - `<congressReceived>` (e.g., 117)
    - The congress during which the treaty was submitted.
    - Unlike bills and resolutions, treaties remain active in a congress until they are ratified or returned to the President.
    - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
  - `<congressConsidered>` (e.g., 117)
    - The congress during which the treaty was ratified or returned to the President.
  - `<number>` (e.g., 3)
    - The assigned treaty number.
  - `<suffix>`
    - The treaty part, if the treaty was partitioned.
    - Possible values include "A", "B", "C", etc.
  - `<countriesParties>`
    - The country/ies associated with a particular treaty.
    - `<item>`
      - Container element for individual countries/parties associated with the treaty. An <item> element may include the following children:
         - `<name>` (e.g., North Macedonia)
           - The name of the associated country.
  - `<oldNumber>`
    - The number assigned to treaties ratified prior to the 97th Congress.
    - To allow for searching by treaty document number on Congess.gov, old treaty numbers were converted. View the table that converts the old numbering to a new one at the [Treaty Numbers Conversion Table](https://www.congress.gov/help/treaty-documents#conversion) on Congress.gov.
  - `<oldNumberDisplayName>`
    - The original treaty number display string, prior to conversion, for treaties ratified prior to the 97th Congress.
    - To allow for searching by treaty document number on Congess.gov, old treaty numbers were converted. View the table that converts the old numbering method to a new one at the [Treaty Numbers Conversion Table](https://www.congress.gov/help/treaty-documents#conversion) on Congress.gov.
  - `<transmittedDate>` (e.g., 2022-07-11T00:00:00Z)
    - The date the treaty was transmitted to the Senate.
  - `<inForceDate>`
    - The date when the treaty agreement takes effect.
  - `<indexTerms>`
    - The index terms associated with a particular treaty.
    - `<item>`
      - Container element for individual index terms associated with the treaty. An <item> element may include the following children:
         - `<name>` (e.g., Maritime)
           - The name of the associated index term.
  - `<relatedDocs>`
    - Container for executive reports associated with the treaty. A `<relatedDocs>` element may include the following children (the data below is taken from <https://api.congress.gov/v3/treaty/116/1>):
      - `<item>`
        - Container element for individual executive reports associated with the treaty. An `<item>` element may include the following children:
          - `<name>` (e.g., Ex. Rept. 116-5)
            - The citation for the associated executive report.
          - `<url>` (e.g., <https://api.congress.gov/v3/committee-report/116/ERPT/5>)
            - A referrer URL to the executive report item in the API. Documentation on committee reports is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeReportEndpoint.md).
  - `<resolutionText>` (e.g., `<![CDATA[<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" lang="en"><head><meta name="meta:creation-date" content="2022/08/03 18:28:08" /><meta name="dc:title" content="[117] TreatyRes. 6 for TreatyDoc. 117 - 3" /><meta name="Creation-Date" content="2022/08/03 18:28:08" /><meta name="dcterms:created" content="2022/08/03 18:28:08" /><meta name="Content-Type" content="application/rtf" /><title>[117] TreatyRes. 6 for TreatyDoc. 117 - 3</title></head><body><p>As approved by the Senate: </p><p><i>Resolved (two-thirds of the Senators present concurring therein),</i></p><p></p><p><b>SECTION 1. SENATE ADVICE AND CONSENT SUBJECT TO DECLARATIONS AND CONDITIONS.</b></p><p></p><p>The Senate advises and consents to the ratification of the Protocols to the North Atlantic Treaty of 1949 on the Accession of the Republic of Finland and the Kingdom of Sweden, which were signed on July 5, 2022, by the United States of America and other parties to the North Atlantic Treaty of 1949 (Treaty Doc. 117-3), subject to the declarations of section 2 and the condition of section 3.</p><p><b>SEC. 2. DECLARATIONS.</b></p><p></p><p>The advice and consent of the Senate under section 1 is subject to the following declarations:</p><p>(1)Reaffirmation That United States Membership in NATO Remains a Vital National Security Interest of the United States.- The Senate declares that-</p><p>(A)for more than 70 years the North Atlantic Treaty Organization (NATO) has served as the preeminent organization to defend the countries in the North Atlantic area against all external threats;</p><p>(B)through common action, the established democracies of North America and Europe that were joined in NATO persevered and prevailed in the task of ensuring the survival of democratic government in Europe and North America throughout the Cold War;</p><p>(C)NATO enhances the security of the United States by embedding European states in a process of cooperative security planning and by ensuring an ongoing and direct leadership role for the United States in European security affairs;</p><p>(D)the responsibility and financial burden of defending the democracies of Europe and North America can be more equitably shared through an alliance in which specific obligations and force goals are met by its members;</p><p>(E)the security and prosperity of the United States is enhanced by NATO's collective defense against aggression that may threaten the security of NATO members; and</p><p>(F)United States membership in NATO remains a vital national security interest of the United States.</p><p>(2)Strategic Rationale for NATO Enlargement.- The Senate declares that-</p><p>(A)the United States and its NATO allies face continued threats to their stability and territorial integrity;</p><p>(B)an attack against Finland or Sweden, or the destabilization of either arising from external subversion, would threaten the stability of Europe and jeopardize United States national security interests;</p><p>(C)Finland and Sweden, having established democratic governments and having demonstrated a willingness to meet the requirements of membership, including those necessary to contribute to the defense of all NATO members, are in a position to further the principles of the North Atlantic Treaty and to contribute to the security of the North Atlantic area; and</p><p>(D)extending NATO membership to Finland and Sweden will strengthen NATO, enhance stability in Europe, and advance the interests of the United States and its NATO allies.</p><p>(3)Support for NATO's Open Door Policy.- The policy of the United States is to support NATO's Open Door Policy that allows any European country to express its desire to join NATO and demonstrate its ability to meet the obligations of NATO membership.</p><p>(4)Future Consideration of Candidates for Membership in NATO.-</p><p>(A)Senate Finding.-The Senate finds that the United States will not support the accession to the North Atlantic Treaty of, or the invitation to begin accession talks with, any European state (other than Finland and Sweden), unless-</p><p>(i)the President consults with the Senate consistent with Article II, section 2, clause 2 of the Constitution of the United States (relating to the advice and consent of the Senate to the making of treaties); and</p><p>(ii)the prospective NATO member can fulfill all of the obligations and responsibilities of membership, and the inclusion of such state in NATO would serve the overall political and strategic interests of NATO and the United States.</p><p>(B)Requirement for Consensus and Ratification.-The Senate declares that no action or agreement other than a consensus decision by the full membership of NATO, approved by the national procedures of each NATO member, including, in the case of the United States, the requirements of Article II, section 2, clause 2 of the Constitution of the United States (relating to the advice and consent of the Senate to the making of treaties), will constitute a commitment to collective defense and consultations pursuant to Articles 4 and 5 of the North Atlantic Treaty.</p><p>(5)Influence of Non-NATO Members on NATO Decisions.- The Senate declares that any country that is not a member of NATO shall have no impact on decisions related to NATO enlargement.</p><p>(6)Support for 2014 Wales Summit Defense Spending Benchmark.--The Senate declares that all NATO members should spend a minimum of 2 percent of their Gross Domestic Product (GDP) on defense and 20 percent of their defense budgets on major equipment, including research and development, by 2024, as outlined in the 2014 Wales Summit Declaration.</p><p><b>SEC. 3. CONDITION.</b></p><p></p><p>The advice and consent of the Senate under section 1 is subject to the following conditions</p><p>(1)Presidential Certification.-Prior to the deposit of the instrument of ratification, the President shall certify to the Senate as follows:</p><p>(A)The inclusion of Finland and Sweden in NATO will not have the effect of increasing the overall percentage share of the United States in the common budgets of NATO.</p><p>(B)The inclusion of Finland and Sweden in NATO does not detract from the ability of the United States to meet or to fund its military requirements outside the North Atlantic area.</p><p><b>SEC. 4. DEFINITIONS.</b></p><p></p><p>In this resolution:</p><p>(1)NATO Members.-The term &ldquo;NATO members&rdquo; means all countries that are parties to the North Atlantic Treaty.</p><p>(2)Non-NATO Members.-The term &ldquo;non-NATO members&rdquo; means all countries that are not parties to the North Atlantic Treaty.</p><p>(3)North Atlantic Area.-The term &ldquo;North Atlantic Area&rdquo; means the area covered by Article 6 of the North Atlantic Treaty, as applied by the North Atlantic Council.</p><p>(4)North Atlantic Treaty.-The term &ldquo;North Atlantic Treaty&rdquo; means the North Atlantic Treaty, signed at Washington April 4, 1949 (63 Stat. 2241; TIAS 1964), as amended.</p><p>(5)United States Instrument of Ratification.-The term &ldquo;United States instrument of ratification&rdquo; means the instrument of ratification of the United States of the Protocols to the</p><p>North Atlantic Treaty of 1949 on the Accession of the Republic of Finland and the Kingdom of Sweden.</p></body></html>]]>`)
    - The text of the resolution of ratification.
    - Note that the text is encased in CDATA and includes HTML codes.
  - `<topic>` (e.g., International Law and Organization)
    - The assigned topic of the treaty.  
  - `<updateDate>` (e.g., 2022-08-04T02:46:11Z)
    - The date of update on Congress.gov.
  - `<parts>`
    - Container for treaty part information. A `<parts>` element may include the following children (the below data is taken from <https://api.congress.gov/v3/treaty/114/13>):
      - `<count>` (e.g., 2)
        - The number of treaty parts.
      - `<urls>`
        - Container for the referrer URLs to the treaty part items in the API. A `<urls>` element may include the following children:
      - `<item>` (e.g., <https://api.congress.gov/v3/treaty/114/13/B>)
        - A referrer URL to the treaty part item in the API.
 - `<titles>`
    - Container for title information for the treaty. An `<titles>` element may include the following children:
      - `<title>` 
        - The title of the treeaty.
      - `<titleType>` (e.g., https://api.congress.gov/v3/treaty/114/13/B)
        - Type of title (e.g., Treaty- Formal Title)
  - `<actions>`
    - Container for actions on the treaty. An `<actions>` element may include the following children:
      - `<count>` (e.g., 7)
        - The number of actions on the treaty.
      - `<url>` (e.g., <https://api.congress.gov/congress/v3/treaty/117/3/actions>)
        - A referrer URL to the actions level of the treaty API. Click [here](#actions-level) for more information about the actions level.

### Actions Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<actions>` (the example below is based on <https://api.congress.gov/v3/treaty/114/13/A/actions>. While this example is a treaty with parts, the same structure exists for treaties without parts.)

- Parent container for actions on a treaty. An `<actions>` element may include the following children:
  - `<item>`
    - Container for an individual action on a treaty. An `<item>` element is repeatable and may include the following children:
      - `<type>` (e.g., IntroReferral)
        - A short name representing stages or categories of more detailed actions. Most types condense actions into sets. Some types are used for data processing and do not represent Senate processes.
        - Possible values include "Calendars", "Committee", "Discharge", "Floor", and "IntroReferral".
      - `<committee>`
        - Container for committee information. A `<committee>` element may include the following children:
          - `<systemCode>` (e.g., ssfr00)
            - Unique ID value for the committee.
          - `<name>` (e.g., Foreign Relations Committee)
            - The name of the committee.
          - `<url>` (e.g., <https://api.congress.gov/v3/committee/senate/ssfr00>)
            - A referrer URL to the committee item in the API. Documentation for the committee endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeEndpoint.md).
      - `<actionCode>` (e.g, S05120)
        - A Senate-provided action code associated with the action taken on a treaty.
      - `<actionDate>` (e.g., 2016-12-09)
        - The date of action taken on the treaty.
      - `<text>` (e.g., Received in the Senate and referred to the Committee on Foreign Relations by unanimous consent removing the injunction of secrecy.)
        - The text of the action taken on the treaty.

### Committees Level  

`<api-root>`

The `<api-root>` is only present in the XML format.

`<treatyCommittees>` (the example below is based on <https://api.congress.gov/v3/treaty/116/3/committees>.)

- Parent container for committees with activity associated with the treaty. A `<treatyCommittees>` element may include the following children:
  - `<item>`
    - Container for the individual elements associated with a committee taking action on a treaty. An `<item>` element is repeatable and may include the following children:
      - `<url>` (e.g., <https://api.congress.gov/v3/committee/senate/ssfr00>)
        - A referrer URL to the committee item in the API. Documentation for the committee endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeEndpoint.md).
      - `<systemCode>` (e.g, ssfr00)
        - Unique ID value for the committee.
      - `<name>` (e.g, Foreign Relations Committee)
        - The name of the committee or subcommittee.
      - `<chamber>` (e.g., Senate)
        - The chamber where the committee operates. This value will always be set to "Senate".
      - `<type>` (e.g., Standing)
        - The type or status of the committee. This value will always be set to "Standing".
      - `<subcommittees>`
        - Container for subcommittees with activity associated with the nomination.
      - `<activities>`
        - Container for the committee or subcommittee activities associated with the treaty. An `<activities>` element may include the following children:
          - `<item>`
            - Container for a committee or subcommittee activity. An `<item>` element is repeatable and may include the following children:
              - `<name>` (e.g., Referred to)
                - The committee or subcommittee activity.
                - Possible values are "Referred to", "Re-Referred to", "Reported by", and "Discharged from".
              - `<date>` (e.g., 2020-06-18T20:19:22Z)
                - The date of the committee or subcommittee activity.


================================================
File: /Documentation/SenateCommunicationEndpoint.md
================================================
# Senate communication endpoints

## Coverage

Coverage information for Senate communications data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about Senate communications data at [About Senate Executive and Other Communications](https://www.congress.gov/help/senate-communications) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the Senate communications API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/senate-communication/senate_communication).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that Senate communication items at the list level can be filtered down by congress (e.g. 117) and by communication type (e.g. ec) - <https://api.congress.gov/v3/senate-communication/117/ec?api_key>=.

`<api-root>`

The `<api-root>` is only present in the XML format.

`<senateCommunications>`

Parent container for Senate communications. A `<senateCommunications>` element may include the following children:

- `<item>`
  - Container for a Senate communication item. An `<item>` element is repeatable and may include the following children:
    - `<chamber>` (e.g. Senate)
      - The chamber where the communication was received. This value will always be set to "Senate".
    - `<number>` (e.g. 2561)
      - The assigned communication number.
    - `<communicationType>`
      - Container for communication type information. A `<communicationType>` element may include the following children:
        - `<code>` (e.g. EC)
          - The code for the type of communication.
          - Possible values are "EC", "POM", and "PM".
        - `<name>` (e.g. Executive Communication)
          - The name of the type of communication.
          - Possible values are "Executive Communication", "Petition or Memorial", and "Presidential Message".
    - `<congress>` (e.g. 117)
      - The congress during which the communication was received.
      - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
    - `<url>` (e.g. <https://api.congress.gov/v3/senate-communication/117/ec/2561>)
      - A referrer URL to the communication item in the API.

## Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<senate-communication>`

Parent container for a Senate communication item. A `<senate-communication>` element may include the following children:

- `<chamber>` (e.g. Senate)
  - The chamber where the communication was received. This value will always be set to "Senate".
- `<number>` (e.g. 2561)
  - The assigned communication number.
- `<communicationType>`
  - Container for communication type information. A `<communicationType>` element may include the following children:
    - `<code>` (e.g. EC)
      - The code for the type of communication.
      - Possible values are "EC", "POM", and "PM".
    - `<name>` (e.g. Executive Communication)
      - The name of the type of communication.
      - Possible values are "Executive Communication", "Petition or Memorial", and "Presidential Message".
- `<congress>` (e.g. 117)
  - The congress during which the communication was received.
  - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
- `<abstract>` (e.g. A communication from the Board Chairman and Chief Executive Officer, Farm Credit Administration, transmitting, pursuant to law, the Administration's annual report for calendar year 2021; to the Committee on Agriculture, Nutrition, and Forestry.)
  - The abstract text for the communication.
- `<congressionalRecordDate>` (e.g. 2021-11-03)
  - The date the communication was published in the Congressional Record.
- `<committees>`
  - Container for committees associated with the communication. A `<committees>` element may include the following children:
    - `<item>`
      - Container for a single committee associated with the communication. An `<item>` element is repeatable and may include the following children:
        - `<name>` (e.g. Agriculture, Nutrition, and Forestry Committee)
          - The name of the committee.
        - `<referralDate>` (e.g. 2021-11-03)
          - The date the communication was referred to the committee.
        - `<url>` (e.g. <https://api.congress.gov/v3/committee/senate/ssaf00>)
          - A referrer URL to the committee item in the API. Documentation for the committee endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeEndpoint.md).


================================================
File: /Documentation/BoundCongressionalRecordEndpoint.md
================================================
# Bound Congressional Record endpoint

## Coverage

Coverage information for bound Congressional Record data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates).  Read more about Congressional Record data at [About the Congressional Record](https://www.congress.gov/help/congressional-record) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the Congressional Record API and available parameters at [https://api.congress.gov](https://api.congress.gov/#/daily-congressional-record/daily-congressional-record_list).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that bound Congressional Record items can be filtered down to volume by adding /{year}?api_key=[INSERT_KEY], /{year}/{month}?api_key=[INSERT_KEY], or /{year}/{month}/{day}?api_key=[INSERT_KEY] to your search. 

Examples of these searches include:
- /{year}: <https://api.congress.gov/v3/bound-congressional-record/1990?api_key=[INSERT_KEY]>
- /{year}/{month}: <https://api.congress.gov/v3/bound-congressional-record/1990/05?api_key=[INSERT_KEY]>
- /{year}/{month}/{day}: <https://api.congress.gov/v3/bound-congressional-record/1990/05/21?api_key=[INSERT_KEY]>

`<api-root>`

The `<api-root>` is only present in the XML format.

`<boundCongressionalRecord>`

Parent container for Congressional Record issues. A `<boundCongressionalRecord>` element may include the following children:

- `<item>`
  - Container for a bound Congressional Record issue. An `<item>` element may include the following children:
    - `<date>`
      - The bound Congressional Record's date.
    - `<volumeNumber>`
      - The bound Congressional Record's volume number. 
    - `<congress>`
      - The Congress associated with the bound Congressional Record issue.
    - `<SessionNumber>`
      - The session number. Possible values are "1" and "2". 
    - `<UpdateDate>` 
       - The date that the bound Congressional Reord was updated.
    - `<URL>`
      - The URL for the bound Congress Record.

- `<dailyDigest>`
  - Container for a bound Congressional Record's Daily Digest. A `<dailyDigest>` element may include the following children:
    - `<startPage>`
      - The start page for the Daily Digest section.
    - `<endPage>`
      - The end page for the Daily Digest section.
    - `<text>`
      - Container for Daily Digest text. A `<text>` element may include:
        - `<item>`
        - Container for single Daily Digest text. An `<item>` element may include:
           - `<type>`
           - The Daily Digest format type. For example, PDF.
           - `<URL>`
           - The URL for the Daily Digest text.
             
- `<Sections>`
  - Container for a bound Congressional Record's sections. A `<Sections>` element may include the following children:
    - `<item>`
    - Container for a section of a bound Congressional Record. An `<item> ` element may include the following children:
       - `<name> `
       - The name of the bound Congressional Record section. For example, "Senate." 
       - `<startPage>`
       - The start page for the Daily Digest section.
       - `<endPage>`
       - The end page for the Daily Digest section.
       
      




================================================
File: /Documentation/HouseCommunicationEndpoint.md
================================================
# House communication endpoints

## Coverage

Coverage information for House communications data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about House communications data at [About Communications to the House](https://www.congress.gov/help/house-communications) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the House communications API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/house-communication/house_communication).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that House communication items at the list level can be filtered down by congress (e.g. 117) and by communication type (e.g. ec) - <https://api.congress.gov/v3/house-communication/117/ec?api_key>=.

`<api-root>`

The `<api-root>` is only present in the XML format.

`<houseCommunications>`

Parent container for House communications. A `<houseCommunications>` element may include the following children:

- `<item>`
  - Container for a House communication item. An `<item>` element is repeatable and may include the following children:
    - `<chamber>` (e.g. House)
      - The chamber where the communication was received. This value will always be set to "House".
    - `<number>` (e.g. 1)
      - The assigned communication number.
    - `<communicationType>`
      - Container for communication type information. A `<communicationType>` element may include the following children:
        - `<code>` (e.g. EC)
          - The code for the type of communication.
          - Possible values are "EC", "PM", "PT", and "ML".
        - `<name>` (e.g. Executive Communication)
          - The name of the type of communication.
          - Possible values are "Executive Communication", "Presidential Message", "Petition", and "Memorial".
    - `<congressNumber>` (e.g. 115)
      - The congress during which the communication was received.
      - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
    - `<url>` (e.g. <https://api.congress.gov/v3/house-communication/115/ec/1>)
      - A referrer URL to the communication item in the API.

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<house-communication>`

Parent container for a House communication item. A `<house-communication>` element may include the following children:

- `<chamber>` (e.g. House)
  - The chamber where the communication was received. This value will always be set to "House".
- `<number>` (e.g. 1)
  - The assigned communication number.
- `<communicationType>`
  - Container for communication type information. A `<communicationType>` element may include the following children:
    - `<code>` (e.g. EC)
      - The code for the type of communication.
      - Possible values are "EC", "PM", "PT", and "ML".
    - `<name>` (e.g. Executive Communication)
      - The name of the type of communication.
      - Possible values are "Executive Communication", "Presidential Message", "Petition", and "Memorial".
- `<congress>` (e.g. 115)
   - The congress during which the communication was received.
- `<updateDate>` (e.g. 2023-01-22)
   - The date the communication was updated.
  - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
- `<abstract>` (e.g. A letter from the Clerk, U.S. House of Representatives, transmitting a list of reports created by the Clerk, pursuant to Rule II, clause 2(b), of the Rules of the House; (H. Doc. No. 115–4); to the Committee on House Administration and ordered to be printed.)
    - The abstract text for the communication.
- `<congressionalRecordDate>` (e.g. 2017-01-03)
    - The date the communication was published in the Congressional Record.
- `<sessionNumber>` (e.g. 1 or 2)
- `<isRulemaking>` (Y or N value)
- `<committees>`
  - Container for committees associated with the communication. A `<committees>` element may include the following children:
    - `<item>`
      - Container for a single committee associated with the communication. An `<item>` element is repeatable and may include the following children:
        - `<name>` (e.g. House Administration Committee)
          - The name of the committee.
        - `<referralDate>` (e.g. 2017-01-03)
          - The date the communication was referred to the committee.
        - `<systemCode>` (e.g. hsfa00)
          - The assigned code used in Congress.gov for the committee
   - `<matchingRequirements>`
  - Container for matching requirements associated with the communication. A `<matchingRequirements>` element may include the following children:
    - `<item>`
      - Container for a single matching requirement associated with the communication. An `<item>` element is repeatable and may include the following children:
        - `<number>` (e.g. House Administration Committee)
          - The assigned number of the matching requirement.
        - `<URL>` (e.g. https://api.congress.gov/v3/house-communication/115/ec/1)
          - A referrer URL to the communication item in the API.
   - `<reportNature>`
     - The description of the nature of the report.
    - `<submittingAgency>` (e.g. Department of the Treasury)
       - The agency responsible for submitting the report.
    - `<submittingOfficial>`
       - The official responsible for submittnig the report. 
    - `<legalAuthority>`
       - The legal authority responsible for the report. 
    - `<houseDocument>`
  - Container for matching requirements associated with the communication. A `<houseDocument>` element may include the following children:
    - `<item>`
      - Container for a single house document associated with the communication. An `<item>` element is repeatable and may include the following children:
        - `<citation>` 
          - The citation of the house document.
        - `<title>` 
          - The title of the house document.
     


================================================
File: /Documentation/NominationEndpoint.md
================================================
# Nomination endpoints

## Coverage

Coverage information for nominations data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about nominations data at [About Nominations by the U.S. President](https://www.congress.gov/help/nominations) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the nomination API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/nomination/nomination_list).

## A Note on Partitioned Nominations

A presidential nomination (PN) with multiple nominees may be partitioned by the Senate if the nominees follow a different confirmation path. Partitions are identified with a suffix; for example, PN230-1 (114th Congress) and PN230-2 (114th Congress). Searching on a PN number in Congress.gov API, such as PN230, without a partition designation will retrieve all partitions of a partitioned nomination.

## Elements and Descriptions

The section below details available element names, their descriptions, and possible values.

### List Level

Note that nomination items at the list level can be filtered down by congress (e.g. 117) - <https://api.congress.gov/v3/nomination/117/?api_key>=.

`<api-root>`

The `<api-root>` is only present in the XML format.

`<nominations>`

Parent container for nominations. A `<nominations>` element may include the following children:

- `<item>`
  - Container for a nomination. An `<item>` element is repeatable and may include the following children:
    - `<congress>` (e.g. 117)
      - The congress during which the nomination was received.
      - View the [field value list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
    - `<number>` (e.g. 1064)
      - The assigned nomination number.
      - Read more about nomination numbering at [About Nominations by the U.S. President](https://www.congress.gov/help/nominations) on Congress.gov.
    - `<partNumber>`
      - The part number for the nomination. Nominations with multiple nominees may be partitioned if the nominees follow different confirmation paths.
    - `<citation>` (e.g. PN1064)
      - The citation identifying the nomination. PN indicates "Presidential Nomination" and the digits that follow are the nomination's assigned number. If the nomination was partitioned, the citation will include a dash and the part number (e.g. PN78-4).
    - `<description>` (e.g. Lisette Nieves, of New York, to be a Member of the Board of Directors of the Corporation for National and Community Service for a term expiring October 6, 2027. (Reappointment))
      - The description of the nomination.
    - `<receivedDate>` (e.g. 2021-09-13)
      - The date the nomination was received from the President.
    - `<nominationType>`
      - Container for type data for the nomination. A `<nominationType>` element may include the following children:
        - `<isCivilian>` (e.g. True)
          - Flag indicating whether the nomination is for a civilian position.
          - Possible values are "True" or "False".
        - `<isMilitary>` (e.g. False)
          - Flag indicating whether the nomination is for a military nomination.
          - Possible values are "True" or "False".
    - `<latestAction>`
      - Container for the latest action taken on the nomination. A `<latestAction>` element may include the following children:
        - `<actionDate>` (e.g., 2022-07-21)
          - The date of the latest action taken on the nomination.
        - `<text>` (e.g., Confirmed by the Senate by Voice Vote.)
          - The text of the latest action taken on the nomination.
    - `<updateDate>` (e.g. 2022-07-22 04:24:15+00:00)
      - The date of update in Congress.gov.
    - `<url>` (e.g. <https://api.congress.gov/v3/nomination/117/1064>)
      - A referrer URL to the nomination item in the API.
    - `<organization>` (e.g., Corporation for National and Community Service)
      - The name of the organization for which the nomination was submitted.

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<nomination>`

Parent container for the nomination. A `<nomination>` element may contain the following children:

- `<congress>` (e.g. 117)
  - The congress during which the nomination was received.
  - View the [field value list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
- `<number>` (e.g. 1064)
  - The assigned nomination number.
  - Read more about nomination numbering at [About Nominations by the U.S. President](https://www.congress.gov/help/nominations) on Congress.gov.
- `<partNumber>`
  - The part number for the nomination. Nominations with multiple nominees may be partitioned if the nominees follow different confirmation paths.
- `<citation>` (e.g. PN1064)
  - The citation identifying the nomination. PN indicates "Presidential Nomination" and the digits that follow are the nomination's assigned number. If the nomination was partitioned, the citation will include a dash and the part number (e.g. PN78-4).
- `<isPrivileged>` (e.g. True)
  - Flag indicating whether the nomination is privileged and entitled to expedited procedures.
  - Possible values are "True" or "False".
  - Read more about privileged nominations at [About Nominations by the U.S. President](https://www.congress.gov/help/nominations) on Congress.gov.
- `<isList>` (e.g. False)
  - Flag indicating whether the nomination is for the Military, Foreign Service, National Oceanic and Atmospheric Administration (NOAA), or Public Health.
  - Possible values are "True" or "False".
- `<receivedDate>` (e.g., 2021-09-13)
  - The date the nomination was received from the President.
- `<description>` (e.g., Lisette Nieves, of New York, to be a Member of the Board of Directors of the Corporation for National and Community Service for a term expiring October 6, 2027. (Reappointment))
  - The description of the nomination.
- `<executiveCalendarNumber>`
  - Executive calendar number information for the nomination.
- `<authorityDate>` (e.g. 2022-07-21)
  - The date when the Senate granted authority to the Secretary of the Senate to receive nominations during periods of recess or adjournment.
- `<nominees>`
  - Container for nominee position data. A `<nominees>` element may include the following children:
    - `<item>`
      - Container for a nominee position. An `<item>` element is repeatable and may include the following children:
        - `<ordinal>` (e.g. 1)
          - Ordinal used for the display order of positions for a nomination.
        - `<introText>`
          - Introductory text for a nominee position.
        - `<organization>` (e.g. Corporation for National and Community Service)
          - The name of the organization for which the nomination was submitted.
        - `<positionTitle>` (e.g. Member of the Board of Directors of the Corporation for National and Community Service)
          - The title of the position for which the nominee has been nominated.
        - `<division>`
          - The name of the division within the organization for which the nominee has been nominated.
        - `<url>` (e.g. <https://api.congress.gov/v3/nomination/117/1064/1>)
          - A referrer URL to the nominee position level of the nomination API. Click [here](#nominees-level) for more information about the nominee position level.
          - Note that if there are nominees for multiple positions within a nomination, there will be multiple referrer URLs to those nominee position levels. The numbering for the referrer URLs will be sequential (e.g. 1, 2, etc.).
        - `<nomineeCount>` (e.g. 1)
          - The count of nominees for a position.
- `<committees>`
  - Container for committees or subcommittees with activity associated with the nomination. Read more [About Committees and Committee Materials](https://www.congress.gov/help/committee-materials) on Congress.gov.
    - `<count>`
      - The number of committees with activity associated with the nomination.
    - `<url>`
      - A referrer URL to the committees level of the nomination API. Click [here](#committees-level) for more information about the committees level.
- `<latestAction>`
  - Container for the latest action taken by the Senate or the President on the nomination. A `<latestAction>` element may include the following children:
    - `<actionDate>` (e.g. 2022-07-21)
      - The date of the latest action taken on the nomination.
    - `<text>` (e.g. Confirmed by the Senate by Voice Vote)
      - The text of the latest action taken on the nomination.
- `<actions>`
  - Container for actions on the nomination. An `<actions>` element may include the following children:
    - `<count>` (e.g. 6)
      - The number of actions on the nomination. The `<count>` may include actions from the Senate and the President.
    - `<url>` (e.g. <https://api.congress.gov/v3/nomination/117/1064/actions>)
      - A referrer URL to the actions level of the nomination API. Click [here](#actions-level) for more information about the actions level.
- `<hearings>`
  - Container for all printed hearings associated with the nomination. A `<hearings>` element may include the following children (the below data is from <https://api.congress.gov/v3/nomination/116/389>):
    - `<count>` (e.g. 1)
      - The number of printed hearings associated with the nomination.
    - `<url>` (e.g. <https://api.congress.gov/v3/nomination/116/389/hearings>)
      - A referrer URL to the printed hearings level of the nomination API. Click [here](#hearings-level) for more information about the printed hearings level.
- `<updateDate>` (e.g. 2022-07-22 04:25:15+00:00)
  - The date of update in Congress.gov.

### Nominees Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<nominees>`

Parent container for nominees associated with the nomination. A `<nominees>` element may include the following children:

- `<item>`
  - Container for a nominee associated with the nomination. An `<item>` element is repeatable and may include the following children:
    - `<ordinal>` (e.g. 1)
      - Ordinal used for the display order of nominees.
    - `<lastName>` (e.g. Nieves)
      - Last name of a nominee.
      - This element may be populated with a string (the letter 'D' followed by a sequence of numbers)  like 'D016128'. That string is an identification number used for classified nominees.
    - `<firstName>` (e.g. Lisette)
      - The first name of a nominee.
    - `<middleName>`
      - The middle name of a nominee.
    - `<prefix>`
      - The name prefix for a nominee. This may be a military title, like 'Col.'
    - `<suffix>`
      - The name suffix for a nominee. This may suffixes like 'Jr.'
    - `<state>` (e.g. NY)
      - The two-digit postal code abbreviation for the nominee.
    - `<effectiveDate>`
      - The date when the appointment will become effective.
    - `<predecessorName>`
      - The name of the person who previously held the position to which the nominee has been nominated.
    - `<corpsCode>`
      - The corps code assigned by the White House to identify Corps.

### Committees Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<committees>`

Parent container for committees with activity associated with the nomination. A list of committees with an association to data on Congress.gov is available at the [Committee Name History](https://www.congress.gov/help/committee-name-history) page on Congress.gov. A list of current committees is available at [Committees of the U.S. Congress](https://www.congress.gov/committees) on Congress.gov. A `<committees>` element may include the following children:

- `<item>`
  - Container for a committee with activity associated with the nomination. An `<item>` element is repeatable and may include the following children (the below data is from <https://api.congress.gov/v3/nomination/117/1520/committees>):
    - `<url>` (e.g. <https://api.congress.gov/v3/committee/house/sscm00>)
      - A referrer URL to the committee item in the API. Documentation for the committee endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeEndpoint.md).
    - `<systemCode>` (e.g. sscm00)
      - Unique ID value for the committee.
    - `<name>` (e.g. Commerce, Science, and Transportation Committee)
      - The name of the committee.
    - `<chamber>` (e.g. Senate)
      - The chamber where the committee operates. This value will always be set to "Senate".
    - `<type>` (e.g. Standing)
      - The type or status of the committee.
      - Possible values are "Standing", "Select", and "Other".
    - `<subcommittees>`
      - Container for subcommittees with activity associated with the nomination.
    - `<activities>`
      - Container for committee or subcommittee activities associated with the nomination. An `<activities>` element may include the following children:
        - `<item>`
          - Container for a committee or subcommittee activity. An `<item>` element is repeatable and may include the following children:
            - `<name>`
              - The name of the committee or subcommittee activity.
              - Possible values are "Referred to", "Discharged from", "Re-Referred to", "Re-Committed to", and "Reported by".
            - `<date>` (e.g. 2022-01-20T103:53:52Z)
              - The date of the committee or subcommittee activity.

### Actions Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<actions>`

Parent container for all actions taken on the nomination. Actions may come from the Senate or the President. An `<actions>` element may include the following children:

- `<item>`
  - Container for an action taken on the nomination. An `<item>` element is repeatable and may include the following children:
    - `<actionDate>`(e.g. 2022-07-21)
      - The date of action taken on the nomination.
    - `<text>` (e.g. Confirmed by the Senate by Voice Vote.)
      - The text of the action taken on the nomination.
    - `<type>` (e.g. Floor)
      - A short name representing stages or categories of more detailed actions. Most types condense actions into sets. Some types are used for data processing and do not represent Senate processes.
      - Possible values are "IntroReferral", "Committee", "Calendars", and "Floor".
    - `<actionCode>` (e.g. S05310)
      - A Senate-provided code associated with the action taken on the nomination.
    - `<committees>`
      - Container for committees associated with the action. A `<committees>` element may include the following children:
        - `<item>`
          - Container for a committee associated with the action. An `<item>` element is repeatable and may include the following children:
            - `<url>`
              - A referrer URL to the committee item in the API. Documentation for the committee endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeEndpoint.md).
            - `<systemCode>`
              - Unique ID value for the committee.
            - `<name>`
              - The name of committee.

### Hearings Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<hearings>`

Parent container for printed hearings associated with the nomination. A `<hearings>` element may include the following children (the below data is from <https://api.congress.gov/v3/nomination/116/389/hearings>):

- `<item>`
  - Container for a printed hearing on the nomination. An `<item>` element is repeatable and may include the following children:
    - `<chamber>` (e.g. Senate)
      - The chamber where the hearing associated with the nomination took place. This value will always be set to "Senate".
    - `<number>` (e.g. 38)
      - The number for the printed hearing.
    - `<partNumber>`
      - The part number for the hearing, if printed in parts.
    - `<citation>` (e.g. S.Hrg. 116-38)
      - The printed hearing citation.
    - `<jacketNumber>` (e.g. 37106)
      - The jacket number, as present on the paper and PDF formats of the printed hearing.
    - `<errataNumber>`
      - If errata, the printed hearing's errata number.
      - Read more [about errata](https://www.congress.gov/help/legislative-glossary#glossary_errata) on Congress.gov.
    - `<date>` (e.g. 2019-06-05)
      - The date when the hearing took place.


================================================
File: /Documentation/SummariesEndpoint.md
================================================
# Summaries endpoints

## Coverage

Coverage information for bill summaries data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). By default, only bill summaries published in the last day are available from this endpoint unless "fromDateTime" and/or "toDateTime" parameters are added to the API request (read more about those parameters in the OpenAPI Specification, linked below; however, all bill summaries published for bills available on Congress.gov can be found at the [bill endpoint](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/BillEndpoint.md#summaries-level).

## OpenAPI Specification

View OpenAPI Specification on the summaries API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/summaries/bill_summaries_all).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that bill summary items at the list level can be filtered down by congress (e.g., 117) and by bill type (e.g., hr) - <https://api.congress.gov/v3/summaries/117/hr?api_key>=.

`<api-root>`

The `<api-root>` is only present in the XML format.

`<summaries>`

 Parent container for bill summaries. A `<summaries>` element may include the following children:

- `<summary>`
  - Container for an individual bill summary. A `<summary>` element is repeatable and may include the following children:
    - `<bill>`
      - Container for the associated bill to the summary. A `<bill>` element may include the following children:
        - `<congress>` (e.g., 117)
          - The congress during which a bill or resolution was introduced or submitted.
          - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
        - `<type>` (e.g., HR)
          - The type of bill or resolution.
          - Possible values are "HR", "S", "HJRES", "SJRES", "HCONRES", "SCONRES", "HRES", and "SRES".
        - `<originChamber>` (e.g., House)
          - The chamber of origin where a bill or resolution was introduced or submitted.
          - Possible values are "House" and "Senate".
        - `<originChamberCode>` (e.g., H)
          - The code for the chamber of origin where the bill or resolution was introduced or submitted.
          - Possible values are "H" and "S".
        - `<number>` (e.g., 8432)
          - The assigned bill or resolution number.
        - `<url>` (e.g., <https://api.congress.gov/v3/bill/117/hr/8432>)
          - A referrer URL to the bill or resolution item in the API. Documentation for the bill endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/BillEndpoint.md).
        - `<title>` (e.g., Beagle Brigade Act of 2022)
          - The display title for the bill or resolution on Congress.gov.
        - `<updateDateIncludingText>` (e.g., 2022-09-29T07:15:39Z)
          - The date of update for the bill on Congres.gov, which includes updates to the bill's text.
    - `<text>` (e.g., `<![CDATA[ <p><strong>Beagle Brigade Act of 2022</strong></p> <p>This bill provides statutory authority for the National Detector Dog Training Center that is operated by the Animal and Plant Health Inspection Service of the Department of Agriculture. The center trains dogs to inspect passenger baggage, cargo, mailed packages, and vehicles to detect foreign pests and diseases that threaten domestic agriculture and natural resources.</p> ]]>`>
      - The text of the bill summary.
      - Note that the bill summary text is encased in CDATA and contains HTML codes. The HTML codes may not be valid (see [#2](https://github.com/LibraryOfCongress/api.congress.gov/issues/2)); efforts are underway to improve the validity of the HTML codes.
    - `<actionDate>` (e.g., 2022-05-16)
      - The date of the action associated with the bill summary.
    - `<updateDate>` (e.g., 2022-08-18T17:00:44Z)
      - The date of update on Congress.gov.
    - `<currentChamber>` (e.g., House)
      - The chamber that took the action associated with the bill summary.
      - Possible values are "House" and "Senate".
    - `<currentChamberCode>` (e.g., H)
      - The code for the chamber that took the action associated with the bill summary.
      - Possible values are "H" and "S".
    - `<actionDesc>` (e.g., Introduced in House)
      - The description of the action associated with the bill summary.
    - `<versionCode>` (e.g., 00)
      - The internal code used by CRS to tag its bill summaries according to the action associated with the bill summary.
      - Click [here](#bill-summary-version-codes-action-descriptions-and-chamber) for a list of codes. Note that the version codes used have varied over time.  
    - `<lastSummaryUpdateDate>` (e.g., 2022-08-18T16:46:01Z)
      - The date the bill summary was last updated. This date also reflects the date and time when a bill summary is re-published.

#### Bill summary version codes, action descriptions, and chamber

| versionCode | actionDesc | chamber |
| ----------- | ---------- | ------- |
| 00 | Introduced in House | House |
| 00 | Introduced in Senate | Senate |
| 01 | Reported to Senate with amendment(s) | Senate |
| 02 | Reported to Senate amended, 1st committee reporting | Senate |
| 03 | Reported to Senate amended, 2nd committee reporting | Senate |
| 04 | Reported to Senate amended, 3rd committee reporting | Senate |
| 07 | Reported to House | House |
| 08 | Reported to House, Part I | House |
| 09 | Reported to House, Part II | House |
| 12 | Reported to Senate without amendment, 1st committee reporting | Senate |
| 13 | Reported to Senate without amendment, 2nd committee reporting | Senate |
| 17 | Reported to House with amendment(s) | House |
| 18 | Reported to House amended, Part I | House |
| 19 | Reported to House amended Part II | House |
| 20 | Reported to House amended, Part III | House |
| 21 | Reported to House amended, Part IV | House |
| 22 | Reported to House amended, Part V | House |
| 25 | Reported to Senate | Senate |
| 28 | Reported to House without amendment, Part I | House |
| 29 | Reported to House without amendment, Part II | House |
| 31 | Reported to House without amendment, Part IV | House |
| 33 | Laid on table in House | House |
| 34 | Indefinitely postponed in Senate | Senate |
| 35 | Passed Senate amended | Senate |
| 36 | Passed House amended | House |
| 37 | Failed of passage in Senate | Senate |
| 38 | Failed of passage in House | House |
| 39 | Senate agreed to House amendment with amendment | Senate |
| 40 | House agreed to Senate amendment with amendment | House |
| 43 | Senate disagreed to House amendment | Senate |
| 44 | House disagreed to Senate amendment | House |
| 45 | Senate receded and concurred with amendment | Senate |
| 46 | House receded and concurred with amendment | House |
| 47 | Conference report filed in Senate | Senate |
| 48 | Conference report filed in House | House |
| 49 | Public Law | |
| 51 | Line item veto by President | |
| 52 | Passed Senate amended, 2nd occurrence | Senate |
| 53 | Passed House | House |
| 54 | Passed House, 2nd occurrence | House |
| 55 | Passed Senate | Senate |
| 56 | Senate vitiated passage of bill after amendment | Senate |
| 58 | Motion to recommit bill as amended by Senate | Senate |
| 59 | House agreed to Senate amendment | House |
| 60 | Senate agreed to House amendment with amendment, 2nd occurrence | Senate |
| 62 | House agreed to Senate amendment with amendment, 2nd occurrence | House |
| 66 | House receded and concurred with amendment, 2nd occurrence | House |
| 70 | House agreed to Senate amendment without amendment | House |
| 71 | Senate agreed to House amendment without amendment | Senate |
| 74 | Senate agreed to House amendment | Senate |
| 77 | Discharged from House committee | House |
| 78 | Discharged from Senate committee | Senate |
| 79 | Reported to House without amendment | House |
| 80 | Reported to Senate without amendment | Senate |
| 81 | Passed House without amendment | House |
| 82 | Passed Senate without amendment | Senate |
| 83 | Conference report filed in Senate, 2nd conference report | Senate |
| 86 | Conference report filed in House, 2nd conference report | House |
| 87 | Conference report filed in House, 3rd conference report | House |


================================================
File: /Documentation/AmendmentEndpoint.md
================================================
# Amendment endpoints

## Coverage

Coverage information for amendment data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates) on Congress.gov. Read more [about amendments](https://www.congress.gov/help/legislative-glossary#glossary_amendment) on Congress.gov. 

## OpenAPI Specification

View OpenAPI Specification on the amendment API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/amendments/Amendment).

## Elements and Descriptions

### List Level

Note that amendment items at the list level can be filtered down by congress and then by amendment type (e.g. <https://api.congress.gov/v3/amendment/117/SAMDT?api_key>=).

`<api-root>`

The `<api-root>` is only present in the XML format.

`<amendments>`

Parent container for amendments. An `<amendments>` element may include the following children:

- `<amendment>`
  - Container for an amendment. An `<amendment>` element may include the following children:
    - `<number>` (e.g. 2137)
      - The assigned amendment number.
    - `<description>`
      - The amendment's description.
      - Only House amendments will have this element populated.
    - `<purpose>` (e.g. In the nature of a substitute.)
      - The amendment's purpose.
      - House amendments and proposed Senate amendments may have this element populated.
    - `<congress>` (e.g. 117)
      - The congress during which an amendment was submitted or offered.
    - `<type>` (e.g. SAMDT)
      - The type of amendment.
      - Possible values are "HAMDT", "SAMDT", and "SUAMDT". Note that the "SUAMDT" type value is only available for the 97th and 98th Congresses.
    - `<latestAction>`
      - Container for the latest action taken on the amendment. A `<latestAction>` element may include the following children:
        - `<actionDate>` (e.g. 2021-08-08)
          - The date of the latest action taken on the amendment.
        - `<text>` (e.g. Amendment SA 2137 agreed to in Senate by Yea-Nay Vote. 69 - 28. Record Vote Number: 312.)
          - The text of the latest action taken on the amendment.
        - `<actionTime>`
          - The time of the latest action taken on the amendment.
          - Certain actions taken by the House contain this element.
    - `<url>` (e.g. <https://api.congress.gov/v3/amendment/117/samdt/2137>)
      - The referrer URL to the amendment item in the API.

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<amendment>`

Parent container for an amendment. An `<amendment>` element may include the following children:

- `<number>` (e.g. 2137)
  - The assigned amendment number.
- `<description>`
  - The amendment's description.
  - Only House amendments will have this element populated.
- `<purpose>` (e.g. In the nature of a substitute.)
  - The amendment's purpose.
  - House amendments and proposed Senate amendments may have this element populated.
- `<congress>` (e.g. 117)
  - The congress during which an amendment was submitted or offered.
- `<type>` (e.g. SAMDT)
  - The type of amendment.
  - Possible values are "HAMDT", "SAMDT", and "SUAMDT". Note that the "SUAMDT" type value is only available for the 97th and 98th Congresses.
- `<latestAction>`
  - Container for the latest action taken on the amendment. A `<latestAction>` element may include the following children:
    - `<actionDate>` (e.g. 2021-08-08)
      - The date of the latest action taken on the amendment.
    - `<text>` (e.g. Amendment SA 2137 agreed to in Senate by Yea-Nay Vote. 69 - 28. Record Vote Number: 312.)
      - The text of the latest action taken on the amendment.
    - `<actionTime>`
      - The time of the latest action taken on the amendment.
      - Certain actions taken by the House contain this element.
- `<sponsors>`
  - Container for the sponsor of the amendment. A `<sponsors>` element may include the following children:
    - `<item>`
      - Container for a single sponsor of the amendment. An `<item>` element may include the following children:
        - `<bioguideId>` (e.g. S001191)
          - The unique identifier for the amendment's sponsor, as assigned in the [Biographical Directory of the United States Congress, 1774-Present](https://bioguide.congress.gov/).
          - View a [field values list of Bioguide identifiers](https://www.congress.gov/help/field-values/member-bioguide-ids) for current and former members in Congress.gov.
        - `<fullName>` (e.g. Sen. Sinema, Kyrsten [D-AZ])
          - The display name of the amendment's sponsor.
        - `<firstName>` (e.g. Kyrsten)
          - The first name of the amendment's sponsor.
        - `<middleName>`
          - The middle name or initial of the amendment's sponsor.
        - `<lastName>`(e.g. Sinema)
          - The last name of the amendment's sponsor.
        - `<party>` (e.g. D)
          - The party code of the amendment's sponsor.
        - `<state>` (e.g. AZ)
          - A two-letter abbreviation for the state, territory, or district represented by the amendment's sponsor.
        - `<url>` (e.g. <https://api.congress.gov/v3/member/S001191>)
          - A referrer URL to the member item in the API. Documentation for the member endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/MemberEndpoint.md).
        - `<district>`
          - The congressional district that the amendment's sponsor represents.
          - Note that this element will be empty for Senate sponsors and will be "0" for states, territories, or districts where there is only one congressional district.
- `<cosponsors>`
  - Container for any cosponsors of the amendment. Only Senate amendments may have this element populated.
  - A `<cosponsors>` element may include the following children (the below counts are taken from <https://api.congress.gov/v3/amendment/117/samdt/3892>):
    - `<countIncludingWithdrawnCosponsors>` (e.g. 2)
      - The total number of cosponsors of the amendment, including any withdrawn cosponsors.
    - `<count>` (e.g. 1)
      - The current number of cosponsors of the amendment, not including any withdrawn cosponsors.
    - `<url>` (e.g. <https://api.congress.gov/v3/amendment/117/samdt/3892/cosponsors>)
      - A referrer URL to the cosponsors level of the amendment API. Click [here](#cosponsors-level) for more information about the cosponsors level.
- `<proposedDate>` (e.g. 2021-08-01T04:00:00Z)
  - The date the amendment was proposed on the floor.
  - This element will only be populated for proposed Senate amendments.
- `<submittedDate>` (e.g. 2021-08-01T04:00:00Z)
  - The date the amendment was submitted or offered.
- `<chamber>` (e.g. Senate)
  - The chamber in which the amendment was submitted or offered.
- `<amendedBill>`
  - Container for the bill amended by the amendment. An `<amendedBill>` element may include the following children:
    - `<congress>` (e.g. 117)
      - The congress during which the bill or resolution was introduced or submitted.
    - `<type>` (e.g. HR)
      - The type of bill or resolution.
      - Possible values are "HR", "S", "HJRES", "SJRES", "HCONRES", "SCONRES", "HRES", and "SRES".
    - `<originChamber>` (e.g. House)
      - The chamber of origin where a bill or resolution was introduced or submitted.
      - Possible values are "House" and "Senate".
    - `<originChamberCode>` (e.g. H)
      - The code for the chamber of origin where the bill or resolution was introduced or submitted.
      - Possible values are "H" and "S".
    - `<number>` (e.g. 3684)
      - The assigned bill or resolution number.
    - `<url>` (e.g. <https://api.congress.gov/v3/bill/117/hr/3684>)
      - A referrer URL to the bill or resolution item in the API. Documentation for the bill endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/BillEndpoint.md).
    - `<title>` (e.g. Infrastructure Investment and Jobs Act)
      - The display title for the bill or resolution on Congress.gov.
- `<amendedAmendment>`
  - Container for the amendment amended by the amendment. An `<amendedAmendment>` element may include the following children (the below amendment data is taken from <https://api.congress.gov/v3/amendment/117/samdt/2564>) :
    - `<number>` (e.g. 2137)
      - The assigned amendment number.
    - `<description>`
      - The amendment's description.
      - Only House amendments will have this element populated.
    - `<purpose>` (e.g. In the nature of a substitute.)
      - The amendment's purpose.
      - House amendments and proposed Senate amendments may have this element populated.
    - `<congress>` (e.g. 117)
      - The congress during which an amendment was submitted or offered.
    - `<type>` (e.g. SAMDT)
      - The type of amendment.
      - Possible values are "HAMDT", "SAMDT", and "SUAMDT". Note that the "SUAMDT" type value is only available for the 97th and 98th Congresses.
    - `<url>` (e.g. <https://api.congress.gov/v3/amendment/117/samdt/2137>)
      - A referrer URL to the amendment item in the API.
- `<amendmentsToAmendment>`
  - Container for amendments to the amendment. An `<amendmentsToAmendment>` element may contain the following children:
    - `<count>` (e.g. 507)
      - The number of amendments to the amendment.
    - `<url>` (e.g. <https://api.congress.gov/v3/amendment/117/samdt/2137/amendments>)
      - A referrer URL to the amendment to amendments level of the amendment API. Click [here](#amendments-to-amendment-level) for more information about the amendments to amendments level.
- `<notes>`
  - Container for notes attached to the amendment on Congress.gov. The note may contain supplemental information about the amendment that users may find helpful. Read more [about notes](https://www.congress.gov/help/legislative-glossary#glossary_notes) on Congress.gov.
  - A  `<notes>` element may include the following children:
    - `<item>`
      - Container for a note. An `<item>` element may include the following children:
        - `<text>` (e.g. `<![CDATA[ The Senate agreed to the amendment on 12/5/2016, then vitiated its adoption on 12/5/2016, then agreed to the amendment on 12/10/2016. ]]>`)
          - The text of the note on Congress.gov (from <https://api.congress.gov/v3/amendment/114/samdt/5129>).
          - Note that the text is encased in CDATA.
- `<amendedTreaty>`
  - Container for the treaty amended by the amendment. An `<amendedTreaty>` element may contain the following children (the below treaty data is taken from <https://api.congress.gov/v3/amendment/117/samdt/2137>):
    - `<congress>` (e.g. 116)
      - The congress during which a treaty was submitted.
    - `<treatyNumber>` (e.g. 1)
      - The assigned treaty number.
    - `<url>` (e.g. <https://api.congress.gov/v3/treaty/116/1>)
      - A referrer URL to the treaty item in the API. Documentation for the treaty endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/TreatyEndpoint.md).
- `<actions>`
  - Container for actions on the amendment. An `<actions>` element may include the following children:
    - `<count>` (e.g. 19)
      - The number of actions on the amendment. A `<count>` element may include actions from the House, Senate, and Library of Congress.
    - `<url>` (e.g. <https://api.congress.gov/v3/amendment/117/samdt/2137/actions>)
      - A referrer URL to the actions level of the amendment API. Click [here](#actions-level) for more information about the actions level.

## Actions Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<actions>`

Parent container for all actions taken on an amendment. Actions may come from the House, Senate, or Library of Congress. An `<actions>` element may include the following children:

- `<item>`
  - Container for an action taken on an amendment. An `<item>` element is repeatable and may include the following children:
    - `<actionDate>` (e.g. 2021-08-08)
      - The date of the action taken on an amendment.
    - `<actionTime>`
      - The time of the action taken on an amendment.
      - Certain actions taken by the House contain this element.
    - `<text>` (e.g. Amendment SA 2137 agreed to in Senate by Yea-Nay Vote. 69 - 28. Record Vote Number: 312.)
      - The text of the action taken on an amendment.
    - `<type>` (e.g. Floor)
      - A short name representing legislative process stages or categories of more detailed actions. Most types condense actions into sets. Some types are used for data processing and do not represent House or Senate legislative process activities.
      - Possible values are "Committee", "Floor", "IntroReferral", "ResolvingDifferences", and "NotUsed".
    - `<actionCode>`
      - An action code associated with the action taken on an amendment.
      - The `<actionCode>` element will be present only for actions where the `<sourceSystem>` is 2 (House) or 9 (Library of Congress).
        - [Action Codes](https://www.congress.gov/help/field-values/action-codes) is an authoritative list of values where the `<sourceSystem>` is 9 (Library of Congress).
        - An authoritative list of values where the `<sourceSystem>` is 2 (House) does not exist.
      - Various code sets are used by multiple systems in the House, Senate, and Library of Congress by legislative clerks and data editors for functions independent of this data set. As new codes and systems were developed, there was no coordinated effort to retroactively apply new codes to old records. Many codes are concatenated with other codes or elements or utilize free text. Codes in one set may be redundant with a different code in another code set. Additionally, some codes may have been used and re-used over the years for different purposes further complicating the ability to create an authoritative list. View the original code set of [U.S. Congress legislative status steps](http://www.loc.gov/pictures/resource/ppmsca.33996/).
    - `<sourceSystem>`
      - Container for the source system where the action was entered. A `<sourceSystem>` element may include the following children:
        - `<code>` (e.g. 0)
          - A code for the source system that entered the action.
          - Possible values are "0", "1", "2", or "9".
          - "0" is for Senate, "1" and "2" are for House, and "9" is Library of Congress.
        - `<name>` (e.g. Senate)
          - The name of the source system that entered the action.
          - Possible values are "Senate", "House committee actions", "House floor actions", and "Library of Congress".
    - `<committees>`
      - Container for committees associated with the action. A `<committees>` element may include the following children:
        - `<item>`
          - Container for a committee associated with the action. An `<item>` element is repeatable and may include the following children:
            - `<url>`
              - A referrer URL to the committee or subcommittee in the API. Documentation for the committee endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeEndpoint.md).
            - `<systemCode>`
              - Unique ID value for the committee or subcommittee.
            - `<name>`
              - The name of the committee or subcommittee associated with the action.
    - `<recordedVotes>`
      - Container for recorded (roll call) votes associated with the action. Read more [about roll call votes]( https://www.congress.gov/help/legislative-glossary#glossary_rollcallvote) on Congress.gov. More information can also be found at the [Roll Call Votes by the U.S. Congress](https://www.congress.gov/roll-call-votes) and [Votes in the House and Senate](https://www.congress.gov/help/votes-in-the-house-and-senate) pages on Congress.gov.
        - A `<recordedVotes>` element may include the following children:
          - `<recordedVote>`
            - Container for a recorded (roll call) vote associated with the action. A `<recordedVote>` element may include the following children:
              - `<rollNumber>` (e.g. 312)
                - The recorded (roll call) vote number.
              - `<url>` (e.g. <https://www.senate.gov/legislative/LIS/roll_call_votes/vote1171/vote_117_1_00312.xml>)
                - The url to the recorded (roll call) vote on [Senate.gov](https://www.senate.gov/legislative/votes_new.htm) or [Clerk.House.gov](https://clerk.house.gov/Votes).
              - `<chamber>` (e.g. Senate)
                - The chamber where the recorded (roll call) vote took place.
                - Possible values are "House" and "Senate".
              - `<congress>` (e.g. 117)
                - The congress during which the recorded (roll call) vote took place.
              - `<date>` (e.g. 2021-08-09T00:45:48Z)
                - The date of the recorded (roll call) vote.
              - `<sessionNumber>` (e.g. 1)
                - The session of congress during which the recorded (roll call) vote took place.

## Amendments To Amendment Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<amendments>`

Parent container for all amendments to the amendment. An `<amendments>` element may include the following children:

- `<amendment>`
  - Container for an amendment to the amendment. An `<amendment>` element is repeatable and may include the following children:
    - `<number>` (e.g. 2300)
      - The assigned amendment number.
    - `<description>`
      - The amendment's description.
      - Only House amendments will have this element populated.
    - `<purpose>` (e.g. To designate additional high priority corridors on the National Highway system.)
      - The amendment's purpose.
      - House amendments and proposed Senate amendments may have this element populated.
    - `<congress>` (e.g. 117)
      - The congress during which an amendment was submitted or offered.
    - `<type>` (e.g. SAMDT)
      - The type of amendment.
      - Possible values are "HAMDT", "SAMDT", and "SUAMDT". Note that the "SUAMDT" type value is only available for the 97th and 98th Congresses.
    - `<latestAction>`
      - Container for the latest action taken on the amendment. A `<latestAction>` element may include the following children:
        - `<actionDate>` (e.g. 2021-08-03)
          - The date of the latest action taken on the amendment.
        - `<actionTime>`
          - The time of the latest action taken on the amendment.
          - Certain actions taken by the House contain this element.
        - `<text>` (e.g. Amendment SA 2300 agreed to in Senate by Voice Vote.)
          - The text of the latest action taken on the amendment.
        - `<url>` (e.g. <https://api.congress.gov/v3/amendment/117/samdt/2300>)
          - A referrer URL to the amendment item in the API.

## Cosponsors Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<cosponsors>`

Parent container for cosponsors of an amendment. Read more [about cosponsors](https://www.congress.gov/help/legislative-glossary#glossary_cosponsor) on Congress.gov. Only Senate amendments will have this deeper level. A `<cosponsors>` element may include the following children:

- `<item>`
  - Container for a cosponsor of an amendment. An `<item>` element is repeatable and may include the following children:
    - `<bioguideId>` (e.g. P000449)
      - The unique identifier for the amendment cosponsor, as assigned in the [Biographical Directory of the United States Congress, 1774-Present](http://bioguide.congress.gov/).
      - View a [field values list of Bioguide identifiers](https://www.congress.gov/help/field-values/member-bioguide-ids) for current and former members in Congress.gov.
    - `<fullName>` (e.g. Sen. Portman, Rob [R-OH])
      - The display name for the amendment cosponsor.
    - `<firstName>` (e.g. Rob)
      - The first name of the amendment cosponsor.
    - `<middleName>`
      - The middle name or initial of the amendment cosponsor.
    - `<lastName>` (e.g. Portman)
      - The last name of the amendment cosponsor.
    - `<party>` (e.g. R)
      - The party code of the amendment cosponsor.
      - Possible values are "D", "R", "I", "ID", and "L".
    - `<state>` (e.g. OH)
      - A two-letter abbreviation for the state, territory, or district represented by the amendment cosponsor.
    - `<url>` (e.g. <https://api.congress.gov/v3/member/P000449>)
      - A referrer URL to the member item in the API. Documentation for the member endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/MemberEndpoint.md).
    - `<sponsorshipDate>` (e.g. 2021-08-01)
      - The date the member became a cosponsor of the amendment.
    - `<isOriginalCosponsor>` (e.g. True)
      - A designation that the member is an original or additional cosponsor of the amendment. If the member cosponsored the amendment on the date of its submission, then this value will be "True". If the member cosponsored the amendment after its date of submission, then this value will be "False".
      - Possible values are "True" or "False".
    - `<sponsorshipWithdrawnDate>`
      - The date the cosponsor withdrew their cosponsorship of amendment.
- `<pagination>` (from <https://api.congress.gov/v3/amendment/117/samdt/3892>)
  - `<count>` (e.g. 1)
    - The current count of cosponsors of the amendment, not including any withdrawn cosponsors.
  - `<countIncludingWithdrawnCosponsors>` (e.g. 2)
    - The total number of cosponsors of the amendment, including any withdrawn cosponsors.
   
      
## Text Level

Note: Full text of Senate submitted amendments is displayed and searchable on Congress.gov for the 117th Congress forward.  Links to text in the Congressional Record are provided for Senate amendments prior to the 117th Congress and for House amendments.  See [About the Congressional Record](https://www.congress.gov/help/congressional-record) to learn more about searching the Congressional Record. Not all House amendments from the 117th Congress forward have text granules available at this time. 

`<api-root>`

The `<api-root>` is only present in the XML format.

`<textVersions>`

Parent container for text versions of an amendment. Only Senate amendments and some House amendments from the 117th Congress foward will have this deeper level. A `<textVersions>` element may include the following children:

- `<item>`
  - Container for text versions of an amendment. An `<item>` element is repeatable and may include the following children:
    - `<type>`
      - The type of the amendment. For example, "Submitted" or "Modified".
    - `<date>` 
      - The date of the amendment text.
    - `<formats>` (e.g. Rob)
      - Container for amendment text format types. A `<formats>` element is repeateable and may include the following children:
        - `<item>`
            - Container for format items. An `<item>` element is repeatable and may include the following children:
              - `<URL>`
                - URL for the amendment text version.
              - `<type>`
                - The format type. For example, "PDF" or "HTML".
- `<pagination>`
  - `<count>` (e.g. 1)
    - The current count of text versions of the amendment.


================================================
File: /Documentation/MemberEndpoint.md
================================================
# Member endpoints

## Coverage

Coverage information for member data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about member data at [About Congressional Member Profiles](https://www.congress.gov/help/members) on Congress.gov. Vacancies and changes to membership in the House of Representatives can be found at [current vacancies page](https://clerk.house.gov/Members#Vacancies) on the Office of the Clerk website. 

## OpenAPI Specification

View OpenAPI Specification on the member API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/member/member_list).

## A note on filtering members by Congress
When calling for member data from prior congresses using the /member/congress/{congress} filters, please use 'currentMember=False' in your call to get the most complete data. An example API request is: https://api.congress.gov/v3/member/congress/117?currentMember=false&api_key=[INSERT_KEY]

## A note on filtering members by Congress, state, and district
There are instances where a member has been redistricted but previously represented the district you are generating an API request for and, thus, appears in the returned data. If you are looking for ONLY the current member of a particular district, please use the `currentMember=True` filter to get the most accurate results (e.g., https://api.congress.gov/v3/member/congress/118/TX/15?currentMember=true&api_key=[INSERT_KEY]).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that member items at the list level cannot be filtered (<https://api.congress.gov/v3/member?api_key>=).

`<api-root>`

The `<api-root>` is only present in the XML format.

`<members>`

Parent container for all member entries. A `<members>` element may include the following children:

- `<member>`
  - Container for an individual member’s entry.  A `<member>` element may include the following children:
    - `<bioguideID>` (e.g., L000174)
      - The unique ID value that originates in the [Biographical Directory of the United States Congress, 1774-Present](https://bioguide.congress.gov/).
      - View a [field values list of Bioguide identifiers](https://www.congress.gov/help/field-values/member-bioguide-ids) for current and former members in Congress.gov.
    - `<state>` (e.g., Vermont)
      - The state represented by the member.
    - `<partyName>`  (e.g., Democrat)
      - The political party of the member.
      - Possible values are "Democratic", "Independent", "Independent Democrat", "Libertarian", or "Republican".
    - `<district>`  
      - The Congressional district represented by the member (exclusive to House). The value of zero indicates the state, district or territory has only one member in the House.
    - `<name>`  (e.g.,  Leahy, Patrick J.)
      - The name of the member in last-name-first order.
  - `<terms>`
  - Container of a member’s terms of service in chronological order. A `<terms>` element may include the following child, which is repeatable:
    - `<item>`
      - Container for the member’s service in an individual Congress. An `<item>` element is repeatable and may include the following children:
        - `<chamber>` (e.g., Senate)
          - The chamber the member served in.
          - Possible values are "Senate" and "House of Representatives".
        - `<startYear>` (e.g., 1975)
          - The year in which the member began serving in the designated chamber.
        - `<endYear>` (e.g., 1990)
          - The year in which the member ceased serving in the designated chamber.
    - `<url>`  (e.g., <https://api.congress.gov/v3/member/L000174>)
      - A referrer URL to the member item in the API.
    - `<depiction>`
      - Container for the member’s current official portrait. The `<depiction>` element may include the following children:
        - `<imageUrl>` (e.g. <https://www.congress.gov/img/member/l000174_200.jpg>)
          - The member's current portrait on Congress.gov.
        - `<attribution>` (e.g. `<a href="http://www.senate.gov/artandhistory/history/common/generic/Photo_Collection_of_the_Senate_Historical_Office.htm">Courtesy U.S. Senate Historical Office</a>`)
          - The source of the image.

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<member>`

Parent container for an individual member’s entry. A `<member>` element may include the following children:

- `<currentMember>` (e.g., True)  
  - Indicator of whether the member is currently serving.
  - Possible values are "True" or "False".
- `<birthYear>` (e.g., 1940)  
  - Member’s year of birth.
- `<deathYear>`
  - Member’s year of death.
- `<updateDate>` (e.g., 2022-05-17T18:44:02Z)
  - The date of update in Congress.gov.
- `<depiction>`
  - Container for the member’s current official portrait. A `<depiction>` element may include the following children:
    - `<imageUrl>` (e.g., <https://www.congress.gov/img/member/l000174_200.jpg>)
      - The member's current portrait on Congress.gov.
    - `<attribution>` (e.g., `<a href="http://www.senate.gov/artandhistory/history/common/generic/Photo_Collection_of_the_Senate_Historical_Office.htm">Courtesy U.S. Senate Historical Office</a>`)
      - The source of the image.
- `<terms>`
  - Container of a member’s terms of service in chronological order. A `<terms>` element may include the following child, which is repeatable:
    - `<item>`
      - Container for the member’s service in an individual Congress. An `<item>` element is repeatable and may include the following children:
        - `<memberType>` (e.g., Senator)
          - The membership type.
          - Possible values are "Representative", "Resident Commissioner", "Delegate", or "Senator".
        - `<congress>` (e.g., 94)
          - The Congress during which the member served.  
          - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
        - `<chamber>` (e.g., Senate)
          - The chamber in which the member served during that Congress.
          - Possible values are "House of Representatives" and "Senate".
        - `<stateCode>` (e.g., VT)
          - The two-digit postal code abbreviation for the state represented by the member.
        - `<stateName>` (e.g., Vermont)
          - The name of the state represented by the member.
        - `<partyName>` (e.g., Democratic)
          - The political party of the member.
          - Possible values are "Democratic", "Independent", "Independent Democrat", "Libertarian", and "Republication".
        - `<partyCode>` (e.g., D)
          - The single letter abbreviation for the political party of the member.
          - Possible values are "D", "I", "ID", "L", and "R".
        - `<startYear>` (e.g., 1975)
          - The year in which the member’s service in that Congress began.
        - `<endYear>` (e.g., 1977)
          - The year in which the member’s service in that Congress ended.
        - `<district>`  
          - The Congressional district represented by the member (exclusive to the House). The value of zero indicates the state, district or territory has only one member in the House.
- `<bioguideID>` (e.g., L000174)
  - The unique ID value that originates in the [Biographical Directory of the United States Congress, 1774-Present](https://bioguide.congress.gov/).
  - View a [field values list of Bioguide identifiers](https://www.congress.gov/help/field-values/member-bioguide-ids) for current and former members in Congress.gov.
- `<party>` (e.g., Democatic)
  - The current political party of the member. Note: This does not currently reflect party changes.
  - Possible values are "Democratic", "Independent", "Independent Democrat", "Libertarian", and "Republication".
- `<state>` (e.g., Vermont)
  - The state represented by the member.
- `<district>`
  - The Congressional district represented by the member (exclusive to House). The value of zero indicates the state, district or territory has only one member in the House.
- `<officialUrl>` (e.g., <https://www.leahy.senate.gov/>)
  - The member’s official website.
- `<honorificName>` (e.g., Mr.)  
  - The honorific title of the member.
- `<firstName>` (e.g., Patrick)  
  - The member’s first name.
- `<middleName>` (e.g., Joseph)
  - The member’s middle name.
- `<lastName>` (e.g., Leahy)
  - The member’s last name.
- `<suffixName>`  
  - The member’s suffix.
- `<nickName>`  
  - The member’s nickname.
- `<directOrderName>` (e.g., Patrick J. Leahy)
  - The member’s name in first-name-first order.
- `<invertedOrderName>` (e.g., Leahy, Patrick J.)
  - The member’s name in last-name-first order.
- `<addressInformation>`
  - Container for the member’s contact information. An `<addressInformation>` container may include the following children:
    - `<officeAddress>` (e.g, 437 Russell Senate Office Building Washington, DC 20510)
      - The member’s mailing and physical office address in Washington, D.C. The `<officeAddress>` element provides the full address for Senate members and only the House office building information for House members.
    - `<city>` Washington
      - The city of Washington.
    - `<district>` DC
      - The two letter postal abbreviation for the District of Columbia.
    - `<zipCode>` (e.g., 20510)
      - The postal zip code for the member’s office in Washington, D.C.
    - `<phoneNumber>` (e.g., (202) 224-4242)
      - The telephone number for the member’s office in Washington, D.C.
- `<leadership>`
  - Container for the leadership positions available on Congress.gov that the member has held during their membership/tenure of service. A `<leadership>` container may include the following child, which is repeatable:
    - `<item>`
      - Container for individual leadership positions held by the member during a Congress. An `<item>` container is repeatable and may include the following children:
      - `<type>` (e.g., President Pro Tempore)
        - The title of the leadership position held by the member.
      - `<congress>` (e.g., 113)
        - The Congress during which the specified leadership position was held by the member.
      - `<current>` (e.g., False)
        - Indicator whether the leadership position is currently held by the member. NOTE: This value may change from True to False during a Congress.
        - Possible values are "True" or "False".
- `<sponsoredLegislation>`
  - Container for bills and resolutions sponsored by member. A `<sponsoredLegislation>` container may include the following children:
    - `<count>` (e.g., 1753)
      - The total number of bills and resolutions sponsored by the member.
    - `<url>` (e.g., <https://api.congress.gov/v3/member/L000174/sponsored-legislation>)
      - A referrer URL to the sponsored-legislation level of the API. Click [here](#sponsored-legislation-level) for more information about the sponsored-legislation level.
- `<cosponsoredLegislation>`
  - Container for bills and resolutions cosponsored by member. A `<cosponsoredLegislation>` container may include the following children:
    - `<count>` (e.g., 7470)  
      - The total number of bills and resolutions cosponsored by the member.
    - `<url>` (e.g., <https://api.congress.gov/v3/member/L000174/cosponsored-legislation>)
      - A referrer URL to the cosponsored-legislation level of the API. Click [here](#cosponsored-legislation-level) for more information about the cosponsored-legislation level.  
- `<updateDate>` (e.g., 2022-07-22T18:44:02Z)
  - The date of last update in Congress.gov.

### Sponsored-Legislation Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<sponsoredLegislation>`

Parent container for all sponsored bills and resolutions. A `<sponsoredLegislation>` element may include the following children:

- `<item>`
  - Container for an individual bill or resolution sponsored by the member. An `<item>` element may include the following children:
    - `<introducedDate>` (e.g., 2022-06-16)
      - The date the bill or resolution was introduced.
    - `<type>` (e.g., S)
      - The type of bill or resolution.
      - Possible values are "HR", "S", "HJRES", "SJRES", "HCONRES", "SCONRES", "HRES", and "SRES".
    - `<congress>` (e.g., 117)
      - The congress during which a bill or resolution was introduced or submitted.
      - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov
    - `<latestTitle>` (e.g., Patent Trial and Appeal Board Reform Act of 2022)
      - The display title for the bill or resolution on Congress.gov.
    - `<number>` (e.g., 4417)
      - The assigned bill or resolution number.
    - `<policyArea>`
      - Container for the policy area term of the bill or resolution. Every bill and resolution is assigned one policy area term; view the [field values list of policy area terms](https://www.congress.gov/help/field-values/policy-area) on Congress.gov. Read more about [policy area terms](https://www.congress.gov/help/legislative-glossary#glossary_policyareaterm) on Congress.gov. A `<policyArea>` element may include the following child:
        - `<name>` (e.g., Commerce)
          - The policy area term assigned to the bill or resolution by CRS.
    - `<latestAction>`
      - Container for the latest action taken on the bill or resolution. A `<latestAction>` element may include the following children:
        - `<actionDate>` (e.g., 2022-06-16)
          - The date of the latest action taken on the bill or resolution.
        - `<text>` (e.g., Read twice and referred to the Committee on the Judiciary.)
          - The text of the latest action taken on the bill or resolution.
    - `<url>` (e.g., <https://api.congress.gov/v3/bill/117/s/4417>)
      - A referrer URL to the bill item in the API. Documentation for the bill endpoint is [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/BillEndpoint.md).

### Cosponsored-Legislation Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<cosponsoredLegislation>`

Parent container for all sponsored bills and resolutions. A `<cosponsoredLegislation>` element may include the following children:

- `<item>`
  - Container for an individual bill or resolution sponsored by the member. An `<item>` element may include the following children:
    - `<introducedDate>` (e.g., 2022-07-20)
      - The date the bill or resolution was introduced.
    - `<type>` (e.g., SRES)
      - The type of bill or resolution.
      - Possible values are "HR", "S", "HJRES", "SJRES", "HCONRES", "SCONRES", "HRES", and "SRES".
    - `<congress>` (e.g., 117)
      - The congress during which a bill or resolution was introduced or submitted.
      - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
    - `<latestTitle>` (e.g., A resolution recognizing the importance of independent living for individuals with disabilities made possible by the Americans with Disabilities Act of 1990 and calling for further action to strengthen home and community living for individuals with disabilities.)
      - The display title for the bill or resolution on Congress.gov.
    - `<number>` (e.g., 714)
      - The assigned bill or resolution number.
    - `<policyArea>`
      - Container for the policy area term of the bill or resolution. Every bill and resolution is assigned one policy area term; view the [field values list of policy area terms](https://www.congress.gov/help/field-values/policy-area) on Congress.gov. Read more about [policy area terms](https://www.congress.gov/help/legislative-glossary#glossary_policyareaterm) on Congress.gov. The `<policyArea>` element may include the following child:
        - `<name>` (e.g., Health)
          - The policy area term assigned to the bill or resolution by CRS.
    - `<latestAction>`
      - Container for the latest action taken on the bill or resolution. A `<latestAction>` element may include the following children:
        - `<actionDate>` (e.g., 2022-07-20)
          - The date of the latest action taken on the bill or resolution.
        - `<text>` (e.g., Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S3547-3548))
          - The text of the latest action taken on the bill or resolution.
    - `<url>` (e.g., <https://api.congress.gov/v3/bill/117/sres/714>)
      - A referrer URL to the bill item in the API. Documentation for the bill endpoint is [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/BillEndpoint.md).


================================================
File: /Documentation/CommitteeMeetingEndpoint.md
================================================
# Committee Meeting endpoint

## Coverage

Coverage information for committee meeting data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about committee meeting data at [About Committees and Committee Materials](https://www.congress.gov/help/committee-materials#committee-schedule) on Congress.gov. For information on conference committees, please click [here](https://www.congress.gov/help/legislative-glossary#c). 

## OpenAPI Specification

View OpenAPI Specification on the committee meeting API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/committee-meeting/committee_meeting_list).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that committee meeting items at the list level can be filtered down by congress (e.g., 118) and by chamber (e.g., house) - <https://api.congress.gov/v3/committee-meeting/118/house?api_key>=.

`<api-root>`

The `<api-root>` is only present in the XML format.

`<committeeMeetings>`

Container for committee meetings. A `<committeeMeetings>` container may include the following children:

- `<item>`
  - Container for an individual committee meeting. An `<item>` element is repeatable and may include the following children:
     - `<eventId>` (e.g., 115538)
         - The event identifier of the committee meeting.
     - `<url>` (e.g., <https://api.congress.gov/v3/committee-meeting/118/house/115538>)
         - A referrer URL to the committee meeting item in the API.
     - `<updateDate>` (e.g., 2023-03-27 18:11:19+00:00)
         - The date of update in Congress.gov.
     - `<congress>` (e.g., 117)
         - The congress during which the committee meeting took place.
         - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
     - `<chamber>` (e.g., House)
         - The chamber where the committee meeting was held.
         - Possible values are "House", "Senate" and "NoChamber".

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<committeeMeeting>`

Parent container for a single committee meeting. A `<committeeMeeting>` element may include the following children:
- `<eventId>` (e.g., 115538)
    - The event identifier of the committee meeting.
- `<updateDate>` (e.g., 2023-03-27 18:11:19+00:00)
    - The date of update in Congress.gov.
- `<congress>` (e.g., 117)
    - The congress during which the committee meeting took place.
    - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
- `<type>` (e.g., Hearing)
    - The type of meeting.
    - Possible values for House meetings are "Meeting", "Hearing", and "Markup". Senate meetings are all tagged as a "Meeting".
- `<title>` (e.g., Legislative hearing on: •H.R. 1246 (Rep. Hageman), To authorize leases of up to 99 years for land held in trust for federally recognized Indian tribes; and•H.R. 1532 (Rep. Hageman), To authorize any Indian Tribe to lease, sell, convey, warrant, or otherwise transfer real property to which that Indian Tribe holds fee title without the consent of the Federal Government, and for other purposes.)
    - The title of the meeting.
- `<meetingStatus>` (e.g., Scheduled)
    - The status of the meeting.
    - Possible values are "Scheduled", "Canceled", "Postponed", and "Rescheduled".
- `<date>` (e.g., 2023-03-24 13:00:00+00:00)
    - The date of the meeting.
- `<chamber>` (e.g., House)
    - The chamber where the committee meeting was held.
    - Possible values are "House", "Senate" and "NoChamber".
- `<committees>` 
    - Container for the committees or subcommittees the held the meeting. A `<committees>` element may include the following children:
        - `<item>`
            - Container for an individual committee or subcommittee that held the meeting. An `<item>` element is repeatable and may include the following children:
                - `<systemCode>` (e.g., hsii24)
                    - Unique ID value for the committee or subcommittee.
                - `<url>` (e.g., <https://api.congress.gov/v3/committee/house/hsii24>)
                    - A referrer URL to the committee or subcommittee item in the API. Documentation for the committee API is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeEndpoint.md).
                - `<name>` (e.g., House Natural Resources Subcommittee on Indian and Insular Affairs)
                    - The name of the committee or subcommittee.
- `<location>` 
    - Container for the location of the meeting. A `<location>` element may include the following children:
        - `<room>` (e.g., 1324)
            - The room number where the meeting will be or was held. If the meeting was held virtually using 'Webex', the value for `<room>` will be 'WEBEX'. 
            - This element is not present for field meetings.
        - `<building>` (e.g., Longworth House Office Building)
            - The building name where the meeting will be or was held. If the meeting was held virtually using 'Webex', the value for `<building>` may be '----------'. 
            - This element is not present for field meetings.
        - `<address>`
            - The address for the meeting, including the building's name, postal code, state, street address, and city.
            - This element is only present for field meetings.
- `<videos>`
    - Container for videos on the meeting. A `<videos>` element may include the following children:
        - `<item>`
            - Container for a video on the meeting. An `<item>` element may include the following children:
                - `<name>` (e.g., Securing Our Communities: Federal Support to High-Risk Urban Areas)
                    - The title of the video.
                - `<url>` (e.g., <https://www.congress.gov/committees/video/house-appropriations/hshm12/yv8VUIRAm7k>)
                    - The URL for the video on Congress.gov.
- `<witnesses>`
    - Container for witnesses associated with the meeting. A `<witnesses>` element may include the following children:
        - `<item>`
            - Container for a witness associated with the meeting. An `<item>` element may include the following children:
                - `<name>` (e.g., Mr. Thomas DiNanno)
                    - The name of the witness.
                - `<position>` (e.g., Assistant Administrator, Grant Programs Directorate, Federal Emergency Management Agency)
                    - The witness's professional position.
                - `<organization>` (e.g., U.S. Department of Homeland Security)
                    - The witness's organization.
- `<witnessDocuments>`
    - Container for documents provided by witnesses. A `<witnessDocuments>` element may include the following children:
        - `<item>`
            - Container for a witness document. An `<item>` element may include the following children:
                - `<documentType>` (e.g., Witness Statement)
                    - The type of witness document. 
                    - Possible values are "Witness Biography", "Witness Supporting Document", "Witness Statement", and "Witness Truth in Testimony".
                - `<format>` (e.g., PDF)
                    - The format type for the witness document.
                - `<url>` (e.g., https://www.congress.gov/118/meeting/house/115538/witnesses/HHRG-118-II24-Wstate-OsceolaM-20230324.pdf)
                    - The URL for the witness document in Congress.gov.
- `<meetingDocuments>`
    - Container for meeting-related documents, provided by committees or subcommittees. A `<meetingDocuments>` element may include the following children:
        - `<item>`
            - Container for a meeting document. An `<item>` element may include the following children:
                - `<name>` (e.g., Hearing Notice)
                    - The name of the meeting document. 
                - `<description>`
                    - A description of the meeting document. 
                - `<documentType>` (e.g., Support Document)
                    - The type of meeting document.
                    - Possible values are "Activity Report", "Bills and Resolutions", "Committee Amendment", "Committee Recorded Vote", "Committee Report", "Committee Rules", "Conference Report", "Floor Amendment", "Generic Document", "Hearing: Cover Page", "Hearing: Member Roster", "Hearing: Questions for the Record", "Hearing: Table of Contents", "Hearing: Transcript", "Hearing: Witness List", "House or Senate Amendment", "Member Statements", and "Support Document".
                - `<url>` (e.g., <https://www.congress.gov/118/meeting/house/115538/documents/HHRG-118-II24-20230324-SD001.pdf>)
                    - The URL for the meeting document on Congress.gov.
                - `<format>` (e.g., PDF)
                    - The format type for the meeting document.
- `<hearingTranscript>`
    - Container for associated hearing transcripts to committee meetings. A `<hearingTranscript>` element may include the following children:
        - `<jacketNumber>` 
            - The jacket identifier of the hearing transcript. The `<jacketNumber>` is printed on the front page of a hearing transcript and is usually five digits.
        - `<url>` 
            - A referrer URL to the hearing item in the API. Documentation for the hearing API is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/HearingEndpoint.md).
- `<relatedItems>`
    - Container for associated bills, resolutions, treaties or nominations to the meeting. A `<relatedItems>` element may include the following children:
        - `<bills>`
            - Container for associated bills and resolutions to the meeting. A `<bills>` element may include the following children:
                - `<bill>`
                    - Container for an associated bill or resolution to the meeting. A `<bill>` element may include the following children:
                        - `<type>` (e.g., HR)
                            - The type of bill or resolution.
                            - Possible values are "HR", "S", "HJRES", "SJRES", "HCONRES", "SCONRES", "HRES", and "SRES".
                        - `<number>` (e.g., 1532)
                            - The assigned bill or resolution number.
                        - `<congress>` (e.g., 118)
                            - The congress during which a bill or resolution was introduced or submitted.
                        - `<url>` (e.g., <https://api.congress.gov/v3/bill/118/hr/1532>)
                            - A referrer URL to the bill or resolution item in the API. Documentation for the bill API is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/BillEndpoint.md).
        - `<treaties>`
            - Container for associated treaties to the meeting. A `<treaties>` element may include the following children:
                - `<item>`
                    - Container for an associated treaty to the meeting. An `<item>` element may include the following children:
                        - `<part>`
                            - The part number for the treaty, if partitioned.
                        - `<number>` 
                            - The assigned treaty number.
                        - `<congress>`
                            - The congress during which the treaty was submitted.
                        - `<url>`
                            - A referrer URL to the treaty item in the API. Documentation for the treaty API is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/TreatyEndpoint.md).
        - `<nominations>`
            - Container for associated nominations to the meeting. A `<nominations>` element may include the following children:
                - `<item>`
                    - Container for an associated nomination to the meeting. An `<item>` element may include the following children:
                        - `<part>`
                            - The part number for the nomination. 
                            - If the nomination wasn't partitioned, the value will be 00.
                        - `<number>` 
                            - The assigned nomination number.
                        - `<congress>`
                            - The congress during which the nomination was received.
                        - `<url>`
                            - A referrer URL to the nomination item in the API. Documentation for the nomination API is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/NominationEndpoint.md).


================================================
File: /Documentation/CongressEndpoint.md
================================================
# Congress endpoints

## Coverage

Coverage information for congress data in the API can be found at the [Congresses field values list](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Information on past session dates can be found on Congress.gov at the [Dates of Past Sessions](https://www.congress.gov/past-days-in-session).

## OpenAPI Specification

View OpenAPI Specification on the congress API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/congress/congress_list).

## Elements and Descriptions

The section below details available element names, their descriptions, and possible values.

### List Level

Note that congress items at the list level cannot be filtered (<https://api.congress.gov/v3/congress?api_key>=).

`<api-root>`

The `<api-root>` is only present in the XML format.

`<congresses>`

Parent container for congress and congressional sessions. A `<congresses>` element may include the following children:

- `<item>`
  - Container for a congress item. An `<item>` element is repeatable and may include the following children:
    - `<name>` (e.g. 116th Congress)
      - The name of the congress.
    - `<startYear>` (e.g. 2019)
      - The start year for the congress. Congresses span over a two-year period.
    - `<endYear>` (e.g. 2020)
      - The generalized end year for the congress. Congresses span over a two-year period. See [Congresses - Field Values](https://www.congress.gov/help/field-values/congresses) for more information about congress field values.  
    - `<sessions>`
      - Container for sessions of congress. A `<sessions>` element may include the following children:
        - `<item>`
          - Container for a single session of congress for a chamber. An `<item>` element is repeatable and may include the following children:
            - `<chamber>`(e.g. House of Representatives)
              - The chamber associated with the session of congress.
              - Possible values are "House of Representatives" and "Senate".
            - `<type>` (e.g. R)
              - The type of session.
              - Possible values are "R" and "S" where "R" stands for "Regular" and "S" stands for "Special".
            - `<startDate>` (e.g. 2019-01-03)
              - The start date of the session.
            - `<endDate>` (e.g. 2020-01-03)
              - The specific end date of the session. This value is specified for legislative research. See [Past Days in Session](https://www.congress.gov/past-days-in-session) for more information about past days in session of legislative sessions.
            - `<number>` (e.g. 1)
              - The assigned session's number.
              - For special sessions, this value is suppressed.
     - `<url>` (e.g. <https://api.congress.gov/v3/congress/117>)
       - A referrer URL to the congress item in the API. 

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<congress>`

Parent container for a congress and its congressional sessions. A `<congress>` element may include the following children:

- `<sessions>`
  - Container for sessions of congress. A `<sessions>` element may include the following children:
    - `<item>`
      - Container for a single session of congress for a chamber. An `<item>` element is repeatable and may include the following children:
        - `<chamber>`(e.g. House of Representatives)
          - The chamber associated with the session of congress.
          - Possible values are "House of Representatives" and "Senate".
        - `<type>` (e.g. R)
          - The type of session.
          - Possible values are "R" and "S" where "R" stands for "Regular" and "S" stands for "Special".
        - `<startDate>` (e.g. 2019-01-03)
          - The start date of the session.
        - `<endDate>` (e.g. 2020-01-03)
          - The end date of the session.
        - `<number>` (e.g. 1)
          - The assigned session's number.
          - For special sessions, this value is suppressed.
- `<name>` (e.g. 116th Congress)
  - The name of the congress.
- `<startYear>` (e.g. 2019)
  - The start year for the congress. Congresses span over a two-year period.
- `<endYear>` (e.g. 2020)
  - The end year for the congress. Congresses span over a two-year period.
- `<updateDate>` (e.g. 2019-01-03T18:37:12Z)
  - The date of update in Congress.gov.
- `<number>` (e.g. 116)
  - The congress number.
- `<url>` (e.g. <https://api.congress.gov/v3/congress/116>)
  - A referrer URL to the congress item in the API.


================================================
File: /Documentation/CommitteePrintEndpoint.md
================================================
# Committee Print endpoints

## Coverage

Coverage information for committee print data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about committee print data at [About Committees and Committee Materials](https://www.congress.gov/help/committee-materials#committee-prints) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the committee print API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/committee-print/committee_print_list).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that committee print items at the list level can be filtered down by congress (e.g., 117) and by chamber (e.g., house) - <https://api.congress.gov/v3/committee-print/117/house?api_key>=.

`<api-root>`

The `<api-root>` is only present in the XML format.

`<committeePrints>`

Container for committee prints. A `<committeePrints>` container may include the following children:

- `<item>`
  - Container for an individual committee print. An `<item>` element is repeatable and may include the following children:
     - `<jacketNumber>` (e.g., 48144)
         - The jacket identifier of the committee print. The `<jacketNumber>` is printed on the front page of a print and is usually five digits.
     - `<url>` (e.g., <https://api.congress.gov/v3/committee-print/117/house/48144>)
         - A referrer URL to the committee print item in the API.
     - `<updateDate>` (e.g., 2022-08-01 21:19:33+00:00)
         - The date of update in Congress.gov.
     - `<congress>` (e.g., 117)
         - The congress during which the committee print was produced.
         - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
     - `<chamber>` (e.g., House)
         - The chamber where the committee print was produced.
         - Possible values are "House", "Senate" and "NoChamber".

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<committeePrint>`

Parent container for a single committee print. A `<committeePrint>` element may include the following children:

- `<item>`
  - Container for a committee print. An `<item>` element may include the following children:
     - `<jacketNumber>` (e.g., 48144)
         - The jacket identifier of the committee print. The `<jacketNumber>` is printed on the front page of a print and is usually five digits.
     - `<citation>` (e.g., 117-62)
         - The committee print's citation. 
         - Committee prints may or may not be numbered by their associated committee. 
     - `<congress>` (e.g., 117)
         - The congress during which the committee print was produced.
         - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
     - `<number>` (e.g., 62)
         - The assigned committee print number. 
     - `<title>` (e.g., RULES COMMITTEE PRINT 117-62 TEXT OF H.R. 5768, VIOLENT INCIDENT CLEAR- ANCE AND TECHNOLOGICAL INVESTIGATIVE METHODS ACT OF 2022)
         - The title of the committee print. 
     - `<chamber>` (e.g., House)
         - The chamber where the committee print was produced.
         - Possible values are "House", "Senate" and "NoChamber".
     - `<committees>` 
         - Container for the committees associated with the committee print. A `<committees>` element may include the following children:
             - `<item>`
                 - Container for an individual committee associated with a committee report. An `<item>` element is repeatable and may include the following children:
                      - `<url>` (e.g., <https://api.congress.gov/v3/committee/house/hsru00>)
                          - A referrer URL to the committee item in the API. Documentation for the committee endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeEndpoint.md).
                      - `<systemCode>` (e.g., hsru00)
                          - Unique ID value for the committee.
                      - `<name>` (e.g., Rules Committee)
                          - The name of the committee.
     - `<associatedBills>`
         - Container for associated bills to the committee print. An `<associatedBills>` element may include the following children:
             - `<item>`
                 - Container for an associated bill. An `<item>` element is repeatable and may include the following children:
                     - `<congress>` (e.g., 117)
                         - The congress during which a bill or resolution was introduced or submitted.
                     - `<type>` (e.g., HR)
                         - The type of bill or resolution.
                         - Possible values are "HR", "S", "HJRES", "SJRES", "HCONRES", "SCONRES", "HRES", and "SRES".
                     - `<number>` (e.g., 5768)
                         - The assigned bill or resolution number.
                     - `<url>` (e.g., <https://api.congress.gov/v3/bill/117/hr/5768>)
                         - A referrer URL to the bill or resolution item in the API. Documentation for the bill endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/BillEndpoint.md).
     - `<text>`
         - Container for committee print text. A `<text>` element may include the following children:
             - `<count>` (e.g., 4)
                 - The number of text formats for the committee print.
             - `<url>` (e.g., <https://api.congress.gov/v3/committee-print/117/house/48144/text>)
                 - A referrer URL to the text level of the committee print API. Click [here](#text-level) for more information about the text level.

### Text Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<text>`

Parent container for the text formats of a committee print. A `<text>` element may include the following children:

- `<item>`
     - Container for a text format. An `<item>` element is repeatable and may include the following children: 
         - `<url>` (<https://www.congress.gov/117/cprt/HPRT48144/CPRT-117HPRT48144.pdf>)
             - The URL for the text format in Congress.gov.
         - `<type>` (e.g., PDF)
             - The format type for the text.
             - Possible values are "PDF", "Formatted Text", "Formatted XML", and "Generated HTML".


================================================
File: /Documentation/CommitteeEndpoint.md
================================================
# Committee endpoints

## Coverage

Coverage information for committee data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Read more about committee data at [About Committees and Committee Materials](https://www.congress.gov/help/committee-materials) and committee name data at [Committee Name History](https://www.congress.gov/help/committee-name-history) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the committee API, supported endpoints, and available parameters at [https://api.congress.gov](https://api.congress.gov/#/committee/committee_list).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that committee items at the list level can be filtered down by congress (e.g. 117) and by chamber (e.g. House) – <https://api.congress.gov/v3/committee/117/house?api_key=>).

`<api-root>`

The `<api-root>` is only present in the XML format.

`<committees>`

 Parent container for committees and subcommittees. A `<committees>` element may contain the following children:

- `<item>`
  - Container for an individual committee or subcommittee. An `<item>` element is repeatable and may contain the following children:
    - `<url>` (e.g., <https://api.congress.gov/v3/committee/house/hspw00>)
      - A referrer URL to the committee or subcommittee item in the API.
    - `<systemCode>` (e.g., hspw00)
      - Unique ID value for the committee or subcommittee. The first letter represents the chamber, i.e., House, Senate, or Joint. The two numerals at the end of the `<systemCode>` indicate whether the entity is a full committee or subcommittee. Full committees are represented by a double zero and subcommittees will have an identical systemCode as its parent committee but with numerals other than the double zero.  
    - `<name>` (e.g., Transportation and Infrastructure Committee)
      - The name of the committee or subcommittee.
    - `<parent>`
      - Container for parent committee information providing an indication of whether the subcommittee has a parent. A `<parent>` element may contain the following children:
        - `<url>`
          - A referrer URL to the parent committee item in the API.
        - `<systemCode>`
          - Unique ID value for the parent committee. Parent committee `<systemCode>` values end in a double zero.
        - `<name>`
          - The name of the parent committee.
    - `<subcommittees>`
      - Container for subcommittee information and indication of whether a parent committee has subcommittees. A `<subcommittees>` element is repeatable and may contain the following children:
        - `<item>`
          - Container for an individual subcommittee of the committee. An `<item>` element is repeatable and may contain the following children:
            - `<url>` (e.g., <https://api.congress.gov/v3/committee/house/hspw14>)
              - A referrer URL to the subcommittee item in the API.
            - `<systemCode>` (e.g., hspw14)
              - The unique ID value for the subcommittee. Subcommittee `<systemCode>` values contain numerals other than a double zero.
            - `<name>` (e.g., Railroads, Pipelines, and Hazardous Materials Subcommittee)
              - The name of the subcommittee.
    - `<chamber>` (e.g., House)
      - The committee's chamber of origin.
      - Possible values are "House", "Senate", and "Joint".
    - `<committeeTypeCode>` (e.g., Standing)
      - The type of committee. Possible values are "Commission or Caucus", "Joint", "Other", "Select", "Special", "Standing", "Subcommittee", and "Task Force".

### Item Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<committee>`

Parent container for an individual committee or subcommittee entry. A `<committee>` element may contain the following children:

- `<systemCode>` (e.g., hspw00)
  - The unique ID value for the committee. Parent committee `<systemCode>` values end in a double zero while those for a subcommittee end with numerals other than a double zero.
- `<parent>`  
  - Container for parent committee information providing an indication of whether the subcommittee has a parent. A `<parent>` element may contain the following children:
    - `<url>`
      - A referrer URL to the committee's parent in the API.
    - `<systemCode>`
      - The unique ID of the committee's parent. Parent committee `<systemCode>` values end in a double zero.
    - `<name>`
      - The name of the committee's parent.  
- `<updateDate>` (e.g., 2020-02-04T00:07:37Z)
  - The date of update in Congress.gov.
- `<isCurrent>` (e.g., True)
  - Flag indicating whether the committee is currently active.
  - Possible values are "True" or "False".
- `<subcommittees>`
  - Container for all of the committee's subcommittee's. The `<subcommittee>` element may contain the following children, which are repeatable:  
    - `<item>`
      - Container for an individual subcommittee under the committee. The `<item>` element is repeatable and may contain the following children:
      - `<url>` (e.g., <https://api.congress.gov/v3/committee/house/hspw14>)
        - A referrer URL to the subcommittee item in the API.
      - `<systemCode>` (e.g., hspw14)
        - The unique ID of the subcommittee. Subcommittee `<systemCode>` values contain numerals other than a double zero.
      - `<name>` (e.g., Railroads, Pipelines, and Hazardous Materials Subcommittee)
        - The name of the subcommittee.
- `<reports>`
  - Container for committee reports issued by a committee. A `<reports>` element may contain the following children:
    - `<url>` (e.g., <https://api.congress.gov/v3/committee/house/hspw00/reports>)
      - A referrer URL to the committee reports level of the committee API. Click [here](#committee-reports-level) for more information about the committee reports level.
    - `<count>` (e.g., 1373)
      - The number of reports present in the committee's reports API endpoint.  
- `<communications>`
  - Container for communications associated with a committee. A `<communications>` element may contain the following children:
    - `<url>` (e.g., <https://api.congress.gov/v3/committee/house/hspw00/house-communication>)
      - A referrer URL to the communications level of the committee API. Click [here](#house-communications-level) for more information on the House communications level and [here](#senate-communications-level) for more information on the Senate communications level.
    - `<count>` (e.g., 6796)
      - The number of communications in the committee's House or Senate communications API endpoint.  
- `<bills>`
  - Container for bills associated with a committee. A `<bills>` element may contain the following children:
    - `<url>` (e.g., <https://api.congress.gov/v3/committee/house/hspw00/bills>)
      - A referrer URL to the bills level of the committee API. Click [here](#bills-level) for more information about the bills level.
    - `<count>` (e.g., 25313)
      - The number of bills in the committee's bills API endpoint.  
- `<nominations>`
  - Container for nominations associated with a committee. This is exclusive to the Senate. A `<nominations>` element may contain the following children (the below data is taken from <https://api.congress.gov/v3/committee/senate/ssas00>):
    - `<url>` (e.g., <https://api.congress.gov/v3/committee/senate/ssas00/nominations>)
      - A referrer URL to the nominations level of the committee API. Click [here](#nominations-level) for more information about the nominations level.
    - `<count>` (e.g., 20126)
      - The number of nominations in the committee's nominations API endpoint.
- `<history>`
  - Container for the committee's activity/identification history across Congresses. The `<history>` element may contain the following children, which are repeatable:  
    - `<item>`
      - Container for a committee's activity/identification. The `<item>` element is repeatable and may contain the following children:
        - `<endDate>`
          - The date the committee, as named, ceased to exist.
        - `<officialName>` (e.g., Committee on Transportation and Infrastructure)
          - The full official name of the committee.  
        - `<libraryOfCongressName>` (e.g., Transportation and Infrastructure)
          - The shortened name of the committee.
        - `<startDate>` (e.g., 1995-01-04T05:00:00Z)
          - The date the committee, as named, was formed.
        - `<committeeTypeCode>`
          - The type of committee.
          - Possible values are "Commission or Caucus", "Joint", "Other", "Select", "Special", "Standing", "Subcommittee", and "Task Force".
        - `<establishingAuthority>`
          - The legislative authority for the committee (e.g., 79 H.Res. 5). 
        - `<locLinkedDataId>`
          - ID value to support linking with Library of Congress data (e.g., n79036852). NOTE: Displays when available.
        - `<superintendentDocumentNumber>`
          - ID value to support linking with GPO data (e.g., Y 4.IM 6/2:). NOTE: Displays when available. 
        - `<naraId>`
          - ID value to support linking with NARA data (e.g., 10531570). NOTE: Displays when available.
- `<type>`  (e.g., Standing)
  - Type of committee.
  - Possible values are "Commission or Caucus", "Joint", "Other", "Select", "Special", "Standing", "Subcommittee" and "Task Force".

### Committee Reports Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<reports>`

Parent container for reports issued by a committee. The `<reports>` element may contain the following children, which are repeatable:

- `<item>`
  - Container for individual reports issued by the committee. The `<item>` container is repeatable and may contain the following children:
    - `<citation>` (e.g., H. Rept. 109-570)
      - The citation of the report issued by the committee.  
    - `<url>` (e.g., <https://api.congress.gov/v3/committee-report/109/HRPT/570>)
      - A referrer URL to the committee report item in the API. Documentation for the committee report endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/CommitteeReportEndpoint.md).
    - `<updateDate>` (e.g., 2021-07-10 16:19:06+00:00)
      - The date of update in Congress.gov.
    - `<congress>` (e.g., 109)
      - The congress during which the committee report was produced.
    - `<chamber>` (e.g., House)
      - The chamber where the committee report was produced.
      - Possible values are "House" and "Senate".
    - `<type>` (e.g., HRPT)
      - The type of report.
      - Possible values are "HRPT", "SRPT", and "ERPT".
    - `<number>` (e.g., 570)
      - The assigned committee report number.
    - `<part>` (e.g., 1)
      - The part number of the report.
      - Committee reports without parts will have a value of 1. If there are multiple parts, the number value may be 2, 3, etc.

### Bills Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<committee-bills>`

Parent container for bills and resolutions associated with the committee or subcommittee. The `<committee-bills>` element may contain the following children:

- `<url>` (e.g., <https://api.congress.gov/v3/committee/house/hspw00/bills>)
  - A referrer URL to the committee's bills level in the API.
- `<count>` (e.g., 25313)
  - The number of bills and resolutions in the bills level API.
- `<bills>`
  - Container for all bills and resolutions associated with the committee. The `<bills>` element may contain the following children:
    - `<bill>`
      - Container for individual bills and resolutions associated with the committee. The `<bill>` element is repeatable and may contain the following children:
    - `<congress>` (e.g., 112)
      - The Congress during which the bill or resolution was introduced.  
    - `<billType>` (e.g., HCONRES)
      - The type of bill or resolution.
      - Possible values are “HR”, “S”, “HJRES”, “SJRES”, “HCONRES”, “SCONRES”, “HRES” or “SRES”. House committees will not have a bill type value of “SRES” and Senate committees will not have a bill type value of “HRES”.
    - `<billNumber>` (e.g., 117)
      - The assigned bill or resolution number.  
    - `<relationshipType>` (e.g., Referred to)
      - The relationship of the bill or resolution to the committee.
    - `<actionDate>` (e.g., 2012-04-19T13:01:00Z)
      - The date the `<relationshipType>` occurred.
    - `<updateDate>` (e.g., 2019-02-17T21:10:13Z)
      - The date of update in Congress.gov.

### Nominations Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<nominations>`

Parent container for nominations associated with a Senate committee (the below data is taken from <https://api.congress.gov/v3/committee/senate/ssju00/nominations?api_key>=). The `<nominations>` element may contain the following children, which are repeatable:

- `<item>`
  - Container for individual nominations considered by the Senate committee. The `<item>` element is repeatable and may contain the following children:
    - `<congress>` (e.g., 117)
      - The Congress during which the nomination was received.
    - `<number>` (e.g., 2439)
      - The assigned nomination number.
      - Read more about nomination numbering at [About Nominations by the U.S. President](https://www.congress.gov/help/nominations) on Congress.gov.
    - `<partNumber>` (e.g., 00)
      - The part number for the individual nomination. Nominations with multiple nominees may be partitioned if the nominees follow different confirmation paths.
    - `<citation>` (e.g., PN2439)
      - The citation identifying the nomination. PN indicates "Presidential Nomination" and the digits are the nominations assigned number. If the nomination was partitioned, the citation will include a dash and the partition number (e.g. PN78-4).  
    - `<description>` (e.g., Araceli Martinez-Olguin, of California, to be United States District Judge for the Northern District of California, vice Jeffrey S. White, retired.)
      - The description of the nomination.
    - `<receivedDate>` (e.g., 2022-08-01)
      - The date the nomination was received from the President.
    - `<nominationType>`
      - Container for nomination type data. A `<nominationType>` element may contain the following children:
        - `<isCivilian>` (e.g., True)
          - Flag indicating whether the nomination is for a civilian position.
          - Possible values are "True" or "False".
        - `<inMilitary>` (e.g., False)
          - Flag indicating whether the nomination is for a military position.
          - Possible values are "True" or "False".
    - `<updateDate>` (e.g., 2022-08-02 04:25:19+00:00)
      - Date of update in Congress.gov
    - `<latestAction>`
      - Container for the latest action taken on the nomination. A `<latestAction>` element may contain the following children:
        - `<actionDate>`(e.g., 2022-08-01)
          - The date of the latest action on the nomination.
        - `<text>` (e.g., Received in the Senate and referred to the Committee on the Judiciary.)
          - The text of the latest action taken on the nomination.
        - `<url>` (e.g., <https://api.congress.gov/v3/nomination/117/2439>)
          - A referrer URL to the nomination item in the API. Documentation for the nomination endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/NominationEndpoint.md).

### House Communications Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<houseCommunications>`

Parent container for communications associated with a House committee. The `<houseCommunications>` element may contain the following children, which are repeatable:

- `<item>`
  - `<chamber>` (e.g., House)
    - The chamber where the communication was received. This value will always be set to "House".
  - `<number>` (e.g., 3262)
    - The assigned communication number.
  - `<communicationType>`
    - Container for communication type information. A `<communicationType>` element may include the following children:
      - `<code>` (e.g., EC)
        - The code for the type of communication.
        - Possible values are "EC", "PM", "PT", and "ML".
      - `<name>` (e.g., Executive Communication)
        - The name of the type of communication.
        - Possible values are "Executive Communication", "Presidential Message", "Petition", and "Memorial".
      - `<congress>` (e.g., 114)
        - The congress during which the communication was received.
      - `<referralDate>` (e.g., 2015-10-27)
        - The date the communication was referred to the committee(s).
      - `<updateDate>` (e.g., 2018-02-02)
        - The date of update in Congress.gov.
      - `<url>` (e.g., <https://api.congress.gov/v3/house-communication/114/ec/3262>)
        - A referrer URL to the House communication item in the API. Documentation for the House communication endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/HouseCommunicationEndpoint.md).

### Senate Communications Level

`<api-root>`

The `<api-root>` is only present in the XML format.

`<senateCommunications>`

Parent container for communications associated with a Senate committee (the below data is taken from <https://api.congress.gov/v3/committee/senate/ssas00/senate-communication?api_key>=). The `<senateCommunications>` element may contain the following children, which are repeatable:

- `<item>`
  - `<chamber>` (e.g., Senate)
    - The chamber where the communication was received. This value will always be set to "Senate".
  - `<number>` (e.g., 1944)
    - The assigned communication number.
  - `<communicationType>`
    - Container for communication type information. A `<communicationType>` element may include the following children:
      - `<code>` (e.g., EC)
        - The code for the type of communication.
        - Possible values are "EC", "POM", and "PM".
      - `<name>` (e.g., Executive Communication)
        - The name of the type of communication.
        - Possible values are "Executive Communication", "Petition or Memorial", and "Presidential Message".
      - `<congress>` (e.g., 117)
        - The congress during which the communication was received.
      - `<referralDate>` (e.g., 2021-09-14)
        - The date the communication was referred to the committee.
      - `<updateDate>` (e.g., 2021-09-15)
        - The date of update in Congress.gov.
      - `<url>` (e.g., <https://api.congress.gov/v3/senate-communication/117/ec/1944>)
        - A referrer URL to the Senate communication item in the API. Documentation for the Senate communication endpoint is available [here](https://github.com/LibraryOfCongress/api.congress.gov/blob/main/Documentation/SenateCommunicationEndpoint.md).


================================================
File: /Documentation/CongressionalRecordEndpoint.md
================================================
# Congressional Record endpoint

## Coverage

Coverage information for Congressional Record data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates). Note that while the Bound Congressional Record is available in Congress.gov, it is not yet available in the API. Read more about Congressional Record data at [About the Congressional Record](https://www.congress.gov/help/congressional-record) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the congressional record API and available parameters at [https://api.congress.gov](https://api.congress.gov/#/congressional-record/congressional_record_list).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that Congressional Record items can be filtered down to a specific year, month, or date by adding ?y=YYYY&m=MM&d=DD to the request URL (e.g., <https://api.congress.gov/v3/congressional-record/?y=2022&m=8&d=16&api_key>=)

`<api-root>`

The `<api-root>` is only present in the XML format.

`<Results>`

Parent container for Congressional Record issues. A `<Results>` element may include the following children:

- `<Issues>`
  - Container for Congressional Record issues. An `<Issues>` element may include the following children:
    - `<item>`
      - Container for an individual COngressional Record issue. An `<item>` element is repeatable and may include the following children:
        - `<Congress>` (e.g., 117)
          - The Congress associated with the Congressional Record issue.
          - View the [field values list of Congresses](https://www.congress.gov/help/field-values/congresses) on Congress.gov. Read more [about Congresses](https://www.congress.gov/help/legislative-glossary#glossary_congress) on Congress.gov.
        - `<Issue>` (e.g., 136)
          - The Congressional Records's issue number.
        - `<Links>`
          - Container for links to the individual sections of the issue. A `<Links>` element may include the following children:
            - `<Digest>`
              - Container for the Daily Digest section of the issue. A `<Digest>` element may include the following children:
                - `<Label>` (e.g., Daily Digest)
                  - The name of the section.
                - `<Ordinal>` (e.g., 1)
                  - The sort order number used for the section's placement on Congress.gov.
                - `<PDF>`
                  - Container for the PDF text format for the section. A `<PDF>` element may include the following children:
                    - `<item>`
                  - Container for the individual PDF text format for the section. Multiple PDFs may be used to deliver the entire section. An `<item>` element is repeatable and may include the following children:
                  - `<Part>` (e.g., 1)
                    - Number assigned to individual PDFs that comprise a single section. If there are multiple Daily Digest section parts, the numbers will be sequential.
                  - `<Url>` (e.g, <https://www.congress.gov/117/crec/2022/08/16/168/136/CREC-2022-08-16-dailydigest.pdf>)
                    - The URL to the individual Daily Digest section PDF.
            - `<Remarks>`
              - Container for the Extension of Remarks section of the issue. A `<Remarks>` element may include the following children:
                - `<Label>` (e.g., Extension of Remarks Section)
                  - The name of the section.
                - `<Ordinal>` (e.g., 4)
                  - The sort order number used for the section's placement on Congress.gov.
                - `<PDF>`
                  - Container for the PDF text format for the section. A `<PDF>` element may include the following children:
                    - `<item>`
                  - Container for the individual PDF text format for the section. Multiple PDFs may be used to deliver the entire section. An `<item>` element is repeatable and may include the following children:
                  - `<Part>` (e.g., 1)
                    - Number assigned to individual PDFs that comprise a single section. If there are multiple Extension of Remarks section parts, the numbers will be sequential.
                  - `<Url>` (e.g, <https://www.congress.gov/117/crec/2022/08/16/168/136/CREC-2022-08-16-extensions.pdf>)
                    - The URL to the individual Extension of Remarks section PDF.
            - `<House>`
              - Container for the House section of the issue. A `<House>` element may include the following children:
                - `<Label>` (e.g., House Section)
                  - The name of the section.
                - `<Ordinal>` (e.g., 3)
                  - The sort order number used for the section's placement on Congress.gov.
                - `<PDF>`
                  - Container for the PDF text format for the section. A `<PDF>` element may include the following children:
                    - `<item>`
                  - Container for the individual PDF text format for the section. Multiple PDFs may be used to deliver the entire section. An `<item>` element is repeatable and may include the following children:
                  - `<Part>` (e.g., 1)
                    - Number assigned to individual PDFs that comprise a single section. If there are multiple House section parts, the numbers will be sequential.
                  - `<Url>` (e.g, <https://www.congress.gov/117/crec/2022/08/16/168/136/CREC-2022-08-16-house.pdf>)
                    - The URL to the individual House section PDF.
            - `<Senate>`
              - Container for the Senate section of the issue. A `<Senate>` element may include the following children:
                - `<Label>` (e.g., Senate Section)
                  - The name of the section.
                - `<Ordinal>` (e.g., 2)
                  - The sort order number used for the section's placement on Congress.gov.
                - `<PDF>`
                  - Container for the PDF text format for the section. A `<PDF>` element may include the following children:
                    - `<item>`
                  - Container for the individual PDF text format for the section. Multiple PDFs may be used to deliver the entire section. An `<item>` element is repeatable and may include the following children:
                  - `<Part>` (e.g., 1)
                    - Number assigned to individual PDFs that comprise a single section. If there are multiple Senate section parts, the numbers will be sequential.
                  - `<Url>` (e.g, <https://www.congress.gov/117/crec/2022/08/16/168/136/CREC-2022-08-16-senate.pdf>)
                    - The URL to the individual Senate section PDF.
            - `<FullRecord>`
              - Container for the Entire Issue section of the issue. A `<FullRecord>` element may include the following children:
                - `<Label>` (e.g., Entire Issue)
                  - The name of the section.
                - `<Ordinal>` (e.g., 5)
                  - The sort order number used for the section's placement on Congress.gov.
                - `<PDF>`
                  - Container for the PDF text format for the section. A `<PDF>` element may include the following children:
                    - `<item>`
                  - Container for the individual PDF text format for the section. Multiple PDFs may be used to deliver the entire section. An `<item>` element is repeatable and may include the following children:
                  - `<Part>` (e.g., 1)
                    - Number assigned to individual PDFs that comprise a single section. If there are multiple Entire Issue section parts, the numbers will be sequential.
                  - `<Url>` (e.g, <https://www.congress.gov/117/crec/2022/08/16/168/136/CREC-2022-08-16.pdf>)
                    - The URL to the individual Entire Issue section PDF.
        - `<PublishDate>` (e.g., 2022-08-16)
          - The publication date of the issue.
        - `<Session>` (e.g., 2)
          - The session of Congress.
          - Possible values are "1" and "2".
        - `<Volume>` (e.g., 168)
          - The volume number of the issue.
          - View a [field values list of Congressional Record Volumes](https://www.congress.gov/help/field-values/congressional-record-volumes) on Congress.gov.


================================================
File: /Documentation/DailyCongressionalRecordEndpoint.md
================================================
# Daily Congressional Record endpoint

## Coverage

Coverage information for daily Congressional Record data in the API can be found at [Coverage Dates for Congress.gov Collections](https://www.congress.gov/help/coverage-dates).  Read more about Congressional Record data at [About the Congressional Record](https://www.congress.gov/help/congressional-record) on Congress.gov.

## OpenAPI Specification

View OpenAPI Specification on the congressional record API and available parameters at [https://api.congress.gov](https://api.congress.gov/#/daily-congressional-record/daily-congressional-record_list).

## Elements and Descriptions

The section below details available element names, their description, and possible values.

### List Level

Note that daily Congressional Record items can be filtered down to volume by adding /{volumeNumber}?api_key=[INSERT_KEY], /{volumeNumber}/{issueNumber}?api_key=[INSERT_KEY], or /{volumeNumber}/{issueNumber}/articles?api_key=[INSERT_KEY] to your search. 

Examples of these searches include:
- /{volumeNumber}: <https://api.congress.gov/v3/daily-congressional-record/167?api_key=[INSERT_KEY]>
- /{volumeNumber}/{issueNumber}: <https://api.congress.gov/v3/daily-congressional-record/167/21?api_key=[INSERT_KEY]>
- /{volumNumber}/{issueNumber}/articles: <https://api.congress.gov/v3/daily-congressional-record/167/21/articles?api_key=[INSERT_KEY]>

`<api-root>`

The `<api-root>` is only present in the XML format.

`<dailyCongressionalRecord>`

Parent container for congressional record issues. A `<dailyCongressionalRecord>` element may include the following children:

- `<issue>`
  - Container for a daily Congressional Record issue. An `<issue>` element may include the following children:
    - `<issueNumber>`
      - The daily Congressional Record's issue number.
    - `<volumeNumber>`
      - The daily Congressional Record's volume number.
    - `<issueDate>`
       - The date that the daily Congressional Record was issued.
    - `<congress>`
      - The Congress associated with the daily congressional record issue.
    - `<sessionNumber>`
      - The session number. Possible values are "1" and "2". 
    - `<url>` 
      - The URL to the entire issue of the daily Congressional Record. 
    - `<updateDate>` 
       - The date that the daily Congressional Record was updated.
      
### Item Level

`<api-root>`

 The `<api-root>` is only present in the XML format.

 `<issue>`

 Parent container for the daily Congressional Record issues. An `<issue>` element may include the following children:

   - `<issueNumber>`
      - The daily Congressional Record's issue number.
   - `<volumeNumber>`
      - The daily Congressional Record's volume number.
   - `<issueDate>`
      - The date that the daily Congressional Record was issued.
   - `<congress>`
      - The Congress associated with the daily Congressional Record issue.
   - `<sessionNumber>`
      - The session number. Possible values are "1" and "2". 
   - `<url>` 
      - The URL to the entire issue of the daily Congressional Record (the URL used to request this issue).
   - `<updateDate>` 
      - The date that the daily Congressional Record was updated.
   - `<fullIssue>`
      - Container for full issue, sections, and articles. A `<fullIssue>` element may include the following children:
        - `<entireIssue>`
          - Container for entire issue items. An `<entireIssue>` element may include the following children:
            - `<item>`
              - Container for an entire issue item. An `<item>` element may include the following children:
              - `<part>`
                 - The part of the daily Congressional Record issue.
              - `<type>`
                 - The type of document that the daily Congressional Record is (e.g. PDF, "Formatted Text").
              - `<url>`
                 - The daily Congressional Record's URL.
          - `<sections>`
              - Container for section items. A `<sections>` element may include the following children:
            - `<item>`
              - Container for a section item. An `<item>` element may include the following children:
              - `<name>`
                 - The section name of the daily Congressional Record issue.
              - `<startPage>`
                 - The start page of the daily Congressional Record section. (e.g. D291)
              - `<endPage>`
                 - The end page of the daily Congressional Record section. (e.g. D296)
              - `<text>`
                - Container for section text items. A `<text>` element may include the following children:
                - `<item>`
                  - Container for a section text item. An `<item>` element may include the following children:
                  - `<part>`
                     - The part of the daily Congressional Record issue.
                  - `<type>`
                     - The type of document that the daily Congressional Record is (e.g. PDF, "Formatted Text").
                  - `<url>`
                     - The daily Congressional Record's URL for the section. 
            - `<articles>`
                - Container for articles. An `<articles>` element may include the following children:
                  - `<count>`
                     - The number of articles in the daily Congressional Record issue.
                  - `<url>`
                     - The daily Congressional Record's URL for articles. 
  
### Articles Sub-Level

  `<api-root>`

  The `<api-root>` is only present in the XML format.

 `<articles>`

 Parent container for the daily Congressional Record articles. An `<articles>` element may include the following children:

   - `<section>`
      - Container for articles in a section. A `<section>` element may include the following children:
        - `<name>`
           - The section name (e.g., Senate).
        - `<sectionArticles>`
           - Container for section article items. A `<sectionArticles>` element may include the following children:
          - `<item>`
            - Container for a section article. An `<item>` element may include the following children:
            - `<title>`
              - The title of the article.
            - `<startPage>`
              - The start page of the daily Congressional Record article. (e.g. D291)
            - `<endPage>`
              - The end page of the daily Congressional Record article. (e.g. D296)
            - `<text>`
              - The container for article text items.  A `<text>` element may include the following children:
                - `<item>`
                   - Container for an article text item. An `<item>` element may include the following children:
                   - `<type>`
                      - The type of document that the daily Congressional Record article is (e.g. PDF, "Formatted Text").
                   - `<url>`
                      - The article URL.
     
================================================
File: /api_client/python/cdg_client.py
================================================
"""
    CDG Client - An example client for the Congress.gov API.

    @copyright: 2022, Library of Congress
    @license: CC0 1.0
"""
from urllib.parse import urljoin

import requests


API_VERSION = "v3"
ROOT_URL = "https://api.congress.gov/"
RESPONSE_FORMAT = "json"


class _MethodWrapper:
    """ Wrap request method to facilitate queries.  Supports requests signature. """

    def __init__(self, parent, http_method):
        self._parent = parent
        self._method = getattr(parent._session, http_method)

    def __call__(self, endpoint, *args, **kwargs):  # full signature passed here
        response = self._method(
            urljoin(self._parent.base_url, endpoint), *args, **kwargs
        )
        # unpack
        if response.headers.get("content-type", "").startswith("application/json"):
            return response.json(), response.status_code
        else:
            return response.content, response.status_code


class CDGClient:
    """ A sample client to interface with Congress.gov. """

    def __init__(
        self,
        api_key,
        api_version=API_VERSION,
        response_format=RESPONSE_FORMAT,
        raise_on_error=True,
    ):
        self.base_url = urljoin(ROOT_URL, api_version) + "/"
        self._session = requests.Session()

        # do not use url parameters, even if offered, use headers
        self._session.params = {"format": response_format}
        self._session.headers.update({"x-api-key": api_key})

        if raise_on_error:
            self._session.hooks = {
                "response": lambda r, *args, **kwargs: r.raise_for_status()
            }

    def __getattr__(self, method_name):
        """Find the session method dynamically and cache for later."""
        method = _MethodWrapper(self, method_name)
        self.__dict__[method_name] = method
        return method


================================================
File: /api_client/python/.gitignore
================================================
__pycache__
*.py[cod]
*$py.class

# Distribution / packaging
.Python build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec

# Log files
pip-log.txt
pip-delete-this-directory.txt
*.log

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Translations
*.mo
*.pot

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pyflow
__pypackages__/

# Environment
.env
.venv
env/
venv/
ENV/

# If you are using PyCharm #
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/dictionaries
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.xml
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/gradle.xml
.idea/**/libraries
*.iws /out/

# Sublime Text
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project

# sftp configuration file
sftp-config.json

# Package control specific files Package
Control.last-run
Control.ca-list
Control.ca-bundle
Control.system-ca-bundle
GitHub.sublime-settings

# Visual Studio Code #
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history

================================================
File: /api_client/python/bill_example.py
================================================
#!/usr/bin/env python3
"""
    CDG Examples

    Below are some examples of using the Bill endpoint with XML parsing.

    @copyright: 2022, Library of Congress
    @license: CC0 1.0
"""
import xml.etree.ElementTree as ET
# from lxml import etree as ET  # lxml is faster, but an extra download.

from cdg_client import CDGClient


BILL_HR = "hr"
BILL_NUM = 21
BILL_PATH = "bill"
CONGRESS = 117
parse_xml = lambda data: ET.fromstring(data)  # from bytes, more accurately


def print_items(items):
    """Print the items found."""
    for i, item in enumerate(items):

        print(f"{i + 1:2}. {item.tag}:")
        for field in item:
            if field.text:
                print(f"   - {field.tag + ':':20} {field.text.strip()!r}")

    # print(root.xpath("count(.//bills/bill)"), 'bills') # lxml implements count()


def get_bill(client):
    """
    'https://api.congress.gov/v3/bill'
    this API returns, list of latest bills
    """
    data, status_code = client.get(BILL_PATH)
    print("response data:", data[:70] + b"...", "status:", status_code)


def get_bill_congress(client):
    """
    'https://api.congress.gov/v3/bill/117'
    this API returns, list of Congress bill that's picked

    Bill list by Congress
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}"
    data, _ = client.get(endpoint)
    root = parse_xml(data)

    print_items(root.findall(".//bills/bill"))


def get_bill_list_type(client):
    """
    'https://api.congress.gov/v3/bill/117/hr'

    Bill list by Type
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/"
    data, _ = client.get(endpoint)
    root = parse_xml(data)

    print_items(root.findall(".//bills/bill"))


def get_bill_detail(client):
    """
    'https://api.congress.gov/v3/bill/117/hr/21'
    This API returns list of all Bill details
    Bill Details
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/{BILL_NUM}"
    data, _ = client.get(endpoint)
    root = parse_xml(data)

    print_items(root.findall(".//bill"))


def get_bill_action(client):
    """
    'https://api.congress.gov/v3/bill/117/hr/21/actions'
    This API returns, Actions of the specified Bill
    Bill Action
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/{BILL_NUM}/actions"
    data, _ = client.get(endpoint)
    root = parse_xml(data)

    print_items(root.findall(".//actions/item"))  # https://professionalsuperhero.com/


def get_bill_amendments(client):
    """
    'https://api.congress.gov/v3/bill/117/hr/21/amendments'
    This API returns, Amendments of the specified Bill
    Bill Amendments
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/{BILL_NUM}/amendments"
    client.get(endpoint)


def get_bill_committee(client):
    """
    'https://api.congress.gov/v3/bill/117/hr/21/committees'
    This API returns, Committees of the specified Bill
    Bill Committees
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/{BILL_NUM}/committees"
    client.get(endpoint)


def get_bill_cosponsors(client):
    """
    'https://api.congress.gov/v3/bill/117/hr/21/cosponsors'
    This API returns, cosponsors of the specified Bill
    Bill Cosponsors
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/{BILL_NUM}/cosponsors"
    client.get(endpoint)


def get_bill_relatedbills(client):
    """
    'https://api.congress.gov/v3/bill/117/hr/21/relatedbills'
    This API returns, relatedbills of the specified Bill
    Bill Relatedbills
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/{BILL_NUM}/relatedbills"
    client.get(endpoint)


def get_bill_subjects(client):
    """
    'https://api.congress.gov/v3/bill/117/hr/21/subjects'
    This API returns, relatedbills of the specified Bill
    Bill subjects
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/{BILL_NUM}/subjects"
    client.get(endpoint)


def get_bill_summaries(client):
    """
    'https://api.congress.gov/v3/bill/117/hr/21/summaries'
    This API returns, summaries of the specified Bill
    Bill subjects
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/{BILL_NUM}/summaries"
    client.get(endpoint)


def get_bill_text(client):
    """
    'https://api.congress.gov/v3/bill/117/hr/21/text'
    This API returns, text of the specified Bill
    Bill subjects
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/{BILL_NUM}/text"
    client.get(endpoint)


def get_bill_titles(client):
    """
    'https://api.congress.gov/v3/bill/117/hr/21/titles'
    This API returns, titles of the specified Bill
    Bill titles
    """
    endpoint = f"{BILL_PATH}/{CONGRESS}/{BILL_HR}/{BILL_NUM}/titles"
    client.get(endpoint)


if __name__ == "__main__":
    """
    to run the file command :
        python bill.py <optional api version v3/v4>
        Example - python bill.py v3 or python bill.py
    """
    # This section demonstrates how to store your key in a config file that should be
    # out of the source code repo and in a secure location only readable by the user
    # of your application:
    from configparser import ConfigParser

    config = ConfigParser()
    config.read("../secrets.ini")
    api_key = config.get("cdg_api", "api_auth_key")

    # if you want to view data in json format, you can change the output type here:
    client = CDGClient(api_key, response_format="xml")

    print(f"Contacting Congress.gov, at {client.base_url} ...")
    pause = lambda: input('\nPress Enter to continue…')

    try:

        get_bill(client)
        pause()
        get_bill_congress(client)
        pause()
        get_bill_list_type(client)
        pause()
        get_bill_detail(client)
        pause()
        get_bill_action(client)
        pause()
        get_bill_amendments(client)
        pause()
        get_bill_committee(client)
        pause()
        get_bill_cosponsors(client)
        pause()
        get_bill_relatedbills(client)
        pause()
        get_bill_subjects(client)
        pause()
        get_bill_summaries(client)
        pause()
        get_bill_text(client)
        pause()
        get_bill_titles(client)

    except OSError as err:
        print('Error:', err)


================================================
File: /api_client/python/bill_example_output.txt
================================================
Output:

Bill: HR21

    Congress:117

    Actions(10):

        01/06/2021 1: "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs." -Senate

        01/05/2021 2: "Motion to reconsider laid on the table Agreed to without objection" -House floor actions

        01/05/2021 3: "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H58-60)" -house

        01/05/2021 4: "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote.(text: CR H58-60)" -House

        01/05/2021 5: "DEBATE - The House proceeded with forty minutes of debate on H.R. 21" -House

        01/05/2021 6: "Considered under suspension of the rules. (consideration: CR H58-62)" -House

        01/05/2021 7: "Mrs. Maloney, Carolyn B. moved to suspend the rules and pass the bill" -House

        01/04/2021 8: "Referred to the House Committee on Oversight and Reform" -House

        01/04/2021 9&10: "Introduced in House" -House

    Amendments(0):

    Committees(2):

        01/07/2021 1: "Homeland Security and Governmental Affairs Committee" -Senate

        01/04/2021 2: "Oversight and Reform Committee" -House

    Cosponsors (2):

        Rep. Comer, James [R-KY-1]

        Rep. Hice, Jody B. [R-GA-10]

    RelatedBills(1):

        S3099(Federal Secure Cloud Improvement and Jobs Act of 2021) - Congress 117

    Subjects(14):

        1: "Administrative law and regulatory procedures"

        2: "Advisory bodies"

        3: "Computer security and identity theft"

        4: "Computers and information technology"

        5: "Congressional oversight"

        6: "General Services Administration"

        7: "Government employee pay, benefits, personnel management"

        8: "Government information and archives"

        9: "Government studies and investigations"

        10: "Intergovernmental relations"

        11: "Internet and video services"

        12: "Internet, web applications, social media"

        13: "Public participation and lobbying"

        14: "Government Operations and Politics"

    Summaries(2):

       01/04/2021 :"<p><b>Federal Risk and Authorization Management Program Authorization Act of 2021 or the FedRAMP Authorization Act</b></p> <p>This bill provides statutory authority for the Federal Risk and Authorization Management Program (FedRAMP) within the General Services Administration (GSA).</p> <p>The GSA must establish a government-wide program that provides the authoritative standardized approach to security assessment and authorization for cloud computing products and services that process unclassified information used by agencies. Agencies must ensure that their cloud computing services meet GSA requirements.</p> <p>The bill establishes the Joint Authorization Board to conduct security assessments of cloud computing services and issue provisional authorizations to operate to cloud service providers that meet FedRAMP security guidelines.</p> <p>The GSA shall (1) publish a report that includes an assessment of the cost incurred by agencies and cloud service providers related to the issuance of FedRAMP authorizations and provisional authorizations, (2) determine the requirements for certification of independent assessment organizations, and (3) establish the Federal Secure Cloud Advisory Committee.</p>" - Inroduced in House

       01/05/2021 :" <p><b>Federal Risk and Authorization Management Program Authorization Act of 2021 or the FedRAMP Authorization Act</b></p> <p>This bill provides statutory authority for the Federal Risk and Authorization Management Program (FedRAMP) within the General Services Administration (GSA).</p> <p>The GSA must establish a government-wide program that provides the authoritative standardized approach to security assessment and authorization for cloud computing products and services that process unclassified information used by agencies. Agencies must ensure that their cloud computing services meet GSA requirements.</p> <p>The bill establishes the Joint Authorization Board to conduct security assessments of cloud computing services and issue provisional authorizations to operate to cloud service providers that meet FedRAMP security guidelines.</p> <p>The GSA shall (1) publish a report that includes an assessment of the cost incurred by agencies and cloud service providers related to the issuance of FedRAMP authorizations and provisional authorizations, (2) determine the requirements for certification of independent assessment organizations, and (3) establish the Federal Secure Cloud Advisory Committee.</p>" - Passed House

    TextVersions(3):

        01/06/2021: Received in senate - HTML, Text, PDF, and XML

        01/05/2021: Engrossed in House - HTML, Text, PDF, and XML

        01/04/2021: Introduced in House - HTML, Text, PDF, and XML

    Titles (8):

        Short Title 1: Display Title
        Official Title 1: FedRAMP Authorization Act

        Short Title 2: Official Title as Introduced
        Official Title 2: To enhance the innovation, security, and availability of cloud computing products and services used in the Federal Government by establishing the Federal Risk and Authorization Management Program within the General Services Administration and by establishing a risk management, authorization, and continuous monitoring process to enable the Federal Government to leverage cloud computing products and services using a risk-based approach consistent with the Federal Information Security Modernization Act of 2014 and cloud-based operations, and for other purposes.

        Short Title 3: Short Title(s) as Passed House
        Official Title 3: FedRAMP Authorization Act

        Short Title 4: Short Title(s) as Passed House
        Official Title 4: Federal Risk and Authorization Management Program Authorization Act of 2021

        Short Title 5: Short Title(s) as Introduced
        Official Title 5: FedRAMP Authorization Act

        Short Title 6: Short Title(s) as Introduced
        Official Title 6: Federal Risk and Authorization Management Program Authorization Act of 2021

        Short Title 7: Short Titles as Passed House
        Official Title 7: Federal Risk and Authorization Management Program Authorization Act of 2021

        Short Title 8: Short Titles as Passed House
        Official Title 8: FedRAMP Authorization Act


================================================
File: /api_client/python/cdg_cli
================================================
#!/usr/bin/env python3
"""
    CDG CLI - An example of secure API Key handling for the Congress.gov API.

    Rather than keeping the API key in source code or given at the command-line
    to be easily copied, we prompt for it and then store it in the Operating
    System's "keyring" storage.  This is a secure place for secrets.

    Example:
        ⏵ cdg_cli --prompt-key  # ENTER
        Password: ••••••••••••••••••••••••••••••••
          INFO     API Key was saved.

        ⏵ cdg_cli bill/117/hr/21/committees
          INFO     __main__/main:101 HTTP Status: 200
          INFO     __main__/main:102 API Returned:
        {'committees': [{'activities': [{'date': '2021-01-07T01:26:34Z',
                                         'name': 'Referred to'}],
         ...

    @copyright: 2022, Library of Congress
    @license: CC0 1.0
"""
import sys, os
import logging


__version__ = '0.90'
log = logging.getLogger(__name__)
CDG_SYSTEM_NAME = 'CDG_API'
CDG_USER = 'API_KEY'  # informational only


def setup():
    """ Parse command line, validate, initialize logging, etc ."""
    from argparse import ArgumentParser, RawTextHelpFormatter

    parser = ArgumentParser(
        description=__doc__, formatter_class=RawTextHelpFormatter
    )
    parser.add_argument(
        'endpoint', nargs="?", help="path to query, i.e. 'bill/117/hr/21/committees'"
    )
    parser.add_argument(
        '--prompt-key',
        action='store_true',
        help='Prompt to store api_key in keyring.\nDo not add key to command-line.',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_const',
        dest='loglvl',
        default=logging.INFO,
        const=logging.DEBUG,
    )
    parser.add_argument(
        '--version', action='version', version='%(prog)s ' + __version__
    )

    # parse and validate
    args = parser.parse_args()

    # start logging
    logging.basicConfig(
        level=args.loglvl,
        stream=sys.stdout,
        format='  %(levelname)-8.8s %(name)s/%(funcName)s:%(lineno)03i %(message)s',
    )
    logging.captureWarnings(True)
    log.debug('arguments: %s', args)
    import keyring

    if args.prompt_key:
        from getpass import getpass

        api_key = getpass('API Key: ')
        if api_key:
            keyring.set_password(CDG_SYSTEM_NAME, CDG_USER, api_key)
            log.info('API Auth Key was saved.')
            sys.exit(os.EX_OK)
        else:
            log.warning('API Auth Key may not be empty, aborting.')
            sys.exit(os.EX_NOINPUT)
    else:
        if not keyring.get_password(CDG_SYSTEM_NAME, CDG_USER):
            parser.error('api_key has not been set, see -h to explain --prompt-key')
        if not args.endpoint:
            parser.error('endpoint parameter is required.')

    return args


def main(args):
    """ Let's get started. """
    from pprint import pformat  # defer imports in favoer of startup speed
    from keyring import get_password
    from cdg_client import CDGClient

    status = os.EX_OK
    try:
        client = CDGClient(
            get_password(CDG_SYSTEM_NAME, CDG_USER), raise_on_error=False
        )

        #
        # Code goes code here:
        # below is a simple example:
        #
        result,  status_code = client.get(args.endpoint)
        log.info('HTTP Status: %s', status_code)
        log.info('API Returned:\n%s', pformat(result))


    except IOError as err:
        status = os.EX_IOERR
        log.error('%s', err)

    except Exception:
        status = os.EX_SOFTWARE
        log.exception("unexpected error:")

    return status


if __name__ == '__main__':

    sys.exit(main(setup()))


================================================
File: /api_client/python/README.md
================================================
# CDG Example Client with Python

## Table of contents

- [Requirements](#requirements)
- [API Credentials](#api-credentials)
- [Typical Use of CDGClient](#typical-use-of-cdgclient)
- [Examples](#examples)
- [Configurable options](#configurable-options)
- [How to talk to various endpoints](#how-to-talk-to-various-endpoints)  
- [Client arguments](#client-arguments)
- [Additional Information](#additional-information)

## Requirements

This client with developed and tested with Python 3.8 so should work with that version
and above. We have tested with older Python versions.

This example client requires the `requests` package, and optionally the `keyring`
package.
They may be installed with one of the the following commands:

```shell
⏵ python3 -m pip install requests keyring        # X-platform
⏵ apt install python3-requests python3-keyring   # Debian

```

`lxml` might be useful as well, if you expect to be using and parsing a lot of XML.
JSON is the default data serialization format.

On Unix, you may want to directly run the example scripts as executable files,
though they work after the `python` command as well:

```bash
⏵ chmod a+x cdg_cli bill_example.py
```

Windows folks will probably need to type `python` before any scripts,
assuming python is on your PATH.

## API Credentials

Sign up for and retrieve your API key from <https://api.congress.gov/sign-up>

## Typical Use of CDGClient

```python
from cdg_client import CDGClient  # make it available

client = CDGClient(api_key)  # pass the key, response_format="xml" if needed

# use requests args and kwargs below modify the request:
data, status_code = client.get(endpoint, *args, **kwargs)

# JSON data is pre-parsed, XML will need
# import xml.etree.ElementTree as ET
# root = ET.fromstring(data)

# go to town!
```

## Examples

Below are a few fleshed out examples.

### Command line interface ➧ `cdg_cli`

`cdg_cli` is an example of:

- Using the CDGClient class.
- Making simple queries at the command-line.
- How to use the "keyring" functionality of your OS.
- Using the JSON format, data is returned as native data structures.

First, you'll need to enter your API Auth key at the prompt.

That is, wait for the prompt, do *not* put it on the command-line proper:

```sh
⏵ python cdg_cli --prompt-key # Enter, do *not* pass API Auth key here ✗

API Key:               # Do paste it here ✓

  INFO     API Key was saved.

# Now you can run it
```

Now, to look at bill/hr/21/committeess, write:

```sh
⏵ python cdg_cli bill/117/hr/21/committees
  INFO     __main__/main:111 HTTP Status: 200
  INFO     __main__/main:112 API Returned:
```

```json
{
    "committees": [
        {
            "activities": [
                {
                    "date": "2021-01-07T01: 26: 34Z",
                    "name": "Referred to"
                }
            ],
            "chamber": "Senate",
            "name": "Homeland Security and Governmental Affairs Committee",
            "subcommittees": [],
            "systemCode": "ssga00",
            "type": "Standing",
            "url": "https: //api.congress.gov/v3/committee/senate/ssga00?format=json"
        },
        {
            "activities": [
                {
                    "date": "2021-01-04T15:11:25Z",
                    "name": "Referred to"
                }
            ],
            "chamber": "House",
            "name": "Oversight and Reform Committee",
            "subcommittees": [],
            "systemCode": "hsgo00",
            "type": "Standing",
            "url": "https://api.congress.gov/v3/committee/house/hsgo00?format=json"
        }
    ],
    "request": {
        "billNumber": "21",
        "billType": "hr",
        "billUrl": "https://api.congress.gov/v3/bill/117/hr/21?format=json",
        "congress": "117",
        "contentType": "application/json",
        "format": "json"
    }
}
```

## Configurable options

| Key                      | Description                                                        | Values                                       |
|--------------------------|--------------------------------------------------------------------|----------------------------------------------|
| *API_KEY*                | The API key used to authenticate calls                             | Retrieved from <https://api.congress.gov>      |
| *RESPONSE_FORMAT*        | Sets the response format returned by the API                       | xml, json                                    |
| *BILL.CONGRESS*          | The numerical value of the congress to query                       | 1 - 117 (or current congress)                |
| *BILL.CHAMBER*           | The congressional chamber                                          | hr, s, sjres, hjres                          |
| *BILL.NUMBER*            | The bill number to query                                           | A valid bill number from <https://congress.gov> |
| *BILL.URL*               | The bill url for the API to query                                  | bill                                         |

### How to talk to various endpoints

`bill_example` is an example of:

- Using the CDGClient class
- How the endpoints are structured.
- Using an external "secrets" config file.
- Using the XML format.

```sh
⏵  python3 bill_example.py
 1. bill:
   - congress:            '117'
   - type:                'HR'
   - originChamber:       'House'
   - originChamberCode:   'H'
   - number:              '5681'
   - url:                 'https://api.congress.gov/v3/bill/117/hr/5681?format=xml'
   - title:               'Shadow Wolves Enhancement Act'
   - latestAction:        ''
   - updateDate:          '2022-04-08'
 ...
```

## Client arguments

Other options allowed as arguments to python bill_example.py are:

| Argument             | Description                              |
|----------------------|------------------------------------------|
| *help*               | Displays the help message                |
| *all_bill_calls*     | Runs all of the defined bill API calls   |
| *bills_get_all*      | Gets all bills                           |
| *bills_by_congress*  | Gets all bills by the specified congress |
| *bills_by_chamber*   | Gets all bills by the specified chamber  |
| *bill*               | Gets a specific bill                     |
| *bill_actions*       | Gets a bills actions                     |
| *bill_amendments*    | Gets a bills amendments                  |
| *bill_committees*    | Gets a bills committees                  |
| *bill_cosponsors*    | Gets a bills cosponsors                  |
| *bill_related_bills* | Gets a bills related bills               |
| *bill_subjects*      | Gets a bills subjects                    |
| *bill_summaries*     | Gets a bills summaries                   |
| *bill_texts*         | Gets a bills texts                       |
|  *bill_titles*       | Gets a bills titles                      |

## Additional Information

- For more information and the full API reference, please visit <https://api.congress.gov/>
- Alternative ways to make use of your API key when making calls can be found here: <https://api.data.gov/docs/api-key/>

---
© 2022, Library of Congress via Congress.gov


