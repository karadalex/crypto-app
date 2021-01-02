import * as React from 'react';
import { useQuery, gql } from '@apollo/client';
import { StyleSheet, Button } from 'react-native';
import { Text, View } from '../components/Themed';
import Container from '../components/Container';
import ScreenTitle from '../components/ScreenTitle'


const ASSETS_QUERY = gql`
  query UserAssets {
    userAssets {
      id,
      assetType {
        model
      },
      assetAmount
    }
  }
`;

export default function Portfolio() {
  const { loading, error, data, refetch } = useQuery(ASSETS_QUERY);

  return (
    <Container>
      <ScreenTitle>Portfolio</ScreenTitle>
      {loading && <Text>Loading...</Text>}
      {error && <Text>Error :(</Text>}
      {data && (
        <React.Fragment>
          <Text>{JSON.stringify(data)}</Text>
          <Button
            onPress={() => refetch()}
            title="Refresh"
            accessibilityLabel="Refresh assets"
          />
        </React.Fragment>
      )}
    </Container>
  );
}

const styles = StyleSheet.create({
  
});
