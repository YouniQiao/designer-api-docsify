# DetectedBlankScreenReason

Enumerates the reasons for the blank screen.

**Since:** 22

<!--Device-unnamed-declare enum DetectedBlankScreenReason--><!--Device-unnamed-declare enum DetectedBlankScreenReason-End-->

**System capability:** SystemCapability.Web.Webview.Core

## NO_CONTENTFUL_NODES

```TypeScript
NO_CONTENTFUL_NODES = 0
```

No contentful node is detected.

This may be triggered when the detection policy is **DETECTION_CONTENTFUL_NODES_SEVENTEEN**.

**Since:** 22

<!--Device-DetectedBlankScreenReason-NO_CONTENTFUL_NODES = 0--><!--Device-DetectedBlankScreenReason-NO_CONTENTFUL_NODES = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## SUB_THRESHOLD_CONTENTFUL_NODES

```TypeScript
SUB_THRESHOLD_CONTENTFUL_NODES = 1
```

The number of contentful nodes detected is less than or equal to the threshold.

This may be triggered when the detection policy is **DETECTION_CONTENTFUL_NODES_SEVENTEEN** and **contentfulNodesCountThreshold** is set.

**Since:** 22

<!--Device-DetectedBlankScreenReason-SUB_THRESHOLD_CONTENTFUL_NODES = 1--><!--Device-DetectedBlankScreenReason-SUB_THRESHOLD_CONTENTFUL_NODES = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

