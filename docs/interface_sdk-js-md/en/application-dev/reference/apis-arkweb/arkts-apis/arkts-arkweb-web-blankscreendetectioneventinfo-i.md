# BlankScreenDetectionEventInfo

Defines the blank screen detection event info.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BlankScreenDetectionEventInfo--><!--Device-unnamed-export declare interface BlankScreenDetectionEventInfo-End-->

**System capability:** SystemCapability.Web.Webview.Core

## blankScreenDetails

```TypeScript
blankScreenDetails?: BlankScreenDetails
```

The details of this detection result.

**Type:** [BlankScreenDetails](arkts-arkweb-web-blankscreendetails-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BlankScreenDetectionEventInfo-blankScreenDetails?: BlankScreenDetails--><!--Device-BlankScreenDetectionEventInfo-blankScreenDetails?: BlankScreenDetails-End-->

**System capability:** SystemCapability.Web.Webview.Core

## blankScreenReason

```TypeScript
blankScreenReason: DetectedBlankScreenReason
```

The reason why we consider this page is blank.

**Type:** [DetectedBlankScreenReason](arkts-arkweb-web-detectedblankscreenreason-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BlankScreenDetectionEventInfo-blankScreenReason: DetectedBlankScreenReason--><!--Device-BlankScreenDetectionEventInfo-blankScreenReason: DetectedBlankScreenReason-End-->

**System capability:** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

The url of detected blank screen page.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BlankScreenDetectionEventInfo-url: string--><!--Device-BlankScreenDetectionEventInfo-url: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

