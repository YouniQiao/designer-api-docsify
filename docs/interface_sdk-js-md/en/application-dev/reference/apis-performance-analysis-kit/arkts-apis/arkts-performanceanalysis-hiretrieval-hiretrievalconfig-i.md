# HiRetrievalConfig

应用灰度活动配置。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-hiRetrieval-interface HiRetrievalConfig--><!--Device-hiRetrieval-interface HiRetrievalConfig-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

## Modules to Import

```TypeScript
import { hiRetrieval } from 'kits/@kit.PerformanceAnalysisKit';
```

## deviceModel

```TypeScript
deviceModel: string
```

设备型号参数，用于标识具体设备型号（具体值由开发者根据业务需求定义）。参数值由开发者自定义，无格式和字符类型限制，最长支持128个字符，超出部分将被截断。这些参数将作为算法输入，影响灰度圈选策略。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HiRetrievalConfig-deviceModel: string--><!--Device-HiRetrievalConfig-deviceModel: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

## deviceType

```TypeScript
deviceType: string
```

设备类型参数，用于标识设备分类特征（具体值由开发者根据业务需求定义）。参数值由开发者自定义，无格式和字符类型限制，最长支持128个字符，超出部分将被截断。这些参数将作为算法输入，影响灰度圈选策略。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HiRetrievalConfig-deviceType: string--><!--Device-HiRetrievalConfig-deviceType: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

## userType

```TypeScript
userType: string
```

用户类型参数，用于标识用户群体特征，如'newUser'、'vipUser'等。参数值由开发者自定义，无格式和字符类型限制，最长支持128个字符，超出部分将被截断。这些参数将作为算法输入，影响灰度圈选策略。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HiRetrievalConfig-userType: string--><!--Device-HiRetrievalConfig-userType: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

