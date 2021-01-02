import * as React from 'react';
import { useQuery, gql } from '@apollo/client';
import { StyleSheet, Button } from 'react-native';
import { Text, View } from '../components/Themed';
import Container from '../components/Container';
import ScreenTitle from '../components/ScreenTitle'


const PRICES_QUERY = gql`
  query PriceRecords {
    priceRecords(fromSymbol: "eur", toSymbol: "btc") {
      fromAmount,
      updatedAt
    }
  }
`;

export default function Prices() {
  const { loading, error, data, refetch } = useQuery(PRICES_QUERY);

  return (
    <Container>
      <ScreenTitle>Prices</ScreenTitle>
      {loading && <Text>Loading...</Text>}
      {error && <Text>Error :(</Text>}
      {data && (
        <React.Fragment>
          <Text>{JSON.stringify(data)}</Text>
          <Button
            onPress={() => refetch()}
            title="Refresh"
            accessibilityLabel="Refresh prices"
          />
        </React.Fragment>
      )}
    </Container>
  );
}

const styles = StyleSheet.create({
  
});
