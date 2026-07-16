# BlankScreenDetectionConfig

Defines the configuration options of the blank screen detection policy.

**Since:** 22

<!--Device-unnamed-declare interface BlankScreenDetectionConfig--><!--Device-unnamed-declare interface BlankScreenDetectionConfig-End-->

**System capability:** SystemCapability.Web.Webview.Core

## contentfulNodesCountThreshold

```TypeScript
contentfulNodesCountThreshold?: number
```

Threshold for number of detected contentful nodes. This parameter takes effect only when the contentful node detection policy is used.

The value ranges from 0 to the maximum number of nodes in the detection policy. If the value is less than or equal to the threshold, the near-blank screen is triggered.

Default value: **0**.

**Type:** number

**Since:** 22

<!--Device-BlankScreenDetectionConfig-contentfulNodesCountThreshold?: number--><!--Device-BlankScreenDetectionConfig-contentfulNodesCountThreshold?: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

## detectionMethods

```TypeScript
detectionMethods?: BlankScreenDetectionMethod[]
```

Methods of the detection policy. The value is an array.

**NOTE**

1. Duplicate values are ignored.

Default value: **[BlankScreenDetectionMethod.DETECTION_CONTENTFUL_NODES_SEVENTEEN]**.

**Type:** BlankScreenDetectionMethod[]

**Since:** 22

<!--Device-BlankScreenDetectionConfig-detectionMethods?: BlankScreenDetectionMethod[]--><!--Device-BlankScreenDetectionConfig-detectionMethods?: BlankScreenDetectionMethod[]-End-->

**System capability:** SystemCapability.Web.Webview.Core

## detectionTiming

```TypeScript
detectionTiming?: number[]
```

The settings of the timing when web try to detect current page is blank or not.The timing is the duration after web navigation.<br>Length range:[0,+∞).Default value:[1.0,3.0,5.0].<br>1. Duplicate values are ignored.2. The value must be greater than 0. If the value is less than 0, the value is ignored.Unit: second.

**Type:** number[]

**Since:** 22

<!--Device-BlankScreenDetectionConfig-detectionTiming?: number[]--><!--Device-BlankScreenDetectionConfig-detectionTiming?: number[]-End-->

**System capability:** SystemCapability.Web.Webview.Core

## enable

```TypeScript
enable: boolean
```

Whether to enable the blank screen policy.

**Type:** boolean

**Since:** 22

<!--Device-BlankScreenDetectionConfig-enable: boolean--><!--Device-BlankScreenDetectionConfig-enable: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

