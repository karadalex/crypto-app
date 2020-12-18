import * as React from 'react';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { FontAwesome5 } from '@expo/vector-icons';
import { MaterialIcons } from '@expo/vector-icons';
import { FontAwesome } from '@expo/vector-icons';

type IconProps = { 
  name: string; 
  size: number; 
  color: string; 
  family?: string 
}

export default function Icon(props: IconProps) {
  switch (props.family) {
    case "material-community":
      return <MaterialCommunityIcons {...props} style={{ marginBottom: -3 }} />  
    case "fa5":
      return <FontAwesome5 {...props} style={{ marginBottom: -3 }} />
    case "fa":
      return <FontAwesome {...props} style={{ marginBottom: -3 }} />
    case "material":
      return <MaterialIcons {...props} style={{ marginBottom: -3 }} />
    default:
      return <MaterialCommunityIcons {...props} />  
  }
}
