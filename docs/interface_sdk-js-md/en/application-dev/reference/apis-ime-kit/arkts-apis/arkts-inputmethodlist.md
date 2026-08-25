# @ohos.inputMethodList(Input Method List)

The **inputMethodList** module is oriented to system applications and input method applications.
 It provides APIs for implementing an input method list. This list displays the default input method subtypes and
 third-party input methods. Users can use this list to switch from the default input method to another input method.
 <br>
 <br> > **NOTE**
 <br> >
 <br> > This component is supported since API version 11.
 Updates will be marked with a superscript to indicate their earliest API version.
 <br>
 <br>###### Child Components
 <br>
 <br>Not supported
 <br>
 <br>###### Attributes
 <br>
 <br>The universal attributes are not supported.
 <br>
 <br>######  Events
 <br>
 <br>The universal events are not supported.
 <br>
 <br>##  Example
 <br>
 <br>```ts
 <br>import { Pattern, PatternOptions } from '@kit.IMEKit';
 <br>
 <br>@Entry
 <br>// Configure the component.
 <br>@Component
 <br>struct SettingsItem {
 <br>  @State defaultPattern: number = 1;
 <br>  private oneHandAction: PatternOptions = {
 <br>    defaultSelected: this.defaultPattern,
 <br>    patterns: [ // Icons in patterns can be used only after the corresponding icon resources have been added to
 the resource directory of the project.
 <br>      {
 <br>        icon: $r('app.media.hand_icon'), // Icon resource for the input method mode option, for example,
 the icon for the one-handed mode.
 <br>        selectedIcon: $r('app.media.hand_icon_selected') // Icon resource for the input method mode option in
 the selected state, for example, the icon for the one-handed mode in the selected state.
 <br>      },
 <br>      {
 <br>        icon: $r('app.media.hand_icon1'),
 <br>        selectedIcon: $r('app.media.hand_icon_selected1')
 <br>      },
 <br>      {
 <br>        icon: $r('app.media.hand_icon2'),
 <br>        selectedIcon: $r('app.media.hand_icon_selected2'),
 <br>      }],
 <br>    action:(index: number)=>{
 <br>      console.info(`pattern is changed, current is ${index}`);
 <br>      this.defaultPattern = index;
 <br>    }
 <br>  };
 <br>  private listController: CustomDialogController = new CustomDialogController({
 <br>    builder: InputMethodListDialog({ patternOptions: this.oneHandAction }),
 <br>    customStyle: true,
 <br>    maskColor: '#00000000'
 <br>  });
 <br>
 <br>  build() {
 <br>    Column() {
 <br>      Flex({ direction: FlexDirection.Column,
 <br>        alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
 <br>        Text("Input Method List").fontSize(20)
 <br>      }
 <br>    }
 <br>    .width("13%")
 <br>    .id('bindInputMethod')
 <br>    .onClick((event?: ClickEvent) => {
 <br>      this.listController.open();
 <br>    })
 <br>  }
 <br>}
 <br>```


## Modules to Import

```TypeScript
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
```

## Summary

### Structs

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [InputMethodListDialog(Input Method List)](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Pattern(Input Method List)](arkts-ime-inputmethodlist-pattern-i.md) |
| [PatternOptions(Input Method List)](arkts-ime-inputmethodlist-patternoptions-i.md) |
