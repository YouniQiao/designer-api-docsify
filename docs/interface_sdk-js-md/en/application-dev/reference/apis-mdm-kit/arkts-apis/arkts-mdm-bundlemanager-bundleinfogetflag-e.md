# BundleInfoGetFlag

包信息获取标志，指示需要获取的包信息的内容。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-bundleManager-export enum BundleInfoGetFlag--><!--Device-bundleManager-export enum BundleInfoGetFlag-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## DEFAULT

```TypeScript
DEFAULT = 0
```

用于获取默认包信息，不包含applicationInfo、signatureInfo的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleInfoGetFlag-DEFAULT = 0--><!--Device-BundleInfoGetFlag-DEFAULT = 0-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## WITH_APPLICATION_INFO

```TypeScript
WITH_APPLICATION_INFO = 1 << 0
```

用于获取默认包信息和applicationInfo的信息，获取的applicationInfo中不包含iconData的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleInfoGetFlag-WITH_APPLICATION_INFO = 1 << 0--><!--Device-BundleInfoGetFlag-WITH_APPLICATION_INFO = 1 << 0-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## WITH_SIGNATURE_INFO

```TypeScript
WITH_SIGNATURE_INFO = 1 << 1
```

用于获取默认包信息和signatureInfo的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleInfoGetFlag-WITH_SIGNATURE_INFO = 1 << 1--><!--Device-BundleInfoGetFlag-WITH_SIGNATURE_INFO = 1 << 1-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## WITH_APPLICATION_ICON_INFO

```TypeScript
WITH_APPLICATION_ICON_INFO = 1 << 2
```

用于获取默认包信息和applicationInfo的iconData信息。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleInfoGetFlag-WITH_APPLICATION_ICON_INFO = 1 << 2--><!--Device-BundleInfoGetFlag-WITH_APPLICATION_ICON_INFO = 1 << 2-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

