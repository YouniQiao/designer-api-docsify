# SecurityParams

Defines the parameters for enableAdvancedSecurityMode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-webview-interface SecurityParams--><!--Device-webview-interface SecurityParams-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## disableJITCompilation

```TypeScript
disableJITCompilation?: boolean
```

Decide whether JIT is disabled, the default value is false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityParams-disableJITCompilation?: boolean--><!--Device-SecurityParams-disableJITCompilation?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## disableMathML

```TypeScript
disableMathML?: boolean
```

Decide whether MathML is disabled, the default value is false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityParams-disableMathML?: boolean--><!--Device-SecurityParams-disableMathML?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## disableNonProxyUDP

```TypeScript
disableNonProxyUDP?: boolean
```

Decide whether NonProxyUDP is disabled, the default value is false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityParams-disableNonProxyUDP?: boolean--><!--Device-SecurityParams-disableNonProxyUDP?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## disablePDFViewer

```TypeScript
disablePDFViewer?: boolean
```

是否禁用PDF查看器。true表示禁用，false表示不禁用。默认值：false。内置PDF解析引擎在解析复杂二进制格式和嵌入式脚本时容易存在漏洞，攻击者可构造特殊PDF文件利用字体解析或内存破坏漏洞控制应用主进程。禁用后无法在ArkWeb中加载PDF。非文档办公类App建议禁用，引导用户使用外部应用打开PDF。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityParams-disablePDFViewer?: boolean--><!--Device-SecurityParams-disablePDFViewer?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## disableServiceWorker

```TypeScript
disableServiceWorker?: boolean
```

Decide whether ServiceWorker is disabled, the default value is false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityParams-disableServiceWorker?: boolean--><!--Device-SecurityParams-disableServiceWorker?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## disableWebAssembly

```TypeScript
disableWebAssembly?: boolean
```

Decide whether WASM is disabled, the default value is false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityParams-disableWebAssembly?: boolean--><!--Device-SecurityParams-disableWebAssembly?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## disableWebGL

```TypeScript
disableWebGL?: boolean
```

Decide whether WebGL is disabled, the default value is false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityParams-disableWebGL?: boolean--><!--Device-SecurityParams-disableWebGL?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

