# DepthSpaceType (System API)

景深空间类型枚举。

> **说明：**
> 
> 全局模式下，其余进程复用壁纸进程的背景、深度图及相机和光照参数，且不可自定义。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare enum DepthSpaceType--><!--Device-unnamed-declare enum DepthSpaceType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## INSTANCE

```TypeScript
INSTANCE = 0
```

实例模式。使用当前进程的背景、深度图、相机参数及光照参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-DepthSpaceType-INSTANCE = 0--><!--Device-DepthSpaceType-INSTANCE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## GLOBAL

```TypeScript
GLOBAL = 1
```

全局模式。使用全局的背景、深度图、相机参数及光照参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthSpaceType-GLOBAL = 1--><!--Device-DepthSpaceType-GLOBAL = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

