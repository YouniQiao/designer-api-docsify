# Template

指定订阅中的模板结构。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-dataShare-interface Template--><!--Device-dataShare-interface Template-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## predicates

```TypeScript
predicates: Record<string, string>
```

指定模板的谓词。当调用  
[on](dataShare.DataShareHelper.on(type: 'rdbDataChange', uris: Array&lt;string&gt;, templateId: TemplateId, callback: AsyncCallback&lt;RdbDataChangeNode&gt;))的回调时，谓词用于生成数据。仅适用于rdb存储数据。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Template-predicates: Record<string, string>--><!--Device-Template-predicates: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## scheduler

```TypeScript
scheduler: string
```

指定模板的调度程序sql。其中嵌入自定义函数处理，目前预置自定义函数remindTimer处理。remindTimer在指定场景触发一次订阅刷新。

触发场景：

1. 修改数据时且有订阅的情况下触发对应的调度程序sql语句。2. 添加对应库第一个订阅的情况下触发对应的调度程序sql语句。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Template-scheduler: string--><!--Device-Template-scheduler: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## update

```TypeScript
update?: string
```

指定模板的update sql语句，未定义时默认值为空字符串。当调用  
[on](dataShare.DataShareHelper.on(type: 'rdbDataChange', uris: Array&lt;string&gt;, templateId: TemplateId, callback: AsyncCallback&lt;RdbDataChangeNode&gt;))的回调时，update参数用于更新数据。仅适用于rdb存储数据。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Template-update?: string--><!--Device-Template-update?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

