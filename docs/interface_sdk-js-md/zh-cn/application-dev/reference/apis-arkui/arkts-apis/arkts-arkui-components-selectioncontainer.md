# @ohos.arkui.components.SelectionContainer

## 导入模块

```TypeScript
import { OnMenuItemClickWithTextCallback, SelectionContainer, SelectionContainerAttribute, SelectionContainerEditMenuOptions, SelectionContainerInstance, SelectionContainerMenuOptions, SelectionContainerTextJoinStyle, SelectionContainerOptions, SelectionContainerController } from '@kit.ArkUI';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [SelectionContainerAttribute](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-c.md) | 支持[通用属性](../arkts-components/arkts-arkui-commonmethod-c.md)。 |
| [SelectionContainerController](arkts-arkui-arkui-components-selectioncontainer-selectioncontainercontroller-c.md) | SelectionContainer组件的控制器。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [SelectionContainerEditMenuOptions](arkts-arkui-arkui-components-selectioncontainer-selectioncontainereditmenuoptions-i.md) | SelectionContainer自定义编辑菜单选项。 |
| [SelectionContainerInterface](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerinterface-i.md) | 创建一个SelectionContainer组件。 |
| [SelectionContainerMenuOptions](arkts-arkui-arkui-components-selectioncontainer-selectioncontainermenuoptions-i.md) | 配置选择菜单中的选项。 |
| [SelectionContainerOptions](arkts-arkui-arkui-components-selectioncontainer-selectioncontaineroptions-i.md) | 组件初始化配置项。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [SelectionContainerTextJoinStyle](arkts-arkui-arkui-components-selectioncontainer-selectioncontainertextjoinstyle-e.md) | 文本聚合拼接方式。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [OnMenuItemClickWithTextCallback](arkts-arkui-onmenuitemclickwithtextcallback-t.md) | 点击菜单项时触发，可拦截系统默认菜单项（如复制、粘贴菜单项）的执行行为。 |

### 常量

| 名称 | 说明 |
| --- | --- |
| [SelectionContainer](arkts-arkui-arkui-components-selectioncontainer-con.md) | SelectionContainer组件用于为多个文本节点提供跨节点文本选中、复制及菜单扩展能力，支持统一配置选中文本的手柄颜色和底板颜色，支持灵活的文本拼接策略，支持自定义选择菜单和扩展菜单选项。适用于需要跨多个Text组件实现文本连续选中、统一复制、样式自定义及菜单扩展的场景，解决了多Text组件场景下文本选择体验割裂的问题，提升了用户在复杂文本布局中的交互体验。 |
| [SelectionContainerInstance](arkts-arkui-arkui-components-selectioncontainer-con.md#selectioncontainerinstance) | 定义SelectionContainer组件实例。 |

## 示例

该示例通过[SelectionContainer](#接口)、copyOption、[textJoinStyle](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-c.md#textjoinstyle)、onTextSelectionChange、onWillCopy、onCopy接口展示跨多个Text组件选中文本、拼接选中文本并处理复制回调的能力。
从API版本26.0.0开始，新增SelectionContainer组件和copyOption等接口。

```TypeScript
import {
  SelectionContainer,
  SelectionContainerAttribute,
  SelectionContainerTextJoinStyle
} from '@kit.ArkUI';

@Entry
@Component
struct SelectionContainerExample1 {
  @State selectedParts: string[] = [];
  @State copiedText: string = '';

  build() {
    Column({ space: 12 }) {
      Text('请长按下方区域并跨节点选择文本')
        .fontSize(16)

      SelectionContainer() {
        Column({ space: 8 }) {
          Text('第一段文本：SelectionContainer支持跨多个Text组件进行选中。')
            .fontSize(18)
            .copyOption(CopyOptions.InApp)
          Text('第二段文本：选中结果会按照Text组件的视觉顺序进行拼接。')
            .fontSize(18)
            .copyOption(CopyOptions.InApp)
          Text('第三段文本：可以监听选中变化、复制前校验和复制完成事件。')
            .fontSize(18)
            .copyOption(CopyOptions.InApp)
        }
      }
      .copyOption(CopyOptions.InApp)
      .textJoinStyle(SelectionContainerTextJoinStyle.NEWLINE)
      .caretColor(Color.Red)
      .selectedBackgroundColor('#33007DFF')
      .onTextSelectionChange((value: Array<string>) => {
        this.selectedParts = value;
        console.info(`选中文本变化：${JSON.stringify(value)}`);
      })
      .onWillCopy((value: string) => {
        this.copiedText = `准备复制：${value}`;
        console.info(`准备复制文本：${value}`);
        return true;
      })
      .onCopy((value: string) => {
        this.copiedText = `复制成功：${value}`;
        console.info(`复制成功文本：${value}`);
      })
      .border({ width: 1, color: '#DCDCDC' })
      .padding(12)
      .width('100%')

      Text(`选中内容：${this.selectedParts.join(' | ')}`)
        .fontSize(14)
        .fontColor('#666666')

      Text(this.copiedText)
        .fontSize(14)
        .fontColor('#666666')
    }
    .width('100%')
    .padding(16)
  }
}
```

该示例通过bindSelectionMenu接口实现了跨节点选中文本时绑定自定义菜单的功能。
从API版本26.0.0开始，新增bindSelectionMenu属性。

```TypeScript
import {
  SelectionContainer,
  SelectionContainerAttribute,
  SelectionContainerMenuOptions,
  SelectionContainerTextJoinStyle
} from '@kit.ArkUI';

@Entry
@Component
struct SelectionContainerExample2 {
  @State selectedText: string = '';
  @State menuLog: string = '';

  build() {
    Column({ space: 12 }) {
      Text('请长按下方区域选择文本，体验自定义菜单')
        .fontSize(16)

      SelectionContainer() {
        Column({ space: 8 }) {
          Text('第一段文本：SelectionContainer支持自定义选择菜单。')
            .fontSize(18)
          Text('第二段文本：通过bindSelectionMenu绑定完整自定义菜单。')
            .fontSize(18)
        }
      }
      .copyOption(CopyOptions.InApp)
      .textJoinStyle(SelectionContainerTextJoinStyle.DIRECT)
      .bindSelectionMenu(
        TextSpanType.TEXT,
        this.menuBuilder,
        TextResponseType.LONG_PRESS,
        {
          onAppear: (text: string) => {
            this.menuLog = `菜单出现：${text}`;
            console.info(`菜单出现：${text}`);
          },
          onDisappear: () => {
            this.menuLog = '菜单消失';
            console.info('菜单消失');
          },
          onMenuShow: (text: string) => {
            this.menuLog = `菜单显示：${text}`;
            console.info(`菜单显示：${text}`);
          },
          onMenuHide: (text: string) => {
            this.menuLog = `菜单隐藏：${text}`;
            console.info(`菜单隐藏：${text}`);
          }
        } as SelectionContainerMenuOptions
      )
      .onTextSelectionChange((value: Array<string>) => {
        this.selectedText = `选中：${value.join(' | ')}`;
        console.info(`选中变化：${JSON.stringify(value)}`);
      })
      .border({ width: 1, color: '#DCDCDC' })
      .padding(12)
      .width('100%')
    }
    .width('100%')
    .padding(16)
  }

  @Builder
  menuBuilder() {
    Column() {
      Menu() {
        MenuItemGroup() {
          MenuItem({ content: '自定义复制', labelInfo: '' })
            .onClick(() => {
              console.info('自定义复制被点击');
            })
          MenuItem({ content: '自定义分享', labelInfo: '' })
            .onClick(() => {
              console.info('自定义分享被点击');
            })
          MenuItem({ content: '自定义翻译', labelInfo: '' })
            .onClick(() => {
              console.info('自定义翻译被点击');
            })
        }
      }
      .radius($r('sys.float.ohos_id_corner_radius_card'))
      .clip(true)
      .backgroundColor('#F0F0F0')
    }
  }
}
```

该示例通过editMenuOptions接口实现了去除系统菜单中的翻译和搜索菜单项，并添加5个自定义菜单项的功能。同时在[onMenuItemClick](arkts-arkui-onmenuitemclickwithtextcallback-t.md)回调中展示拦截系统复制操作（return true）和不拦截全选操作（return false）的差异。
从API版本26.0.0开始，新增editMenuOptions属性。

```TypeScript
import {
  OnMenuItemClickWithTextCallback,
  SelectionContainer,
  SelectionContainerAttribute,
  SelectionContainerEditMenuOptions,
  SelectionContainerTextJoinStyle
} from '@kit.ArkUI';

@Entry
@Component
struct SelectionContainerExample3 {
  @State selectedText: string = '';
  @State menuClickLog: string = '';
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    let targetIndex = menuItems.findIndex(item => item.id.equals(TextMenuItemId.TRANSLATE));
    if (targetIndex !== -1) {
      menuItems.splice(targetIndex, 1);
    }
    targetIndex = menuItems.findIndex(item => item.id.equals(TextMenuItemId.SEARCH));
    if (targetIndex !== -1) {
      menuItems.splice(targetIndex, 1);
    }
    let customItem1: TextMenuItem = {
      content: '标注',
      id: TextMenuItemId.of('highlight'),
    };
    let customItem2: TextMenuItem = {
      content: '收藏',
      id: TextMenuItemId.of('bookmark'),
    };
    let customItem3: TextMenuItem = {
      content: '批注',
      id: TextMenuItemId.of('comment'),
    };
    let customItem4: TextMenuItem = {
      content: '导出',
      id: TextMenuItemId.of('export'),
    };
    // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
    let customItem5: TextMenuItem = {
      content: '推送',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('push'),
    };
    menuItems.push(customItem1);
    menuItems.push(customItem2);
    menuItems.push(customItem3);
    menuItems.push(customItem4);
    menuItems.push(customItem5);
    return menuItems;
  }
  onMenuItemClick: OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, text: string) => {
    this.menuClickLog = `点击菜单项：${menuItem.content}，文本：${text}`;
    console.info(`点击菜单项：${menuItem.content}，文本：${text}`);
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      this.selectedText = `已复制：${text}`;
      console.info(`拦截系统复制操作，return true：${text}`);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
      this.selectedText = `全选操作：${text}`;
      console.info(`不拦截全选操作，return false：执行系统默认行为`);
      return false;
    }
    if (menuItem.id.equals(TextMenuItemId.of('highlight'))) {
      this.selectedText = `已标注：${text}`;
      console.info(`点击自定义菜单项：标注，文本：${text}`);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('bookmark'))) {
      this.selectedText = `已收藏：${text}`;
      console.info(`点击自定义菜单项：收藏，文本：${text}`);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('comment'))) {
      this.selectedText = `已批注：${text}`;
      console.info(`点击自定义菜单项：批注，文本：${text}`);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('export'))) {
      this.selectedText = `已导出：${text}`;
      console.info(`点击自定义菜单项：导出，文本：${text}`);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('push'))) {
      this.selectedText = `已推送：${text}`;
      console.info(`点击自定义菜单项：推送，文本：${text}`);
      return true;
    }
    return false;
  }
  @State editMenuOptions: SelectionContainerEditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick
  };

  build() {
    Column({ space: 12 }) {
      Text('请长按下方区域选择文本，体验扩展菜单')
        .fontSize(16)

      SelectionContainer() {
        Column({ space: 8 }) {
          Text('第一段文本：SelectionContainer支持扩展菜单选项。')
            .fontSize(18)
          Text('第二段文本：可以去除系统菜单项并添加自定义菜单项。')
            .fontSize(18)
        }
      }
      .copyOption(CopyOptions.InApp)
      .textJoinStyle(SelectionContainerTextJoinStyle.DIRECT)
      .editMenuOptions(this.editMenuOptions)
      .onTextSelectionChange((value: Array<string>) => {
        this.selectedText = `选中：${value.join(' | ')}`;
        console.info(`选中变化：${JSON.stringify(value)}`);
      })
      .border({ width: 1, color: '#DCDCDC' })
      .padding(12)
      .width('100%')

      Text(this.selectedText)
        .fontSize(14)
        .fontColor('#666666')

      Text(this.menuClickLog)
        .fontSize(14)
        .fontColor('#999999')
    }
    .width('100%')
    .padding(16)
  }
}
```

该示例通过[SelectionContainer](#接口)传入[SelectionContainerController](arkts-arkui-arkui-components-selectioncontainer-selectioncontainercontroller-c.md)，调用closeSelectionMenu和[clearTextSelection](arkts-arkui-arkui-components-selectioncontainer-selectioncontainercontroller-c.md#cleartextselection)接口展示关闭选择菜单和清除选中文本的能力。
从API版本26.0.0开始，新增[SelectionContainerController](arkts-arkui-arkui-components-selectioncontainer-selectioncontainercontroller-c.md)和[SelectionContainerOptions](arkts-arkui-arkui-components-selectioncontainer-selectioncontaineroptions-i.md)接口。

```TypeScript
import {
  SelectionContainer,
  SelectionContainerController,
  SelectionContainerAttribute
} from '@kit.ArkUI';

@Entry
@Component
struct SelectionContainerControllerExample {
  private controller: SelectionContainerController = new SelectionContainerController();

  build() {
    Column({ space: 12 }) {
      Text('请长按下方区域跨节点选中文本，再点击按钮关闭选择菜单或清除选中文本')
        .fontSize(16)

      SelectionContainer({ controller: this.controller }) {
        Column({ space: 8 }) {
          Text('第一段文本：SelectionContainer支持跨多个Text组件进行选中。')
            .fontSize(18)
            .copyOption(CopyOptions.InApp)
          Text('第二段文本：选中后可通过控制器关闭选择菜单或清除选中文本。')
            .fontSize(18)
            .copyOption(CopyOptions.InApp)
        }
      }
      .copyOption(CopyOptions.InApp)
      .border({ width: 1, color: '#DCDCDC' })
      .padding(12)
      .width('100%')

      Row({ space: 12 }) {
        Button('关闭选择菜单')
          .onClick(() => {
            this.controller.closeSelectionMenu();
          })
        Button('清除文本选中')
          .onClick(() => {
            this.controller.clearTextSelection();
          })
      }
    }
    .width('100%')
    .padding(16)
  }
}
```
