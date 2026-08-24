# CustomComponentV2

自定义组件V2

**继承/实现关系：** CustomComponentV2 extends [BaseCustomComponent](arkts-arkui-basecustomcomponent-c.md)

**起始版本：** 18

<!--Device-unnamed-declare class CustomComponentV2--><!--Device-unnamed-declare class CustomComponentV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## aboutToReuse

```TypeScript
aboutToReuse?(): void
```

当一个状态管理V2的可复用自定义组件从复用缓存中重新加入到节点树时，触发aboutToReuse生命周期回调。在频繁调用场景下，应避免在其中执行耗时操作，否则可能导致丢帧卡顿。详细内容请参考[\@ReusableV2](../../../ui/state-management/arkts-new-reusableV2.md)。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CustomComponentV2-aboutToReuse?(): void--><!--Device-CustomComponentV2-aboutToReuse?(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
export class Message {
  value: string | undefined;

  constructor(value: string) {
    this.value = value;
  }
}

@Entry
@Component
struct Index {
  @State isShown: boolean = true;

  build() {
    Column() {
      // 点击Button切换isShown，控制Child从组件树移除或重新加入
      Button('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.isShown = !this.isShown;
        })
      if (this.isShown) {
        Child({ message: new Message('Child') })
      }
    }
    .height('100%')
    .width('100%')
  }
}

@Reusable
@Component
struct Child {
  @State message: Message = new Message('AboutToReuse');

  aboutToReuse(params: Record<string, ESObject>) {
    console.info('Reuse Child');
    this.message = params.message as Message;
  }

  build() {
    Column() {
      Text(this.message.value)
        .fontSize(20)
    }
    .borderWidth(2)
    .height(100)
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Column, Button, Component, Reusable, ClickEvent, Text, ReuseObject } from "@ohos.arkui.component"
import { State } from "@ohos.arkui.stateManagement"
import hilog from '@ohos.hilog'

export class Message {
  value: string | undefined;

  constructor(value: string) {
    this.value = value
  }
}

@Entry
@Component
struct Index {
  @State isSwitch: boolean = true

  build() {
    Column() {
      Button('Hello World')
        .fontSize(50)
        .onClick(() => {
          this.isSwitch = !this.isSwitch
        })
      if (this.isSwitch) {
        Child({ message: new Message('Child1') })
      } else {
        Child({ message: new Message('Child2') })
      }
    }
    .height("100%")
    .width('100%')
  }
}

@Reusable
@Component
struct Child {
  @State message: Message = new Message('AboutToReuse');

  aboutToReuse(params: ReuseObject) {
    if (params.has('message')) {
      this.message = params['message'] as Message
    }
  }

  build() {
    Column() {
      Text(this.message.value)
        .fontSize(20)
    }
    .borderWidth(2)
    .height(100)
  }
}
```

ArkTS-Dyn示例：

```TypeScript
@Entry
@ComponentV2
struct Index {
  @Local condition: boolean = true;
  build() {
    Column() {
      Button('回收/复用')
        .onClick(() => {
          this.condition = !this.condition;
        }) // 点击切换回收/复用状态
      if (this.condition) {
        ReusableV2Component()
      }
    }
  }
}
@ReusableV2
@ComponentV2
struct ReusableV2Component {
  @Local message: string = 'Hello World';
  aboutToReuse() {
    console.info('ReusableV2Component aboutToReuse'); // 复用时被调用
  }
  build() {
    Column() {
      Text(this.message)
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { Entry, Column, Button, ComponentV2, ReusableV2, Text, Local } from '@kit.ArkUI';
@Entry
@ComponentV2
struct Index {
  @Local condition: boolean = true;
  build() {
    Column() {
      Button('回收/复用').onClick(()=>{this.condition=!this.condition;}) // 点击切换回收/复用状态
      if (this.condition) {
        ReusableV2Component()
      }
    }
  }
}
@ReusableV2
@ComponentV2
struct ReusableV2Component {
  @Local message: string = 'Hello World';
  aboutToReuse() {
    console.info('ReusableV2Component aboutToReuse'); // 复用时被调用
  }
  build() {
    Column() {
      Text(this.message)
    }
  }
}
```

