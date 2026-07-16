# MixedMode

The Web's behavior to load from HTTP or HTTPS. Defaults to MixedMode.None.

**Since:** 8

<!--Device-unnamed-declare enum MixedMode--><!--Device-unnamed-declare enum MixedMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## All

```TypeScript
All = 0
```

Loose mode: Allow a secure origin to load content from any other origin.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MixedMode-All = 0--><!--Device-MixedMode-All = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Compatible

```TypeScript
Compatible = 1
```

Compatible mode: Some insecure content may be allowed to be loaded by a secure origin.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MixedMode-Compatible = 1--><!--Device-MixedMode-Compatible = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## None

```TypeScript
None = 2
```

Strict mode: Not allow a secure origin to load content from an insecure origin.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MixedMode-None = 2--><!--Device-MixedMode-None = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

