# BlankScreenDetectionConfig

The strategy of blank screen detection.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface BlankScreenDetectionConfig--><!--Device-unnamed-export declare interface BlankScreenDetectionConfig-End-->

**System capability:** SystemCapability.Web.Webview.Core

## contentfulNodesCountThreshold

```TypeScript
contentfulNodesCountThreshold?: int
```

When using the specific detection method of detecting contentful nodes, the threshold is used to determine how close the detection is to being blank screen page.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-BlankScreenDetectionConfig-contentfulNodesCountThreshold?: int--><!--Device-BlankScreenDetectionConfig-contentfulNodesCountThreshold?: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

## detectionMethods

```TypeScript
detectionMethods?: BlankScreenDetectionMethod[]
```

The combination of blank screen detection methods.

**Type:** [BlankScreenDetectionMethod](arkts-web-blankscreendetectionmethod-e.md)[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-BlankScreenDetectionConfig-detectionMethods?: BlankScreenDetectionMethod[]--><!--Device-BlankScreenDetectionConfig-detectionMethods?: BlankScreenDetectionMethod[]-End-->

**System capability:** SystemCapability.Web.Webview.Core

## detectionTiming

```TypeScript
detectionTiming?: double[]
```

The settings of the timing when web try to detect current page is blank or not. The timing is the duration after web navigation. <br>Length range:[0,+∞).Unit: second.Default value:[1.0,3.0,5.0].

**Type:** double[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-BlankScreenDetectionConfig-detectionTiming?: double[]--><!--Device-BlankScreenDetectionConfig-detectionTiming?: double[]-End-->

**System capability:** SystemCapability.Web.Webview.Core

## enable

```TypeScript
enable: boolean
```

Enable blank screen detection or not.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-BlankScreenDetectionConfig-enable: boolean--><!--Device-BlankScreenDetectionConfig-enable: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

