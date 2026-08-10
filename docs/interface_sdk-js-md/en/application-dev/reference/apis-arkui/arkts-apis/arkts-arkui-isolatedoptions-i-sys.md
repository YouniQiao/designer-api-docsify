# IsolatedOptions (System API)

用于在IsolatedComponent构造时传递构造参数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface IsolatedOptions--><!--Device-unnamed-declare interface IsolatedOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## want

```TypeScript
want: Want
```

要加载的Abc信息。Want对象的parameters中需包含以下字段：&lt;br/&gt;resourcePath：资源路径，需为.hap文件路径；&lt;br/&gt;abcPath：经verifyAbc校验后的Abc文件路径，需以'/abcs'开头；&lt;br/&gt;entryPoint：Abc入口，格式为'bundleName/页面路径'。

**Type:** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IsolatedOptions-want: Want--><!--Device-IsolatedOptions-want: Want-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## worker

```TypeScript
worker: RestrictedWorker
```

运行Abc的受限Worker。

**Type:** [RestrictedWorker](../../apis-arkts/arkts-apis/arkts-arkts-worker-restrictedworker-c-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IsolatedOptions-worker: RestrictedWorker--><!--Device-IsolatedOptions-worker: RestrictedWorker-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

